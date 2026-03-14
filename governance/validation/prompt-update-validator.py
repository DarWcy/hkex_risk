#!/usr/bin/env python3
"""
Prompt Update Validator and Auto-Commit Script
This script validates prompt integrity and creates automatic commits for chat-prompt-en.md updates
"""

import os
import re
import subprocess
import json
from datetime import datetime
from pathlib import Path

class PromptUpdateValidator:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.prompt_file = self.project_root / "chat-prompt-en.md"
        self.expected_prompts = 15
        self.required_sections = [
            "Global Rules for Prompt Management",
            "Knowledge Base Foundation Prompts",
            "Update Records",
            "Version History",
            "Directory Structure Summary",
            "Quick Reference"
        ]
        
    def validate_prompt_integrity(self) -> dict:
        """Validate that all required prompts are present"""
        result = {
            "valid": True,
            "missing_prompts": [],
            "found_prompts": [],
            "issues": []
        }
        
        if not self.prompt_file.exists():
            result["valid"] = False
            result["issues"].append(f"Prompt file not found: {self.prompt_file}")
            return result
        
        content = self.prompt_file.read_text(encoding='utf-8')
        
        # Check for all 15 prompts
        for i in range(1, self.expected_prompts + 1):
            pattern = rf"^### Prompt {i}\s*\("
            if not re.search(pattern, content, re.MULTILINE):
                result["valid"] = False
                result["missing_prompts"].append(f"Prompt {i}")
            else:
                result["found_prompts"].append(f"Prompt {i}")
        
        # Check for required sections
        for section in self.required_sections:
            if section not in content:
                result["valid"] = False
                result["issues"].append(f"Missing required section: {section}")
        
        # Check for duplicate prompts
        prompt_pattern = r"^### Prompt \d+\s*\("
        prompts = re.findall(prompt_pattern, content, re.MULTILINE)
        if len(prompts) != len(set(prompts)):
            result["valid"] = False
            result["issues"].append("Duplicate prompts detected")
        
        return result
    
    def check_update_record_exists(self) -> bool:
        """Check if update record exists for today's changes"""
        content = self.prompt_file.read_text(encoding='utf-8')
        today = datetime.now().strftime("%Y-%m-%d")
        return f"Update {today}" in content
    
    def create_validation_report(self) -> dict:
        """Create comprehensive validation report"""
        validation_result = self.validate_prompt_integrity()
        update_record_exists = self.check_update_record_exists()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "prompt_file": str(self.prompt_file),
            "validation": validation_result,
            "update_record_exists": update_record_exists,
            "total_prompts_expected": self.expected_prompts,
            "total_prompts_found": len(validation_result["found_prompts"]),
            "ready_for_commit": validation_result["valid"] and update_record_exists
        }
        
        return report
    
    def save_validation_report(self, report: dict) -> Path:
        """Save validation report to governance directory"""
        governance_dir = self.project_root / "governance"
        governance_dir.mkdir(exist_ok=True)
        
        report_file = governance_dir / f"prompt-validation-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report_file
    
    def create_auto_commit(self, message: str) -> bool:
        """Create automatic git commit"""
        try:
            # Check if git repository
            if not (self.project_root / ".git").exists():
                print("Not a git repository, skipping commit")
                return False
            
            # Stage the prompt file
            subprocess.run(
                ["git", "add", str(self.prompt_file)],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            
            # Create commit
            commit_message = f"[AUTO-COMMIT] {message}"
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=self.project_root,
                check=True,
                capture_output=True
            )
            
            print(f"✓ Auto-commit created: {commit_message}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to create auto-commit: {e}")
            return False
        except Exception as e:
            print(f"✗ Error during auto-commit: {e}")
            return False
    
    def validate_and_commit(self, force_commit: bool = False) -> bool:
        """Main validation and commit workflow"""
        print("=" * 60)
        print("PROMPT UPDATE VALIDATOR AND AUTO-COMMIT")
        print("=" * 60)
        
        # Run validation
        report = self.create_validation_report()
        
        # Print validation results
        print(f"\nValidation Results:")
        print(f"  Total Prompts Expected: {report['total_prompts_expected']}")
        print(f"  Total Prompts Found: {report['total_prompts_found']}")
        print(f"  Validation Status: {'✓ PASSED' if report['validation']['valid'] else '✗ FAILED'}")
        print(f"  Update Record: {'✓ EXISTS' if report['update_record_exists'] else '✗ MISSING'}")
        print(f"  Ready for Commit: {'✓ YES' if report['ready_for_commit'] else '✗ NO'}")
        
        if not report['validation']['valid']:
            print(f"\n❌ Issues found:")
            for issue in report['validation']['issues']:
                print(f"  - {issue}")
            if report['validation']['missing_prompts']:
                print(f"  - Missing prompts: {', '.join(report['validation']['missing_prompts'])}")
            
            # Save validation report even if failed
            self.save_validation_report(report)
            return False
        
        if not report['update_record_exists']:
            print(f"\n⚠️  Warning: No update record found for today's changes")
            print(f"   Please add an update record in the 'Update Records' section")
            
            # Save validation report
            self.save_validation_report(report)
            
            if not force_commit:
                print(f"\n❌ Cannot proceed with auto-commit without update record")
                return False
        
        # Save validation report
        report_file = self.save_validation_report(report)
        print(f"\n📄 Validation report saved: {report_file}")
        
        # Create auto-commit
        if report['ready_for_commit'] or force_commit:
            commit_message = f"Update chat-prompt-en.md - {datetime.now().strftime('%Y-%m-%d')}"
            success = self.create_auto_commit(commit_message)
            
            if success:
                print(f"\n✅ Process completed successfully!")
                return True
            else:
                print(f"\n❌ Auto-commit failed")
                return False
        
        return False

def main():
    """Main entry point"""
    import sys
    
    # Get project root
    script_dir = Path(__file__).parent.parent
    project_root = Path.cwd()
    
    # Parse arguments
    force_commit = "--force" in sys.argv or "-f" in sys.argv
    
    # Create validator and run
    validator = PromptUpdateValidator(project_root)
    success = validator.validate_and_commit(force_commit=force_commit)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
