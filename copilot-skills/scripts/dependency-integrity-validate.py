#!/usr/bin/env python3
"""
Dependency Integrity Validation Script

This script verifies Skill dependency relationships integrity,
including circular dependencies and missing references.

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
from typing import Dict, List, Optional, Set, Tuple
from collections import defaultdict
from dataclasses import dataclass, field

# Configuration
CONFIG = {
    "skills_dir": "../skill-definitions",
    "relation_file": "../../tests/skill-bdd-relation.md",
    "index_file": "../../tests/index.md",
    "reports_dir": "../../tests/reports",
    "log_file": "../../governance/logs/dependency-integrity-validate.log"
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
class Dependency:
    """Represents a dependency relationship."""
    source: str
    target: str
    dep_type: str  # Direct, Indirect, Contextual
    strength: str  # Strong, Medium, Weak


@dataclass
class DependencyIssue:
    """Represents a dependency issue."""
    issue_type: str
    severity: str  # ERROR, WARNING, INFO
    message: str
    affected_skills: List[str]
    suggestion: str


@dataclass
class ValidationResult:
    """Represents dependency validation result."""
    skill_id: str
    dependencies: List[Dependency] = field(default_factory=list)
    issues: List[DependencyIssue] = field(default_factory=list)
    is_valid: bool = True


class DependencyIntegrityValidator:
    """Validates Skill dependency relationships integrity."""
    
    def __init__(self):
        self.skills: Set[str] = set()
        self.dependencies: List[Dependency] = []
        self.dependency_graph: Dict[str, List[str]] = defaultdict(list)
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
                # Extract Skill ID from filename
                skill_id = skill_file.stem
                self.skills.add(skill_id)
                count += 1
                logger.info(f"Loaded Skill: {skill_id}")
                    
            except Exception as e:
                logger.error(f"Error loading {skill_file}: {str(e)}")
        
        logger.info(f"Total Skills loaded: {count}")
        return count
    
    def load_dependencies(self) -> int:
        """Load dependencies from relation file."""
        try:
            relation_path = Path(CONFIG["relation_file"])
            if not relation_path.exists():
                logger.warning(f"Relation file not found: {CONFIG['relation_file']}")
                return 0
            
            with open(relation_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find dependency relationship table
            in_dep_table = False
            for line in content.split('\n'):
                if 'Source Skill ID' in line and 'Target Skill ID' in line:
                    in_dep_table = True
                    continue
                
                if in_dep_table and line.startswith('|') and '---' not in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 6:
                        source = parts[1]
                        target = parts[2]
                        dep_type = parts[3]
                        strength = parts[4]
                        
                        if source and target and source != 'Source Skill ID':
                            dep = Dependency(source, target, dep_type, strength)
                            self.dependencies.append(dep)
                            self.dependency_graph[source].append(target)
                            logger.info(f"Loaded dependency: {source} -> {target}")
                
                if in_dep_table and line.strip() and not line.startswith('|'):
                    in_dep_table = False
            
            logger.info(f"Total dependencies loaded: {len(self.dependencies)}")
            return len(self.dependencies)
            
        except Exception as e:
            logger.error(f"Error loading dependencies: {str(e)}")
            return 0
    
    def detect_circular_dependencies(self) -> List[List[str]]:
        """Detect circular dependencies using DFS."""
        circular_deps = []
        visited = set()
        rec_stack = set()
        
        def dfs(node: str, path: List[str]):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            for neighbor in self.dependency_graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path)
                elif neighbor in rec_stack:
                    # Found circular dependency
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    circular_deps.append(cycle)
            
            path.pop()
            rec_stack.remove(node)
        
        for skill in self.skills:
            if skill not in visited:
                dfs(skill, [])
        
        return circular_deps
    
    def check_missing_dependencies(self) -> List[DependencyIssue]:
        """Check for dependencies referencing non-existent Skills."""
        issues = []
        
        for dep in self.dependencies:
            if dep.source not in self.skills:
                issues.append(DependencyIssue(
                    issue_type="Missing Source Skill",
                    severity="ERROR",
                    message=f"Dependency source '{dep.source}' does not exist",
                    affected_skills=[dep.source, dep.target],
                    suggestion=f"Create Skill '{dep.source}' or remove dependency"
                ))
            
            if dep.target not in self.skills:
                issues.append(DependencyIssue(
                    issue_type="Missing Target Skill",
                    severity="ERROR",
                    message=f"Dependency target '{dep.target}' does not exist",
                    affected_skills=[dep.source, dep.target],
                    suggestion=f"Create Skill '{dep.target}' or remove dependency"
                ))
        
        return issues
    
    def check_orphaned_skills(self) -> List[DependencyIssue]:
        """Check for Skills with no dependencies (orphaned)."""
        issues = []
        
        # Skills that are not a source or target of any dependency
        referenced_skills = set()
        for dep in self.dependencies:
            referenced_skills.add(dep.source)
            referenced_skills.add(dep.target)
        
        orphaned = self.skills - referenced_skills
        
        for skill in orphaned:
            # Check if it's the root (intro-overview)
            if skill != "hkex-intro-overview":
                issues.append(DependencyIssue(
                    issue_type="Orphaned Skill",
                    severity="WARNING",
                    message=f"Skill '{skill}' has no dependencies",
                    affected_skills=[skill],
                    suggestion="Add dependencies or verify Skill is intentionally standalone"
                ))
        
        return issues
    
    def check_dependency_completeness(self) -> List[DependencyIssue]:
        """Check for incomplete dependency information."""
        issues = []
        
        for dep in self.dependencies:
            if not dep.dep_type:
                issues.append(DependencyIssue(
                    issue_type="Missing Dependency Type",
                    severity="WARNING",
                    message=f"Dependency {dep.source} -> {dep.target} has no type",
                    affected_skills=[dep.source, dep.target],
                    suggestion="Add dependency type (Direct, Indirect, Contextual)"
                ))
            
            if not dep.strength:
                issues.append(DependencyIssue(
                    issue_type="Missing Dependency Strength",
                    severity="WARNING",
                    message=f"Dependency {dep.source} -> {dep.target} has no strength",
                    affected_skills=[dep.source, dep.target],
                    suggestion="Add dependency strength (Strong, Medium, Weak)"
                ))
        
        return issues
    
    def validate_skill_dependencies(self, skill_id: str) -> ValidationResult:
        """Validate dependencies for a specific Skill."""
        result = ValidationResult(skill_id=skill_id)
        
        # Get dependencies for this Skill
        skill_deps = [d for d in self.dependencies if d.source == skill_id]
        result.dependencies = skill_deps
        
        # Check if dependencies are valid
        for dep in skill_deps:
            if dep.target not in self.skills:
                result.issues.append(DependencyIssue(
                    issue_type="Invalid Dependency Target",
                    severity="ERROR",
                    message=f"Dependency target '{dep.target}' does not exist",
                    affected_skills=[skill_id, dep.target],
                    suggestion=f"Remove or fix dependency to '{dep.target}'"
                ))
        
        result.is_valid = len(result.issues) == 0
        return result
    
    def validate_all_dependencies(self) -> int:
        """Validate all dependencies."""
        # Check for circular dependencies
        circular_deps = self.detect_circular_dependencies()
        if circular_deps:
            for cycle in circular_deps:
                issue = DependencyIssue(
                    issue_type="Circular Dependency",
                    severity="ERROR",
                    message=f"Circular dependency detected: {' -> '.join(cycle)}",
                    affected_skills=cycle[:-1],
                    suggestion="Break the circular dependency by removing one of the relationships"
                )
                # Add to all affected Skills
                for skill in cycle[:-1]:
                    existing_result = next((r for r in self.validation_results if r.skill_id == skill), None)
                    if existing_result:
                        existing_result.issues.append(issue)
                        existing_result.is_valid = False
                    else:
                        result = ValidationResult(skill_id=skill)
                        result.issues.append(issue)
                        result.is_valid = False
                        self.validation_results.append(result)
        
        # Check for missing dependencies
        missing_issues = self.check_missing_dependencies()
        for issue in missing_issues:
            for skill in issue.affected_skills:
                existing_result = next((r for r in self.validation_results if r.skill_id == skill), None)
                if existing_result:
                    existing_result.issues.append(issue)
                    existing_result.is_valid = False
                else:
                    result = ValidationResult(skill_id=skill)
                    result.issues.append(issue)
                    result.is_valid = False
                    self.validation_results.append(result)
        
        # Check for orphaned Skills
        orphaned_issues = self.check_orphaned_skills()
        for issue in orphaned_issues:
            for skill in issue.affected_skills:
                existing_result = next((r for r in self.validation_results if r.skill_id == skill), None)
                if existing_result:
                    existing_result.issues.append(issue)
                else:
                    result = ValidationResult(skill_id=skill)
                    result.issues.append(issue)
                    self.validation_results.append(result)
        
        # Check for incomplete dependencies
        incomplete_issues = self.check_dependency_completeness()
        for issue in incomplete_issues:
            for skill in issue.affected_skills:
                existing_result = next((r for r in self.validation_results if r.skill_id == skill), None)
                if existing_result:
                    existing_result.issues.append(issue)
                else:
                    result = ValidationResult(skill_id=skill)
                    result.issues.append(issue)
                    self.validation_results.append(result)
        
        # Validate each Skill's dependencies
        for skill_id in self.skills:
            existing_result = next((r for r in self.validation_results if r.skill_id == skill_id), None)
            if not existing_result:
                result = self.validate_skill_dependencies(skill_id)
                self.validation_results.append(result)
        
        logger.info(f"Total Skills validated: {len(self.validation_results)}")
        return len(self.validation_results)
    
    def generate_report(self) -> bool:
        """Generate dependency integrity report."""
        try:
            reports_dir = Path(CONFIG["reports_dir"])
            reports_dir.mkdir(parents=True, exist_ok=True)
            
            # Calculate summary
            total_valid = sum(1 for r in self.validation_results if r.is_valid)
            total_issues = sum(len(r.issues) for r in self.validation_results)
            circular_count = sum(1 for r in self.validation_results 
                               for i in r.issues if i.issue_type == "Circular Dependency")
            
            # Generate JSON report
            json_report = {
                "timestamp": datetime.now().isoformat(),
                "summary": {
                    "total_skills": len(self.validation_results),
                    "valid": total_valid,
                    "invalid": len(self.validation_results) - total_valid,
                    "total_issues": total_issues,
                    "circular_dependencies": circular_count,
                    "total_dependencies": len(self.dependencies)
                },
                "dependencies": [
                    {
                        "source": d.source,
                        "target": d.target,
                        "type": d.dep_type,
                        "strength": d.strength
                    }
                    for d in self.dependencies
                ],
                "results": [
                    {
                        "skill_id": r.skill_id,
                        "is_valid": r.is_valid,
                        "dependency_count": len(r.dependencies),
                        "issues": [
                            {
                                "type": i.issue_type,
                                "severity": i.severity,
                                "message": i.message,
                                "affected_skills": i.affected_skills,
                                "suggestion": i.suggestion
                            }
                            for i in r.issues
                        ]
                    }
                    for r in self.validation_results
                ]
            }
            
            json_path = reports_dir / "dependency-integrity-report.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_report, f, indent=2)
            logger.info(f"JSON report generated: {json_path}")
            
            # Generate Markdown report
            md_content = self._generate_markdown_report()
            md_path = reports_dir / "dependency-integrity-report.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            logger.info(f"Markdown report generated: {md_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            return False
    
    def _generate_markdown_report(self) -> str:
        """Generate Markdown dependency integrity report."""
        total_valid = sum(1 for r in self.validation_results if r.is_valid)
        total_issues = sum(len(r.issues) for r in self.validation_results)
        circular_count = sum(1 for r in self.validation_results 
                           for i in r.issues if i.issue_type == "Circular Dependency")
        
        content = f"""# Dependency Integrity Validation Report

## Overview

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Skills**: {len(self.validation_results)}  
**Total Dependencies**: {len(self.dependencies)}  
**Overall Status**: {"Pass" if total_valid == len(self.validation_results) and circular_count == 0 else "Issues Found"}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Skills | {len(self.validation_results)} |
| Valid | {total_valid} |
| Invalid | {len(self.validation_results) - total_valid} |
| Total Issues | {total_issues} |
| Circular Dependencies | {circular_count} |
| Total Dependencies | {len(self.dependencies)} |

---

## Dependency Graph

```mermaid
graph TD
"""
        
        # Add dependency edges
        for dep in self.dependencies[:20]:  # Limit to first 20 for readability
            content += f"    {dep.source}[{dep.source}] --> {dep.target}[{dep.target}]\n"
        
        if len(self.dependencies) > 20:
            content += f"    %% ... and {len(self.dependencies) - 20} more dependencies\n"
        
        content += """```

---

## Detailed Results

"""
        
        for result in self.validation_results:
            status_icon = "✓" if result.is_valid else "✗"
            content += f"""### {status_icon} {result.skill_id}

**Status**: {"Valid" if result.is_valid else "Invalid"}  
**Dependencies**: {len(result.dependencies)}  

"""
            
            if result.dependencies:
                content += "#### Dependencies\n\n"
                content += "| Target | Type | Strength |\n"
                content += "|--------|------|----------|\n"
                for dep in result.dependencies:
                    content += f"| {dep.target} | {dep.dep_type} | {dep.strength} |\n"
                content += "\n"
            
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
    logger.info("Dependency Integrity Validation Script")
    logger.info("=" * 60)
    
    try:
        # Initialize validator
        validator = DependencyIntegrityValidator()
        
        # Load Skills
        skill_count = validator.load_skills()
        if skill_count == 0:
            logger.error("No Skills found. Exiting.")
            return 1
        
        # Load dependencies
        dep_count = validator.load_dependencies()
        if dep_count == 0:
            logger.warning("No dependencies found. This may be the initial setup.")
        
        # Validate all dependencies
        validate_count = validator.validate_all_dependencies()
        
        # Generate report
        if validator.generate_report():
            logger.info("Validation completed successfully")
        else:
            logger.error("Failed to generate report")
            return 1
        
        # Return exit code based on results
        invalid_count = sum(1 for r in validator.validation_results if not r.is_valid)
        if invalid_count > 0:
            logger.warning(f"{invalid_count} Skills have dependency issues")
            return 2
        
        return 0
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
