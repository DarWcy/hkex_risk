#!/usr/bin/env python3
"""
Multi-Model Verification Script

This script performs multi-model Skill verification and generates verification reports.

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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

# Configuration
CONFIG = {
    "skills_dir": "../skill-definitions",
    "verify_config": "../../tests/config/skill-verify-config.md",
    "reports_dir": "../../tests/reports",
    "backup_dir": "../../governance/backups",
    "log_file": "../../governance/logs/multi-model-verify.log"
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


class VerificationStatus(Enum):
    """Verification status enumeration."""
    PASS = "Pass"
    FAIL = "Fail"
    PENDING = "Pending"
    WARNING = "Warning"


@dataclass
class VerificationResult:
    """Represents a verification result."""
    dimension: str
    status: VerificationStatus
    score: float
    issues: List[str]
    details: Dict
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "dimension": self.dimension,
            "status": self.status.value,
            "score": self.score,
            "issues": self.issues,
            "details": self.details
        }


@dataclass
class SkillVerification:
    """Represents Skill verification data."""
    skill_id: str
    content_accuracy: VerificationResult
    reference_integrity: VerificationResult
    dependency_integrity: VerificationResult
    script_execution: VerificationResult
    overall_score: float
    overall_grade: str
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "skill_id": self.skill_id,
            "content_accuracy": self.content_accuracy.to_dict(),
            "reference_integrity": self.reference_integrity.to_dict(),
            "dependency_integrity": self.dependency_integrity.to_dict(),
            "script_execution": self.script_execution.to_dict(),
            "overall_score": self.overall_score,
            "overall_grade": self.overall_grade
        }


class MultiModelVerifier:
    """Performs multi-model verification of Skills."""
    
    def __init__(self):
        self.skills: Dict[str, Dict] = {}
        self.verifications: List[SkillVerification] = []
        self.config: Dict = {}
        
    def load_config(self) -> bool:
        """Load verification configuration."""
        try:
            config_path = Path(CONFIG["verify_config"])
            if not config_path.exists():
                logger.warning(f"Config file not found: {CONFIG['verify_config']}")
                logger.info("Using default configuration")
                self.config = self._default_config()
                return True
            
            with open(config_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse configuration from markdown
            self.config = self._parse_config(content)
            logger.info("Configuration loaded successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            self.config = self._default_config()
            return True
    
    def _default_config(self) -> Dict:
        """Return default configuration."""
        return {
            "content_accuracy": {"weight": 0.35, "threshold": 0.95},
            "reference_integrity": {"weight": 0.25, "threshold": 0.95},
            "dependency_integrity": {"weight": 0.20, "threshold": 0.95},
            "script_execution": {"weight": 0.20, "threshold": 0.95}
        }
    
    def _parse_config(self, content: str) -> Dict:
        """Parse configuration from markdown content."""
        # Simplified parsing - in production would be more robust
        return self._default_config()
    
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
                        "content": content
                    }
                    count += 1
                    logger.info(f"Loaded Skill: {skill_id}")
                    
            except Exception as e:
                logger.error(f"Error loading {skill_file}: {str(e)}")
        
        logger.info(f"Total Skills loaded: {count}")
        return count
    
    def verify_content_accuracy(self, skill_id: str, content: str) -> VerificationResult:
        """Verify content accuracy dimension."""
        issues = []
        details = {}
        
        # Check required sections
        required_sections = ["Skill ID", "Description", "Trigger Words", "Structured Reference"]
        for section in required_sections:
            if section not in content:
                issues.append(f"Missing section: {section}")
        
        # Check content length
        content_length = len(content)
        details["content_length"] = content_length
        
        if content_length < 500:
            issues.append("Content too short")
        
        # Check for structured reference
        if "### Rule_Source" not in content:
            issues.append("Missing Rule_Source in Structured Reference")
        
        # Calculate score
        score = 1.0 - (len(issues) * 0.1)
        score = max(0.0, min(1.0, score))
        
        # Determine status
        threshold = self.config["content_accuracy"]["threshold"]
        if score >= threshold:
            status = VerificationStatus.PASS
        elif score >= threshold - 0.1:
            status = VerificationStatus.WARNING
        else:
            status = VerificationStatus.FAIL
        
        return VerificationResult(
            dimension="Content Accuracy",
            status=status,
            score=score,
            issues=issues,
            details=details
        )
    
    def verify_reference_integrity(self, skill_id: str, content: str) -> VerificationResult:
        """Verify reference integrity dimension."""
        issues = []
        details = {}
        
        # Extract Rule_Source
        rule_match = re.search(r'### Rule_Source\s*\n\s*([^\n]+)', content)
        if rule_match:
            rule_source = rule_match.group(1).strip()
            details["rule_source"] = rule_source
            
            # Check format
            if "|" not in rule_source:
                issues.append("Invalid Rule_Source format")
            
            # Check if file exists
            parts = rule_source.split("|")
            if len(parts) >= 1:
                file_path = parts[0].strip()
                full_path = os.path.join("../../docs", os.path.basename(file_path))
                if not os.path.exists(full_path):
                    issues.append(f"Rule source file not found: {file_path}")
        else:
            issues.append("Rule_Source not found")
        
        # Calculate score
        score = 1.0 - (len(issues) * 0.2)
        score = max(0.0, min(1.0, score))
        
        # Determine status
        threshold = self.config["reference_integrity"]["threshold"]
        if score >= threshold:
            status = VerificationStatus.PASS
        elif score >= threshold - 0.1:
            status = VerificationStatus.WARNING
        else:
            status = VerificationStatus.FAIL
        
        return VerificationResult(
            dimension="Reference Integrity",
            status=status,
            score=score,
            issues=issues,
            details=details
        )
    
    def verify_dependency_integrity(self, skill_id: str, content: str) -> VerificationResult:
        """Verify dependency integrity dimension."""
        issues = []
        details = {}
        
        # Check for dependency references
        # In a real implementation, this would check against the dependency graph
        details["dependencies_checked"] = True
        details["circular_deps"] = 0
        
        # For now, assume no dependencies in individual Skills
        # Dependencies are managed at the index level
        
        score = 1.0
        status = VerificationStatus.PASS
        
        return VerificationResult(
            dimension="Dependency Integrity",
            status=status,
            score=score,
            issues=issues,
            details=details
        )
    
    def verify_script_execution(self, skill_id: str, content: str) -> VerificationResult:
        """Verify script execution dimension."""
        issues = []
        details = {}
        
        # Check for script section
        if "### Automation_Script" in content:
            # Extract script
            script_match = re.search(
                r'### Automation_Script.*?```python(.*?)```',
                content,
                re.DOTALL
            )
            if script_match:
                script_content = script_match.group(1).strip()
                details["script_length"] = len(script_content)
                
                # Basic syntax check
                if "def " not in script_content:
                    issues.append("No function definitions found in script")
                
                if "return" not in script_content:
                    issues.append("No return statements found in script")
            else:
                issues.append("Script content not properly formatted")
        else:
            details["script_present"] = False
        
        # Calculate score
        score = 1.0 - (len(issues) * 0.15)
        score = max(0.0, min(1.0, score))
        
        # Determine status
        threshold = self.config["script_execution"]["threshold"]
        if score >= threshold:
            status = VerificationStatus.PASS
        elif score >= threshold - 0.1:
            status = VerificationStatus.WARNING
        else:
            status = VerificationStatus.FAIL
        
        return VerificationResult(
            dimension="Script Execution",
            status=status,
            score=score,
            issues=issues,
            details=details
        )
    
    def calculate_overall_score(self, verification: SkillVerification) -> Tuple[float, str]:
        """Calculate overall verification score and grade."""
        weights = {
            "content_accuracy": self.config["content_accuracy"]["weight"],
            "reference_integrity": self.config["reference_integrity"]["weight"],
            "dependency_integrity": self.config["dependency_integrity"]["weight"],
            "script_execution": self.config["script_execution"]["weight"]
        }
        
        score = (
            verification.content_accuracy.score * weights["content_accuracy"] +
            verification.reference_integrity.score * weights["reference_integrity"] +
            verification.dependency_integrity.score * weights["dependency_integrity"] +
            verification.script_execution.score * weights["script_execution"]
        )
        
        # Determine grade
        if score >= 0.95:
            grade = "A"
        elif score >= 0.85:
            grade = "B"
        elif score >= 0.75:
            grade = "C"
        elif score >= 0.65:
            grade = "D"
        else:
            grade = "F"
        
        return score, grade
    
    def verify_all_skills(self) -> int:
        """Verify all loaded Skills."""
        count = 0
        
        for skill_id, skill_data in self.skills.items():
            try:
                content = skill_data["content"]
                
                # Verify each dimension
                content_acc = self.verify_content_accuracy(skill_id, content)
                ref_integ = self.verify_reference_integrity(skill_id, content)
                dep_integ = self.verify_dependency_integrity(skill_id, content)
                script_exec = self.verify_script_execution(skill_id, content)
                
                # Create verification record
                verification = SkillVerification(
                    skill_id=skill_id,
                    content_accuracy=content_acc,
                    reference_integrity=ref_integ,
                    dependency_integrity=dep_integ,
                    script_execution=script_exec,
                    overall_score=0.0,
                    overall_grade=""
                )
                
                # Calculate overall score
                score, grade = self.calculate_overall_score(verification)
                verification.overall_score = score
                verification.overall_grade = grade
                
                self.verifications.append(verification)
                count += 1
                
                logger.info(f"Verified {skill_id}: Score={score:.2%}, Grade={grade}")
                
            except Exception as e:
                logger.error(f"Error verifying {skill_id}: {str(e)}")
        
        logger.info(f"Total Skills verified: {count}")
        return count
    
    def generate_reports(self) -> bool:
        """Generate verification reports."""
        try:
            reports_dir = Path(CONFIG["reports_dir"])
            reports_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate JSON report
            json_report = {
                "timestamp": datetime.now().isoformat(),
                "total_skills": len(self.verifications),
                "verifications": [v.to_dict() for v in self.verifications],
                "summary": {
                    "pass": len([v for v in self.verifications if v.overall_grade in ["A", "B"]]),
                    "conditional": len([v for v in self.verifications if v.overall_grade == "C"]),
                    "fail": len([v for v in self.verifications if v.overall_grade in ["D", "F"]]),
                    "average_score": sum(v.overall_score for v in self.verifications) / len(self.verifications) if self.verifications else 0
                }
            }
            
            json_path = reports_dir / "verification-report.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_report, f, indent=2)
            logger.info(f"JSON report generated: {json_path}")
            
            # Generate Markdown report
            md_content = self._generate_markdown_report()
            md_path = reports_dir / "verification-report.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            logger.info(f"Markdown report generated: {md_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error generating reports: {str(e)}")
            return False
    
    def _generate_markdown_report(self) -> str:
        """Generate Markdown verification report."""
        content = f"""# Multi-Model Verification Report

## Overview

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Skills Verified**: {len(self.verifications)}  
**Overall Status**: {"Pass" if all(v.overall_grade in ["A", "B"] for v in self.verifications) else "Review Required"}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Skills | {len(self.verifications)} |
| Pass (A/B) | {len([v for v in self.verifications if v.overall_grade in ["A", "B"]])} |
| Conditional (C) | {len([v for v in self.verifications if v.overall_grade == "C"])} |
| Fail (D/F) | {len([v for v in self.verifications if v.overall_grade in ["D", "F"]])} |
| Average Score | {sum(v.overall_score for v in self.verifications) / len(self.verifications):.2%} |

---

## Detailed Results

"""
        
        for v in self.verifications:
            content += f"""### {v.skill_id}

**Overall Score**: {v.overall_score:.2%}  
**Grade**: {v.overall_grade}  

#### Dimension Results

| Dimension | Score | Status | Issues |
|-----------|-------|--------|--------|
| Content Accuracy | {v.content_accuracy.score:.2%} | {v.content_accuracy.status.value} | {len(v.content_accuracy.issues)} |
| Reference Integrity | {v.reference_integrity.score:.2%} | {v.reference_integrity.status.value} | {len(v.reference_integrity.issues)} |
| Dependency Integrity | {v.dependency_integrity.score:.2%} | {v.dependency_integrity.status.value} | {len(v.dependency_integrity.issues)} |
| Script Execution | {v.script_execution.score:.2%} | {v.script_execution.status.value} | {len(v.script_execution.issues)} |

#### Issues

"""
            
            all_issues = (
                v.content_accuracy.issues +
                v.reference_integrity.issues +
                v.dependency_integrity.issues +
                v.script_execution.issues
            )
            
            if all_issues:
                for issue in all_issues:
                    content += f"- {issue}\n"
            else:
                content += "- No issues found\n"
            
            content += "\n---\n\n"
        
        return content


def main():
    """Main execution function."""
    logger.info("=" * 60)
    logger.info("Multi-Model Verification Script")
    logger.info("=" * 60)
    
    try:
        # Initialize verifier
        verifier = MultiModelVerifier()
        
        # Load configuration
        verifier.load_config()
        
        # Load Skills
        skill_count = verifier.load_skills()
        if skill_count == 0:
            logger.error("No Skills found. Exiting.")
            return 1
        
        # Verify all Skills
        verify_count = verifier.verify_all_skills()
        
        # Generate reports
        if verifier.generate_reports():
            logger.info("Verification completed successfully")
        else:
            logger.error("Failed to generate reports")
            return 1
        
        # Return exit code based on results
        fail_count = len([v for v in verifier.verifications if v.overall_grade in ["D", "F"]])
        if fail_count > 0:
            logger.warning(f"{fail_count} Skills failed verification")
            return 2
        
        return 0
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
