#!/usr/bin/env python3
"""
Test Plan Change Verification Script

This script verifies BDD scenarios and step definitions when test plans change.
It performs consistency checks, impact analysis, and generates verification reports.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class TestPlanChangeVerifier:
    """Verifies BDD consistency when test plans change."""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.test_plans_dir = self.project_root / "tests" / "test-plans"
        self.bdd_features_dir = self.project_root / "tests" / "bdd" / "features"
        self.bdd_steps_dir = self.project_root / "tests" / "bdd" / "steps"
        self.governance_dir = self.project_root / "governance"
        self.change_history_file = self.governance_dir / "change-history.md"
        
    def detect_test_plan_changes(self) -> List[Dict]:
        """Detect changes in test plan files."""
        changes = []
        
        if not self.test_plans_dir.exists():
            print(f"Test plans directory not found: {self.test_plans_dir}")
            return changes
        
        # Scan test plan files
        for test_plan_file in self.test_plans_dir.glob("test-plan-*.md"):
            # Parse test plan to extract ID and version
            test_plan_info = self._parse_test_plan(test_plan_file)
            if test_plan_info:
                changes.append({
                    'file': str(test_plan_file),
                    'test_plan_id': test_plan_info.get('id'),
                    'version': test_plan_info.get('version'),
                    'role': test_plan_info.get('role'),
                    'last_modified': datetime.fromtimestamp(test_plan_file.stat().st_mtime).isoformat()
                })
        
        return changes
    
    def _parse_test_plan(self, file_path: Path) -> Optional[Dict]:
        """Parse a test plan file to extract metadata."""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Extract test plan ID
            id_match = re.search(r'\| Test Plan ID \| (.+?) \|', content)
            test_plan_id = id_match.group(1).strip() if id_match else None
            
            # Extract version
            version_match = re.search(r'\| Version \| (.+?) \|', content)
            version = version_match.group(1).strip() if version_match else "1.0"
            
            # Extract role
            role_match = re.search(r'\| Role Type \| (.+?) \|', content)
            role = role_match.group(1).strip() if role_match else "Unknown"
            
            return {
                'id': test_plan_id,
                'version': version,
                'role': role
            }
        except Exception as e:
            print(f"Error parsing test plan {file_path}: {e}")
            return None
    
    def identify_affected_bdd(self, test_plan_id: str) -> List[Dict]:
        """Identify BDD scenarios affected by a test plan change."""
        affected_bdd = []
        
        if not self.bdd_features_dir.exists():
            print(f"BDD features directory not found: {self.bdd_features_dir}")
            return affected_bdd
        
        # Scan feature files for references to the test plan
        for feature_file in self.bdd_features_dir.glob("*.feature"):
            try:
                content = feature_file.read_text(encoding='utf-8')
                
                # Check if test plan is referenced
                if test_plan_id in content:
                    # Extract feature information
                    feature_match = re.search(r'Feature:\s*(.+)', content)
                    feature_name = feature_match.group(1).strip() if feature_match else "Unknown"
                    
                    # Count scenarios
                    scenario_count = len(re.findall(r'\n\s*Scenario:', content))
                    
                    affected_bdd.append({
                        'file': str(feature_file),
                        'feature_name': feature_name,
                        'scenario_count': scenario_count,
                        'test_plan_reference': test_plan_id
                    })
            except Exception as e:
                print(f"Error reading feature file {feature_file}: {e}")
        
        return affected_bdd
    
    def verify_bdd_consistency(self, test_plan_id: str) -> Dict:
        """Verify BDD scenarios are consistent with the test plan."""
        verification_result = {
            'test_plan_id': test_plan_id,
            'timestamp': datetime.now().isoformat() + "Z",
            'status': 'pending',
            'checks': [],
            'issues': [],
            'recommendations': []
        }
        
        # Check 1: Verify test plan exists
        test_plan_file = self._find_test_plan_file(test_plan_id)
        if not test_plan_file:
            verification_result['checks'].append({
                'check': 'Test Plan Existence',
                'status': 'failed',
                'message': f'Test plan {test_plan_id} not found'
            })
            verification_result['status'] = 'failed'
            return verification_result
        
        verification_result['checks'].append({
            'check': 'Test Plan Existence',
            'status': 'passed',
            'message': f'Test plan {test_plan_id} found'
        })
        
        # Check 2: Verify test plan approval status
        approval_status = self._check_approval_status(test_plan_id)
        verification_result['checks'].append({
            'check': 'Test Plan Approval',
            'status': 'passed' if approval_status == 'Final Approved' else 'failed',
            'message': f'Test plan status: {approval_status}'
        })
        
        if approval_status != 'Final Approved':
            verification_result['issues'].append({
                'severity': 'high',
                'message': f'Test plan {test_plan_id} is not approved. Current status: {approval_status}'
            })
        
        # Check 3: Identify affected BDD scenarios
        affected_bdd = self.identify_affected_bdd(test_plan_id)
        verification_result['checks'].append({
            'check': 'BDD Impact Analysis',
            'status': 'passed',
            'message': f'Found {len(affected_bdd)} affected BDD feature files'
        })
        
        # Check 4: Verify step definitions exist
        for bdd in affected_bdd:
            step_def_status = self._verify_step_definitions(bdd['file'])
            verification_result['checks'].append({
                'check': f'Step Definitions for {bdd["feature_name"]}',
                'status': 'passed' if step_def_status['exists'] else 'failed',
                'message': step_def_status['message']
            })
            
            if not step_def_status['exists']:
                verification_result['issues'].append({
                    'severity': 'medium',
                    'message': f'Missing step definitions for {bdd["feature_name"]}'
                })
        
        # Determine overall status
        failed_checks = [c for c in verification_result['checks'] if c['status'] == 'failed']
        if failed_checks:
            verification_result['status'] = 'failed'
        else:
            verification_result['status'] = 'passed'
        
        # Generate recommendations
        if verification_result['issues']:
            verification_result['recommendations'].append(
                'Review and address all identified issues before proceeding with BDD execution'
            )
        
        if affected_bdd:
            verification_result['recommendations'].append(
                f'Update {len(affected_bdd)} affected BDD feature files to align with test plan changes'
            )
        
        return verification_result
    
    def _find_test_plan_file(self, test_plan_id: str) -> Optional[Path]:
        """Find test plan file by ID."""
        if not self.test_plans_dir.exists():
            return None
        
        for file in self.test_plans_dir.glob("test-plan-*.md"):
            try:
                content = file.read_text(encoding='utf-8')
                if test_plan_id in content:
                    return file
            except Exception:
                continue
        
        return None
    
    def _check_approval_status(self, test_plan_id: str) -> str:
        """Check the approval status of a test plan."""
        # Look for review files
        role = test_plan_id.split('-')[2] if len(test_plan_id.split('-')) > 2 else 'unknown'
        review_file = self.governance_dir / "reviews" / f"test-plan-review-{role}.md"
        
        if review_file.exists():
            try:
                content = review_file.read_text(encoding='utf-8')
                # Extract overall status
                status_match = re.search(r'\*\*Overall Status\*\*:\s*\[\s*\]\s*(.+)', content)
                if status_match:
                    return status_match.group(1).strip()
            except Exception:
                pass
        
        return "Unknown"
    
    def _verify_step_definitions(self, feature_file: str) -> Dict:
        """Verify step definitions exist for a feature file."""
        feature_path = Path(feature_file)
        feature_name = feature_path.stem
        
        # Look for corresponding step definition file
        step_def_file = self.bdd_steps_dir / f"{feature_name}_steps.py"
        
        if step_def_file.exists():
            return {
                'exists': True,
                'message': f'Step definitions found: {step_def_file}'
            }
        
        # Check for common step definition files
        common_step_files = list(self.bdd_steps_dir.glob("*_steps.py"))
        if common_step_files:
            return {
                'exists': True,
                'message': f'Common step definitions found: {len(common_step_files)} files'
            }
        
        return {
            'exists': False,
            'message': 'No step definitions found'
        }
    
    def generate_verification_report(self, verification_result: Dict) -> str:
        """Generate a markdown verification report."""
        report = f"""# Test Plan Change Verification Report

## Summary

| Field | Value |
|-------|-------|
| Test Plan ID | {verification_result['test_plan_id']} |
| Verification Date | {verification_result['timestamp']} |
| Overall Status | {'✅ PASSED' if verification_result['status'] == 'passed' else '❌ FAILED'} |

## Verification Checks

| Check | Status | Message |
|-------|--------|---------|
"""
        
        for check in verification_result['checks']:
            status_icon = '✅' if check['status'] == 'passed' else '❌'
            report += f"| {check['check']} | {status_icon} {check['status'].upper()} | {check['message']} |\n"
        
        if verification_result['issues']:
            report += """
## Issues Identified

| Severity | Issue |
|----------|-------|
"""
            for issue in verification_result['issues']:
                severity_icon = '🔴' if issue['severity'] == 'high' else '🟡' if issue['severity'] == 'medium' else '🟢'
                report += f"| {severity_icon} {issue['severity'].upper()} | {issue['message']} |\n"
        
        if verification_result['recommendations']:
            report += """
## Recommendations

"""
            for i, rec in enumerate(verification_result['recommendations'], 1):
                report += f"{i}. {rec}\n"
        
        report += """
## Next Steps

1. Review all identified issues
2. Update affected BDD scenarios if necessary
3. Re-run verification after fixes
4. Document changes in governance/change-history.md

---

*Report generated by Test Plan Change Verifier*
"""
        
        return report
    
    def save_verification_report(self, verification_result: Dict, output_dir: Optional[str] = None):
        """Save verification report to file."""
        if output_dir is None:
            output_dir = self.governance_dir / "reviews"
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        report_file = output_dir / f"test-plan-verification-{verification_result['test_plan_id']}-{timestamp}.md"
        
        report_content = self.generate_verification_report(verification_result)
        report_file.write_text(report_content, encoding='utf-8')
        
        print(f"Verification report saved to: {report_file}")
        return report_file
    
    def update_change_history(self, verification_result: Dict):
        """Update the change history log with verification results."""
        if not self.change_history_file.exists():
            print(f"Change history file not found: {self.change_history_file}")
            return
        
        try:
            content = self.change_history_file.read_text(encoding='utf-8')
            
            # Create new entry
            new_entry = f"""
### {datetime.now().strftime('%Y-%m-%d')} - Test Plan Change Verification

| Field | Value |
|-------|-------|
| Change ID | CH-TESTPLAN-{datetime.now().strftime('%Y%m%d%H%M%S')} |
| Category | Test Plan |
| Type | Verification |
| Severity | {'High' if verification_result['status'] == 'failed' else 'Medium'} |
| Status | {'Verified' if verification_result['status'] == 'passed' else 'Issues Found'} |

**Description**:
```
Verification completed for test plan: {verification_result['test_plan_id']}
Overall Status: {verification_result['status'].upper()}
Issues Found: {len(verification_result['issues'])}
```

**Related Items**:
- **Source**: Test plan change detection
- **Dependencies**: Affected BDD scenarios

---
"""
            
            # Insert after "## Recent Changes" section
            insert_marker = "## Recent Changes"
            if insert_marker in content:
                parts = content.split(insert_marker, 1)
                updated_content = parts[0] + insert_marker + "\n" + new_entry + parts[1]
                self.change_history_file.write_text(updated_content, encoding='utf-8')
                print("Change history updated successfully")
            else:
                print("Could not find insertion point in change history")
                
        except Exception as e:
            print(f"Error updating change history: {e}")


def main():
    """Main function to run test plan change verification."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify BDD consistency when test plans change')
    parser.add_argument('--test-plan-id', help='Specific test plan ID to verify')
    parser.add_argument('--detect-all', action='store_true', help='Detect all test plan changes')
    parser.add_argument('--project-root', default='.', help='Project root directory')
    parser.add_argument('--output-dir', help='Output directory for reports')
    
    args = parser.parse_args()
    
    verifier = TestPlanChangeVerifier(args.project_root)
    
    if args.detect_all:
        print("Detecting all test plan changes...")
        changes = verifier.detect_test_plan_changes()
        print(f"Found {len(changes)} test plan(s)")
        for change in changes:
            print(f"  - {change['test_plan_id']} (Role: {change['role']}, Version: {change['version']})")
    
    elif args.test_plan_id:
        print(f"Verifying test plan: {args.test_plan_id}")
        result = verifier.verify_bdd_consistency(args.test_plan_id)
        
        # Print summary
        print(f"\nVerification Status: {result['status'].upper()}")
        print(f"Checks Performed: {len(result['checks'])}")
        print(f"Issues Found: {len(result['issues'])}")
        
        # Save report
        report_file = verifier.save_verification_report(result, args.output_dir)
        
        # Update change history
        verifier.update_change_history(result)
        
        # Return exit code based on status
        return 0 if result['status'] == 'passed' else 1
    
    else:
        print("Usage:")
        print("  python test-plan-change-verifier.py --detect-all")
        print("  python test-plan-change-verifier.py --test-plan-id TP-BA-20260318-001")
        return 1


if __name__ == "__main__":
    exit(main())
