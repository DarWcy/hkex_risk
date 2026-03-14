#!/usr/bin/env python3
"""
Execution Result Validation Script

This script validates script execution results against expected outcomes,
including error detection and recovery verification.

Author: System
Version: 1.4
Date: 2026-03-14
"""

import os
import re
import json
import logging
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# Configuration
CONFIG = {
    "scripts_dir": ".",
    "logs_dir": "../../governance/logs",
    "reports_dir": "../../tests/reports",
    "backup_dir": "../../governance/backups",
    "log_file": "../../governance/logs/execution-result-validate.log"
}

# Scripts to validate
SCRIPTS_TO_VALIDATE = [
    "skill-reference-sync.py",
    "bdd-relationship-update.py",
    "multi-model-verify.py",
    "skill-consistency-validate.py",
    "dependency-integrity-validate.py",
    "execution-result-validate.py"
]

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


class ExecutionStatus(Enum):
    """Execution status enumeration."""
    SUCCESS = "Success"
    FAILURE = "Failure"
    PARTIAL = "Partial"
    NOT_EXECUTED = "Not Executed"


@dataclass
class ExecutionResult:
    """Represents script execution result."""
    script_id: str
    skill_id: str
    execution_status: ExecutionStatus
    exit_code: int
    output: str
    errors: str
    execution_time: float
    verification_result: str
    manual_fallback_triggered: bool
    recovery_attempted: bool
    recovery_successful: bool


@dataclass
class ValidationCheck:
    """Represents a validation check."""
    check_name: str
    expected_result: str
    actual_result: str
    passed: bool
    details: str


@dataclass
class ScriptValidation:
    """Represents script validation result."""
    script_id: str
    script_path: str
    syntax_valid: bool
    can_execute: bool
    execution_result: Optional[ExecutionResult] = None
    validation_checks: List[ValidationCheck] = field(default_factory=list)
    issues: List[str] = field(default_factory=list)
    is_valid: bool = True


class ExecutionResultValidator:
    """Validates script execution results."""
    
    def __init__(self):
        self.validations: List[ScriptValidation] = []
        self.execution_results: List[ExecutionResult] = []
        
    def validate_script_syntax(self, script_path: str) -> Tuple[bool, List[str]]:
        """Validate Python script syntax."""
        issues = []
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Try to compile the code
            compile(code, script_path, 'exec')
            logger.info(f"Syntax validation passed: {script_path}")
            return True, issues
            
        except SyntaxError as e:
            issues.append(f"Syntax error at line {e.lineno}: {e.msg}")
            logger.error(f"Syntax error in {script_path}: {e}")
            return False, issues
        except Exception as e:
            issues.append(f"Error validating syntax: {str(e)}")
            logger.error(f"Error validating {script_path}: {e}")
            return False, issues
    
    def check_script_structure(self, script_path: str) -> Tuple[bool, List[str]]:
        """Check script has required structure."""
        issues = []
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for main function
            if 'def main():' not in content:
                issues.append("Missing main() function")
            
            # Check for if __name__ == "__main__"
            if 'if __name__ == "__main__":' not in content:
                issues.append("Missing if __name__ == '__main__' block")
            
            # Check for docstring
            if '"""' not in content and "'''" not in content:
                issues.append("Missing module docstring")
            
            # Check for logging setup
            if 'logging' not in content:
                issues.append("Missing logging setup")
            
            return len(issues) == 0, issues
            
        except Exception as e:
            issues.append(f"Error checking structure: {str(e)}")
            return False, issues
    
    def execute_script(self, script_path: str) -> Tuple[ExecutionResult, float]:
        """Execute a script and capture results."""
        script_id = Path(script_path).stem
        start_time = datetime.now()
        
        try:
            # Execute script with timeout
            result = subprocess.run(
                ['python', script_path],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=os.path.dirname(script_path) or '.'
            )
            
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            # Determine status based on exit code
            if result.returncode == 0:
                status = ExecutionStatus.SUCCESS
            elif result.returncode == 2:
                status = ExecutionStatus.PARTIAL
            else:
                status = ExecutionStatus.FAILURE
            
            exec_result = ExecutionResult(
                script_id=script_id,
                skill_id="N/A",
                execution_status=status,
                exit_code=result.returncode,
                output=result.stdout[-1000:] if len(result.stdout) > 1000 else result.stdout,  # Limit output
                errors=result.stderr[-1000:] if len(result.stderr) > 1000 else result.stderr,
                execution_time=execution_time,
                verification_result="Pending",
                manual_fallback_triggered=False,
                recovery_attempted=False,
                recovery_successful=False
            )
            
            logger.info(f"Executed {script_id}: {status.value} (exit code {result.returncode})")
            return exec_result, execution_time
            
        except subprocess.TimeoutExpired:
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            exec_result = ExecutionResult(
                script_id=script_id,
                skill_id="N/A",
                execution_status=ExecutionStatus.FAILURE,
                exit_code=-1,
                output="",
                errors="Execution timed out after 60 seconds",
                execution_time=execution_time,
                verification_result="Failed",
                manual_fallback_triggered=True,
                recovery_attempted=True,
                recovery_successful=False
            )
            
            logger.error(f"Execution timeout: {script_id}")
            return exec_result, execution_time
            
        except Exception as e:
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            
            exec_result = ExecutionResult(
                script_id=script_id,
                skill_id="N/A",
                execution_status=ExecutionStatus.FAILURE,
                exit_code=-1,
                output="",
                errors=str(e),
                execution_time=execution_time,
                verification_result="Failed",
                manual_fallback_triggered=True,
                recovery_attempted=True,
                recovery_successful=False
            )
            
            logger.error(f"Execution error: {script_id} - {e}")
            return exec_result, execution_time
    
    def validate_execution_result(self, exec_result: ExecutionResult) -> List[ValidationCheck]:
        """Validate execution result against expectations."""
        checks = []
        
        # Check 1: Exit code validation
        expected_exit = 0
        actual_exit = exec_result.exit_code
        checks.append(ValidationCheck(
            check_name="Exit Code",
            expected_result=str(expected_exit),
            actual_result=str(actual_exit),
            passed=actual_exit == expected_exit or actual_exit == 2,  # 0 or 2 (partial) is acceptable
            details=f"Exit code {actual_exit} {'acceptable' if actual_exit in [0, 2] else 'unexpected'}"
        ))
        
        # Check 2: No critical errors
        has_critical_error = any(keyword in exec_result.errors.lower() 
                                 for keyword in ['error', 'exception', 'fatal', 'critical'])
        checks.append(ValidationCheck(
            check_name="No Critical Errors",
            expected_result="No critical errors",
            actual_result="Critical errors found" if has_critical_error else "No critical errors",
            passed=not has_critical_error,
            details=exec_result.errors[:200] if has_critical_error else "No errors detected"
        ))
        
        # Check 3: Execution time
        max_time = 60  # seconds
        checks.append(ValidationCheck(
            check_name="Execution Time",
            expected_result=f"< {max_time}s",
            actual_result=f"{exec_result.execution_time:.2f}s",
            passed=exec_result.execution_time < max_time,
            details=f"Execution completed in {exec_result.execution_time:.2f} seconds"
        ))
        
        # Check 4: Output validation
        has_output = len(exec_result.output) > 0
        checks.append(ValidationCheck(
            check_name="Output Generated",
            expected_result="Output present",
            actual_result="Output present" if has_output else "No output",
            passed=has_output,
            details=f"Output length: {len(exec_result.output)} characters"
        ))
        
        # Check 5: Log file created
        log_file = os.path.join(CONFIG["logs_dir"], f"{exec_result.script_id}.log")
        log_exists = os.path.exists(log_file)
        checks.append(ValidationCheck(
            check_name="Log File Created",
            expected_result="Log file exists",
            actual_result="Log file exists" if log_exists else "Log file missing",
            passed=log_exists,
            details=f"Log file: {log_file}"
        ))
        
        return checks
    
    def validate_script(self, script_name: str) -> ScriptValidation:
        """Validate a single script."""
        script_path = os.path.join(CONFIG["scripts_dir"], script_name)
        script_id = Path(script_name).stem
        
        validation = ScriptValidation(
            script_id=script_id,
            script_path=script_path
        )
        
        # Check if file exists
        if not os.path.exists(script_path):
            validation.issues.append(f"Script file not found: {script_path}")
            validation.is_valid = False
            return validation
        
        # Validate syntax
        syntax_valid, syntax_issues = self.validate_script_syntax(script_path)
        validation.syntax_valid = syntax_valid
        if not syntax_valid:
            validation.issues.extend(syntax_issues)
            validation.is_valid = False
            return validation
        
        # Check structure
        structure_valid, structure_issues = self.check_script_structure(script_path)
        if not structure_valid:
            validation.issues.extend(structure_issues)
        
        # Execute script
        try:
            exec_result, exec_time = self.execute_script(script_path)
            validation.execution_result = exec_result
            self.execution_results.append(exec_result)
            
            # Validate execution result
            validation.validation_checks = self.validate_execution_result(exec_result)
            
            # Determine overall validity
            validation.can_execute = exec_result.execution_status != ExecutionStatus.FAILURE
            validation.is_valid = all(check.passed for check in validation.validation_checks)
            
        except Exception as e:
            validation.issues.append(f"Execution failed: {str(e)}")
            validation.can_execute = False
            validation.is_valid = False
        
        return validation
    
    def validate_all_scripts(self) -> int:
        """Validate all scripts."""
        count = 0
        
        for script_name in SCRIPTS_TO_VALIDATE:
            try:
                validation = self.validate_script(script_name)
                self.validations.append(validation)
                count += 1
                
                status = "VALID" if validation.is_valid else "INVALID"
                logger.info(f"Validated {script_name}: {status}")
                
            except Exception as e:
                logger.error(f"Error validating {script_name}: {str(e)}")
        
        logger.info(f"Total scripts validated: {count}")
        return count
    
    def generate_verification_table(self) -> str:
        """Generate execution result verification table."""
        lines = [
            "# Execution Result Verification Table\n",
            "## Overview\n",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            f"**Total Scripts**: {len(self.validations)}\n\n",
            "## Verification Table\n",
            "| Script ID | Skill ID | Execution Status | Exit Code | Verification Result | Manual Fallback | Recovery Attempted | Recovery Successful |",
            "|-----------|----------|------------------|-----------|---------------------|-----------------|-------------------|---------------------|"
        ]
        
        for validation in self.validations:
            if validation.execution_result:
                er = validation.execution_result
                lines.append(
                    f"| {er.script_id} | {er.skill_id} | {er.execution_status.value} | "
                    f"{er.exit_code} | {er.verification_result} | "
                    f"{'Yes' if er.manual_fallback_triggered else 'No'} | "
                    f"{'Yes' if er.recovery_attempted else 'No'} | "
                    f"{'Yes' if er.recovery_successful else 'No'} |"
                )
        
        lines.extend([
            "\n## Validation Checks Detail\n",
            "| Script ID | Check Name | Expected | Actual | Passed |",
            "|-----------|------------|----------|--------|--------|"
        ])
        
        for validation in self.validations:
            for check in validation.validation_checks:
                lines.append(
                    f"| {validation.script_id} | {check.check_name} | "
                    f"{check.expected_result} | {check.actual_result} | "
                    f"{'✓' if check.passed else '✗'} |"
                )
        
        lines.append("\n## Notes\n")
        lines.append("- **Execution Status**: Success (0), Partial (2), Failure (other)\n")
        lines.append("- **Manual Fallback**: Triggered when automatic recovery fails\n")
        lines.append("- **Recovery**: Automatic error recovery attempts\n")
        
        return "\n".join(lines)
    
    def generate_report(self) -> bool:
        """Generate validation report."""
        try:
            reports_dir = Path(CONFIG["reports_dir"])
            reports_dir.mkdir(parents=True, exist_ok=True)
            
            # Calculate summary
            total_valid = sum(1 for v in self.validations if v.is_valid)
            total_syntax_valid = sum(1 for v in self.validations if v.syntax_valid)
            total_can_execute = sum(1 for v in self.validations if v.can_execute)
            
            # Generate JSON report
            json_report = {
                "timestamp": datetime.now().isoformat(),
                "summary": {
                    "total_scripts": len(self.validations),
                    "valid": total_valid,
                    "invalid": len(self.validations) - total_valid,
                    "syntax_valid": total_syntax_valid,
                    "can_execute": total_can_execute
                },
                "validations": [
                    {
                        "script_id": v.script_id,
                        "script_path": v.script_path,
                        "syntax_valid": v.syntax_valid,
                        "can_execute": v.can_execute,
                        "is_valid": v.is_valid,
                        "issues": v.issues,
                        "execution_result": {
                            "status": v.execution_result.execution_status.value if v.execution_result else None,
                            "exit_code": v.execution_result.exit_code if v.execution_result else None,
                            "execution_time": v.execution_result.execution_time if v.execution_result else None,
                            "errors": v.execution_result.errors if v.execution_result else None
                        } if v.execution_result else None,
                        "validation_checks": [
                            {
                                "check_name": c.check_name,
                                "expected": c.expected_result,
                                "actual": c.actual_result,
                                "passed": c.passed
                            }
                            for c in v.validation_checks
                        ]
                    }
                    for v in self.validations
                ]
            }
            
            json_path = reports_dir / "execution-validation-report.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_report, f, indent=2)
            logger.info(f"JSON report generated: {json_path}")
            
            # Generate Markdown report
            md_content = self._generate_markdown_report()
            md_path = reports_dir / "execution-validation-report.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            logger.info(f"Markdown report generated: {md_path}")
            
            # Generate verification table
            table_content = self.generate_verification_table()
            table_path = reports_dir / "execution-verification-table.md"
            with open(table_path, 'w', encoding='utf-8') as f:
                f.write(table_content)
            logger.info(f"Verification table generated: {table_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            return False
    
    def _generate_markdown_report(self) -> str:
        """Generate Markdown validation report."""
        total_valid = sum(1 for v in self.validations if v.is_valid)
        total_syntax_valid = sum(1 for v in self.validations if v.syntax_valid)
        total_can_execute = sum(1 for v in self.validations if v.can_execute)
        
        content = f"""# Execution Result Validation Report

## Overview

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Scripts**: {len(self.validations)}  
**Overall Status**: {"Pass" if total_valid == len(self.validations) else "Issues Found"}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Scripts | {len(self.validations)} |
| Valid | {total_valid} |
| Invalid | {len(self.validations) - total_valid} |
| Syntax Valid | {total_syntax_valid} |
| Can Execute | {total_can_execute} |

---

## Detailed Results

"""
        
        for validation in self.validations:
            status_icon = "✓" if validation.is_valid else "✗"
            content += f"""### {status_icon} {validation.script_id}

**Script Path**: {validation.script_path}  
**Syntax Valid**: {'Yes' if validation.syntax_valid else 'No'}  
**Can Execute**: {'Yes' if validation.can_execute else 'No'}  
**Overall Valid**: {'Yes' if validation.is_valid else 'No'}  

"""
            
            if validation.execution_result:
                er = validation.execution_result
                content += f"""#### Execution Result

- **Status**: {er.execution_status.value}
- **Exit Code**: {er.exit_code}
- **Execution Time**: {er.execution_time:.2f}s
- **Verification Result**: {er.verification_result}
- **Manual Fallback Triggered**: {'Yes' if er.manual_fallback_triggered else 'No'}
- **Recovery Attempted**: {'Yes' if er.recovery_attempted else 'No'}
- **Recovery Successful**: {'Yes' if er.recovery_successful else 'No'}

"""
                
                if er.errors:
                    content += f"**Errors**:\n```\n{er.errors[:500]}\n```\n\n"
            
            if validation.validation_checks:
                content += "#### Validation Checks\n\n"
                content += "| Check | Expected | Actual | Passed |\n"
                content += "|-------|----------|--------|--------|\n"
                for check in validation.validation_checks:
                    content += f"| {check.check_name} | {check.expected_result} | {check.actual_result} | {'✓' if check.passed else '✗'} |\n"
                content += "\n"
            
            if validation.issues:
                content += "#### Issues\n\n"
                for issue in validation.issues:
                    content += f"- {issue}\n"
            else:
                content += "*No issues found*\n"
            
            content += "\n---\n\n"
        
        return content


def main():
    """Main execution function."""
    logger.info("=" * 60)
    logger.info("Execution Result Validation Script")
    logger.info("=" * 60)
    
    try:
        # Initialize validator
        validator = ExecutionResultValidator()
        
        # Validate all scripts
        validate_count = validator.validate_all_scripts()
        
        if validate_count == 0:
            logger.error("No scripts validated. Exiting.")
            return 1
        
        # Generate report
        if validator.generate_report():
            logger.info("Validation completed successfully")
        else:
            logger.error("Failed to generate report")
            return 1
        
        # Return exit code based on results
        invalid_count = sum(1 for v in validator.validations if not v.is_valid)
        if invalid_count > 0:
            logger.warning(f"{invalid_count} scripts have validation issues")
            return 2
        
        return 0
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
