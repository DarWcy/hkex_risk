#!/usr/bin/env python3
"""
Skill Reference Synchronization Script

This script automatically synchronizes Skill and MD file Reference relationships,
and updates the skill-bdd-relation.md file.

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
from typing import Dict, List, Tuple, Optional

# Configuration
CONFIG = {
    "skills_dir": "../skill-definitions",
    "docs_dir": "../../docs",
    "relation_file": "../../tests/skill-bdd-relation.md",
    "backup_dir": "../../governance/backups",
    "log_file": "../../governance/logs/skill-reference-sync.log"
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


class SkillReference:
    """Represents a Skill's structured reference."""
    
    def __init__(self, skill_id: str, rule_source: str, test_ref: str, 
                 verify_ref: str, update_history: str):
        self.skill_id = skill_id
        self.rule_source = rule_source
        self.test_reference = test_ref
        self.verify_reference = verify_ref
        self.update_history = update_history
        self.integrity_status = "Pending"
        
    def validate(self) -> bool:
        """Validate the reference integrity."""
        # Check if rule source file exists
        if self.rule_source and "to be" not in self.rule_source.lower():
            parts = self.rule_source.split("|")
            if len(parts) >= 1:
                file_path = parts[0].strip()
                full_path = os.path.join(CONFIG["docs_dir"], os.path.basename(file_path))
                if not os.path.exists(full_path):
                    logger.warning(f"Rule source file not found: {full_path}")
                    self.integrity_status = "Invalid"
                    return False
        
        self.integrity_status = "Valid"
        return True


class ReferenceSynchronizer:
    """Synchronizes Skill references with the relationship table."""
    
    def __init__(self):
        self.skills: Dict[str, SkillReference] = {}
        self.changes: List[Dict] = []
        
    def parse_skill_file(self, file_path: str) -> Optional[SkillReference]:
        """Parse a Skill file and extract structured reference."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract Skill ID
            skill_id_match = re.search(r'## Skill ID\s*\n\s*(\S+)', content)
            if not skill_id_match:
                logger.error(f"Skill ID not found in {file_path}")
                return None
            skill_id = skill_id_match.group(1).strip()
            
            # Extract Rule_Source
            rule_source_match = re.search(
                r'### Rule_Source\s*\n\s*([^\n]+)', content
            )
            rule_source = rule_source_match.group(1).strip() if rule_source_match else "to be associated"
            
            # Extract Test_Reference
            test_ref_match = re.search(
                r'### Test_Reference\s*\n\s*([^\n]+)', content
            )
            test_ref = test_ref_match.group(1).strip() if test_ref_match else "to be associated"
            
            # Extract Verify_Reference
            verify_ref_match = re.search(
                r'### Verify_Reference\s*\n\s*([^\n]+)', content
            )
            verify_ref = verify_ref_match.group(1).strip() if verify_ref_match else "to be defined"
            
            # Extract Update_History
            update_hist_match = re.search(
                r'### Update_History\s*\n\s*([^\n]+)', content
            )
            update_hist = update_hist_match.group(1).strip() if update_hist_match else "N/A"
            
            return SkillReference(skill_id, rule_source, test_ref, verify_ref, update_hist)
            
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {str(e)}")
            return None
    
    def load_all_skills(self) -> int:
        """Load all Skill files from the skills directory."""
        skills_path = Path(CONFIG["skills_dir"])
        if not skills_path.exists():
            logger.error(f"Skills directory not found: {CONFIG['skills_dir']}")
            return 0
        
        count = 0
        for skill_file in skills_path.glob("*.md"):
            skill_ref = self.parse_skill_file(str(skill_file))
            if skill_ref:
                self.skills[skill_ref.skill_id] = skill_ref
                count += 1
                logger.info(f"Loaded Skill: {skill_ref.skill_id}")
        
        logger.info(f"Total Skills loaded: {count}")
        return count
    
    def validate_references(self) -> Tuple[int, int]:
        """Validate all Skill references."""
        valid_count = 0
        invalid_count = 0
        
        for skill_id, skill_ref in self.skills.items():
            if skill_ref.validate():
                valid_count += 1
            else:
                invalid_count += 1
                logger.warning(f"Invalid reference for Skill: {skill_id}")
        
        logger.info(f"Validation complete: {valid_count} valid, {invalid_count} invalid")
        return valid_count, invalid_count
    
    def update_relation_file(self) -> bool:
        """Update the skill-bdd-relation.md file with current references."""
        try:
            relation_path = Path(CONFIG["relation_file"])
            if not relation_path.exists():
                logger.error(f"Relation file not found: {CONFIG['relation_file']}")
                return False
            
            # Read existing content
            with open(relation_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create backup
            backup_dir = Path(CONFIG["backup_dir"])
            backup_dir.mkdir(parents=True, exist_ok=True)
            backup_file = backup_dir / f"skill-bdd-relation-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Backup created: {backup_file}")
            
            # Update relationship table
            updated_content = self._update_relationship_table(content)
            
            # Write updated content
            with open(relation_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            logger.info(f"Relation file updated: {relation_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error updating relation file: {str(e)}")
            return False
    
    def _update_relationship_table(self, content: str) -> str:
        """Update the relationship table in the content."""
        # Find and update the relationship table
        lines = content.split('\n')
        updated_lines = []
        in_table = False
        table_header_found = False
        
        for line in lines:
            # Detect table header
            if '| Skill ID |' in line and 'Rule_Source' in line:
                in_table = True
                table_header_found = True
                updated_lines.append(line)
                continue
            
            # Skip separator line
            if in_table and '|' in line and '---' in line:
                updated_lines.append(line)
                continue
            
            # Update table rows
            if in_table and '|' in line and not line.strip().startswith('#'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 2:
                    skill_id = parts[1].strip()
                    if skill_id in self.skills:
                        skill_ref = self.skills[skill_id]
                        # Update the row with current data
                        new_row = self._create_table_row(skill_ref)
                        updated_lines.append(new_row)
                        self.changes.append({
                            "skill_id": skill_id,
                            "action": "updated",
                            "timestamp": datetime.now().isoformat()
                        })
                        continue
            
            # End of table
            if in_table and table_header_found and line.strip() and not line.startswith('|'):
                in_table = False
            
            updated_lines.append(line)
        
        return '\n'.join(updated_lines)
    
    def _create_table_row(self, skill_ref: SkillReference) -> str:
        """Create a table row for a Skill reference."""
        return f"| {skill_ref.skill_id} | {skill_ref.rule_source} | {skill_ref.test_reference} | TC-XXX-001 | tests/bdd/features/{skill_ref.skill_id}.feature | {skill_ref.integrity_status} | {datetime.now().strftime('%Y-%m-%d')} | System |"
    
    def generate_report(self) -> Dict:
        """Generate synchronization report."""
        return {
            "timestamp": datetime.now().isoformat(),
            "total_skills": len(self.skills),
            "changes": self.changes,
            "status": "success" if not any(s.integrity_status == "Invalid" for s in self.skills.values()) else "partial"
        }


def main():
    """Main execution function."""
    logger.info("=" * 60)
    logger.info("Skill Reference Synchronization Script")
    logger.info("=" * 60)
    
    try:
        # Initialize synchronizer
        sync = ReferenceSynchronizer()
        
        # Load all Skills
        skill_count = sync.load_all_skills()
        if skill_count == 0:
            logger.error("No Skills found. Exiting.")
            return 1
        
        # Validate references
        valid, invalid = sync.validate_references()
        
        # Update relation file
        if sync.update_relation_file():
            logger.info("Synchronization completed successfully")
        else:
            logger.error("Failed to update relation file")
            return 1
        
        # Generate report
        report = sync.generate_report()
        logger.info(f"Synchronization report: {json.dumps(report, indent=2)}")
        
        return 0 if invalid == 0 else 2
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
