#!/usr/bin/env python3
"""
Skill Consistency Validation Script

This script verifies Skill consistency across all prompts,
including naming conventions, structure, and references.

Author: System
Version: 1.4
Date: 2026-03-14
"""

import os
import re
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field

# Configuration
CONFIG = {
    "skills_dir": "../skill-definitions",
    "docs_dir": "../../docs",
    "index_file": "../../tests/index.md",
    "relation_file": "../../tests/skill-bdd-relation.md",
    "reports_dir": "../../tests/reports",
    "log_file": "../../governance/logs/skill-consistency-validate.log"
}

# Setup logging
def setup_logging():
    """Configure logging for the script."""
    log_dir = os.path.dirname(CONFIG["log_file"])
    os.makedirs(log_dir, exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(CONFIG["log_file"]),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()


@dataclass
class ConsistencyIssue:
    """Represents a consistency issue."""
    skill_id: str
    issue_type: str
    severity: str  # ERROR, WARNING, INFO
    message: str
    suggestion: str


@dataclass
class ValidationResult:
    """Represents validation result for a Skill."""
    skill_id: str
    is_valid: bool
    issues: List[ConsistencyIssue] = field(default_factory=list)
    checks_passed: int = 0
    checks_failed: int = 0


class SkillConsistencyValidator:
    """Validates Skill consistency across all prompts."""
    
    # Naming convention pattern: {business}-{module}-{capability}
    SKILL_ID_PATTERN = re.compile(r'^[a-z]+-[a-z]+(-[a-z]+)+$')
    
    # Required sections in Skill files
    REQUIRED_SECTIONS = [
        "Skill ID",
        "Description",
        "Trigger Words",
        "User Type Target",
        "Skill Source",
        "Structured Reference",
        "BDD Association Pre-embedding",
        "Script"
    ]
    
    # Valid user types
    VALID_USER_TYPES = ["Type A", "Type B", "Type C", "Type D", "Type A+B", "Type B+C", "Type A+C"]
    
    def __init__(self):
        self.skills: Dict[str, Dict] = {}
        self.index_skills: Set[str] = set()
        self.relation_skills: Set[str] = set()
        self.validation_results: List[ValidationResult] = []
        
    def load_skills(self) -> int:
        """Load all Skills from the skills directory."""
        skills_path = Path(CONFIG["skills_dir"])
        if not skills_path.exists():
            logger.error(f"Skills directory not found: {CONFIG['skills_dir']}")
            return 0
        
        count = 0
        for skill_file in skills_path.glob("*.md"):
            try:
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract Skill ID
                skill_id_match = re.search(r'## Skill ID\s*\n\s*(\S+)', content)
                if skill_id_match:
                    skill_id = skill_id_match.group(1).strip()
                    
                    self.skills[skill_id] = {
                        "file": str(skill_file),
                        "content": content,
                        "filename": skill_file.name
                    }
                    count += 1
                    logger.info(f"Loaded Skill: {skill_id}")
                    
            except Exception as e:
                logger.error(f"Error loading {skill_file}: {str(e)}")
        
        logger.info(f"Total Skills loaded: {count}")
        return count
    
    def load_index_skills(self) -> int:
        """Load Skills listed in the index file."""
        try:
            index_path = Path(CONFIG["index_file"])
            if not index_path.exists():
                logger.warning(f"Index file not found: {CONFIG['index_file']}")
                return 0
            
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract Skill IDs from index table
            skill_matches = re.findall(r'\|\s*(hkex-[a-z-]+)\s*\|', content)
            self.index_skills = set(skill_matches)
            
            logger.info(f"Skills in index: {len(self.index_skills)}")
            return len(self.index_skills)
            
        except Exception as e:
            logger.error(f"Error loading index: {str(e)}")
            return 0
    
    def load_relation_skills(self) -> int:
        """Load Skills listed in the relation file."""
        try:
            relation_path = Path(CONFIG["relation_file"])
            if not relation_path.exists():
                logger.warning(f"Relation file not found: {CONFIG['relation_file']}")
                return 0
            
            with open(relation_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract Skill IDs from relation table
            skill_matches = re.findall(r'\|\s*(hkex-[a-z-]+)\s*\|', content)
            self.relation_skills = set(skill_matches)
            
            logger.info(f"Skills in relation: {len(self.relation_skills)}")
            return len(self.relation_skills)
            
        except Exception as e:
            logger.error(f"Error loading relation: {str(e)}")
            return 0
    
    def validate_naming_convention(self, skill_id: str) -> Tuple[bool, Optional[ConsistencyIssue]]:
        """Validate Skill ID naming convention."""
        if not self.SKILL_ID_PATTERN.match(skill_id):
            issue = ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Naming Convention",
                severity="ERROR",
                message=f"Skill ID '{skill_id}' does not match naming convention: {{business}}-{{module}}-{{capability}}",
                suggestion="Rename to follow pattern: hkex-{module}-{capability} (all lowercase, hyphen-separated)"
            )
            return False, issue
        
        return True, None
    
    def validate_filename_consistency(self, skill_id: str, filename: str) -> Tuple[bool, Optional[ConsistencyIssue]]:
        """Validate filename matches Skill ID."""
        expected_filename = f"{skill_id}.md"
        if filename != expected_filename:
            issue = ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Filename Consistency",
                severity="ERROR",
                message=f"Filename '{filename}' does not match Skill ID '{skill_id}'",
                suggestion=f"Rename file to: {expected_filename}"
            )
            return False, issue
        
        return True, None
    
    def validate_required_sections(self, skill_id: str, content: str) -> Tuple[int, int, List[ConsistencyIssue]]:
        """Validate all required sections are present."""
        passed = 0
        failed = 0
        issues = []
        
        for section in self.REQUIRED_SECTIONS:
            # Check for section header
            pattern = rf'##\s*{re.escape(section)}'
            if re.search(pattern, content):
                passed += 1
            else:
                failed += 1
                issues.append(ConsistencyIssue(
                    skill_id=skill_id,
                    issue_type="Missing Section",
                    severity="ERROR",
                    message=f"Required section '{section}' is missing",
                    suggestion=f"Add '## {section}' section to the Skill file"
                ))
        
        return passed, failed, issues
    
    def validate_user_type(self, skill_id: str, content: str) -> Tuple[bool, Optional[ConsistencyIssue]]:
        """Validate user type is valid."""
        user_type_match = re.search(r'## User Type Target\s*\n\s*(.+)', content)
        if user_type_match:
            user_type = user_type_match.group(1).strip()
            
            # Check if user type is valid
            is_valid = any(valid_type in user_type for valid_type in self.VALID_USER_TYPES)
            
            if not is_valid:
                issue = ConsistencyIssue(
                    skill_id=skill_id,
                    issue_type="Invalid User Type",
                    severity="ERROR",
                    message=f"User type '{user_type}' is not valid",
                    suggestion=f"Use one of: {', '.join(self.VALID_USER_TYPES)}"
                )
                return False, issue
        else:
            issue = ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Missing User Type",
                severity="ERROR",
                message="User Type Target section is missing or empty",
                suggestion="Add '## User Type Target' section with valid user type"
            )
            return False, issue
        
        return True, None
    
    def validate_trigger_words(self, skill_id: str, content: str) -> Tuple[bool, Optional[ConsistencyIssue]]:
        """Validate trigger words are present and sufficient."""
        trigger_match = re.search(r'## Trigger Words\s*\n(.+?)(?=##|$)', content, re.DOTALL)
        if trigger_match:
            trigger_section = trigger_match.group(1)
            # Count trigger words (lines starting with - or *)
            triggers = re.findall(r'^[\s]*[-*][\s]+(.+)', trigger_section, re.MULTILINE)
            
            if len(triggers) < 3:
                issue = ConsistencyIssue(
                    skill_id=skill_id,
                    issue_type="Insufficient Trigger Words",
                    severity="WARNING",
                    message=f"Only {len(triggers)} trigger words found (minimum 3 required)",
                    suggestion="Add more trigger words to improve Skill discoverability"
                )
                return False, issue
        else:
            issue = ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Missing Trigger Words",
                severity="ERROR",
                message="Trigger Words section is missing or empty",
                suggestion="Add '## Trigger Words' section with at least 3 trigger words"
            )
            return False, issue
        
        return True, None
    
    def validate_structured_reference(self, skill_id: str, content: str) -> List[ConsistencyIssue]:
        """Validate structured reference format."""
        issues = []
        
        # Check for Structured Reference section
        if "## Structured Reference" not in content:
            issues.append(ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Missing Structured Reference",
                severity="ERROR",
                message="Structured Reference section is missing",
                suggestion="Add '## Structured Reference' section with all required sub-sections"
            ))
            return issues
        
        # Check required sub-sections
        required_subsections = ["Rule_Source", "Test_Reference", "Verify_Reference", "Update_History"]
        for subsection in required_subsections:
            pattern = rf'###\s*{subsection}'
            if not re.search(pattern, content):
                issues.append(ConsistencyIssue(
                    skill_id=skill_id,
                    issue_type="Missing Reference Subsection",
                    severity="ERROR",
                    message=f"Reference subsection '{subsection}' is missing",
                    suggestion=f"Add '### {subsection}' subsection to Structured Reference"
                ))
        
        return issues
    
    def validate_index_consistency(self, skill_id: str) -> Tuple[bool, Optional[ConsistencyIssue]]:
        """Validate Skill is listed in index."""
        if skill_id not in self.index_skills:
            issue = ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Missing from Index",
                severity="WARNING",
                message=f"Skill '{skill_id}' is not listed in the index file",
                suggestion="Add Skill to tests/index.md Skill index table"
            )
            return False, issue
        
        return True, None
    
    def validate_relation_consistency(self, skill_id: str) -> Tuple[bool, Optional[ConsistencyIssue]]:
        """Validate Skill is listed in relation file."""
        if skill_id not in self.relation_skills:
            issue = ConsistencyIssue(
                skill_id=skill_id,
                issue_type="Missing from Relation",
                severity="WARNING",
                message=f"Skill '{skill_id}' is not listed in the relation file",
                suggestion="Add Skill to tests/skill-bdd-relation.md relationship table"
            )
            return False, issue
        
        return True, None
    
    def validate_skill(self, skill_id: str, skill_data: Dict) -> ValidationResult:
        """Validate a single Skill."""
        result = ValidationResult(skill_id=skill_id, is_valid=True)
        content = skill_data["content"]
        filename = skill_data["filename"]
        
        # Validate naming convention
        valid, issue = self.validate_naming_convention(skill_id)
        if not valid:
            result.issues.append(issue)
            result.checks_failed += 1
        else:
            result.checks_passed += 1
        
        # Validate filename consistency
        valid, issue = self.validate_filename_consistency(skill_id, filename)
        if not valid:
            result.issues.append(issue)
            result.checks_failed += 1
        else:
            result.checks_passed += 1
        
        # Validate required sections
        passed, failed, issues = self.validate_required_sections(skill_id, content)
        result.checks_passed += passed
        result.checks_failed += failed
        result.issues.extend(issues)
        
        # Validate user type
        valid, issue = self.validate_user_type(skill_id, content)
        if not valid:
            result.issues.append(issue)
            result.checks_failed += 1
        else:
            result.checks_passed += 1
        
        # Validate trigger words
        valid, issue = self.validate_trigger_words(skill_id, content)
        if not valid:
            result.issues.append(issue)
            result.checks_failed += 1
        else:
            result.checks_passed += 1
        
        # Validate structured reference
        ref_issues = self.validate_structured_reference(skill_id, content)
        result.issues.extend(ref_issues)
        result.checks_failed += len(ref_issues)
        if not ref_issues:
            result.checks_passed += 1
        
        # Validate index consistency
        valid, issue = self.validate_index_consistency(skill_id)
        if not valid:
            result.issues.append(issue)
            result.checks_failed += 1
        else:
            result.checks_passed += 1
        
        # Validate relation consistency
        valid, issue = self.validate_relation_consistency(skill_id)
        if not valid:
            result.issues.append(issue)
            result.checks_failed += 1
        else:
            result.checks_passed += 1
        
        # Determine overall validity
        result.is_valid = result.checks_failed == 0
        
        return result
    
    def validate_all_skills(self) -> int:
        """Validate all loaded Skills."""
        count = 0
        
        for skill_id, skill_data in self.skills.items():
            try:
                result = self.validate_skill(skill_id, skill_data)
                self.validation_results.append(result)
                count += 1
                
                status = "VALID" if result.is_valid else "INVALID"
                logger.info(f"Validated {skill_id}: {status} ({result.checks_passed}/{result.checks_passed + result.checks_failed} checks passed)")
                
            except Exception as e:
                logger.error(f"Error validating {skill_id}: {str(e)}")
        
        logger.info(f"Total Skills validated: {count}")
        return count
    
    def generate_report(self) -> bool:
        """Generate validation report."""
        try:
            reports_dir = Path(CONFIG["reports_dir"])
            reports_dir.mkdir(parents=True, exist_ok=True)
            
            # Calculate summary
            total_valid = sum(1 for r in self.validation_results if r.is_valid)
            total_invalid = len(self.validation_results) - total_valid
            total_issues = sum(len(r.issues) for r in self.validation_results)
            
            # Generate JSON report
            json_report = {
                "timestamp": datetime.now().isoformat(),
                "summary": {
                    "total_skills": len(self.validation_results),
                    "valid": total_valid,
                    "invalid": total_invalid,
                    "total_issues": total_issues
                },
                "results": [
                    {
                        "skill_id": r.skill_id,
                        "is_valid": r.is_valid,
                        "checks_passed": r.checks_passed,
                        "checks_failed": r.checks_failed,
                        "issues": [
                            {
                                "type": i.issue_type,
                                "severity": i.severity,
                                "message": i.message,
                                "suggestion": i.suggestion
                            }
                            for i in r.issues
                        ]
                    }
                    for r in self.validation_results
                ]
            }
            
            json_path = reports_dir / "consistency-validation-report.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_report, f, indent=2)
            logger.info(f"JSON report generated: {json_path}")
            
            # Generate Markdown report
            md_content = self._generate_markdown_report()
            md_path = reports_dir / "consistency-validation-report.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            logger.info(f"Markdown report generated: {md_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            return False
    
    def _generate_markdown_report(self) -> str:
        """Generate Markdown validation report."""
        total_valid = sum(1 for r in self.validation_results if r.is_valid)
        total_invalid = len(self.validation_results) - total_valid
        total_issues = sum(len(r.issues) for r in self.validation_results)
        
        content = f"""# Skill Consistency Validation Report

## Overview

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Skills Validated**: {len(self.validation_results)}  
**Overall Status**: {"Pass" if total_invalid == 0 else "Issues Found"}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Skills | {len(self.validation_results)} |
| Valid | {total_valid} |
| Invalid | {total_invalid} |
| Total Issues | {total_issues} |

---

## Detailed Results

"""
        
        for result in self.validation_results:
            status_icon = "✓" if result.is_valid else "✗"
            content += f"""### {status_icon} {result.skill_id}

**Status**: {"Valid" if result.is_valid else "Invalid"}  
**Checks Passed**: {result.checks_passed}  
**Checks Failed**: {result.checks_failed}  

"""
            
            if result.issues:
                content += "#### Issues\n\n"
                content += "| Type | Severity | Message | Suggestion |\n"
                content += "|------|----------|---------|------------|\n"
                
                for issue in result.issues:
                    content += f"| {issue.issue_type} | {issue.severity} | {issue.message} | {issue.suggestion} |\n"
            else:
                content += "*No issues found*\n"
            
            content += "\n---\n\n"
        
        return content


def main():
    """Main execution function."""
    logger.info("=" * 60)
    logger.info("Skill Consistency Validation Script")
    logger.info("=" * 60)
    
    try:
        # Initialize validator
        validator = SkillConsistencyValidator()
        
        # Load Skills
        skill_count = validator.load_skills()
        if skill_count == 0:
            logger.error("No Skills found. Exiting.")
            return 1
        
        # Load index and relation Skills
        validator.load_index_skills()
        validator.load_relation_skills()
        
        # Validate all Skills
        validate_count = validator.validate_all_skills()
        
        # Generate report
        if validator.generate_report():
            logger.info("Validation completed successfully")
        else:
            logger.error("Failed to generate report")
            return 1
        
        # Return exit code based on results
        invalid_count = sum(1 for r in validator.validation_results if not r.is_valid)
        if invalid_count > 0:
            logger.warning(f"{invalid_count} Skills have consistency issues")
            return 2
        
        return 0
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
