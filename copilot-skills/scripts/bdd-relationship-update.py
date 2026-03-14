#!/usr/bin/env python3
"""
BDD Relationship Update Script

This script triggers BDD scenario and Skill relationship updates,
and updates the tests/bdd-relation-manager.md file.

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

# Configuration
CONFIG = {
    "skills_dir": "../skill-definitions",
    "bdd_features_dir": "../../tests/bdd/features",
    "relation_manager_file": "../../tests/bdd-relation-manager.md",
    "backup_dir": "../../governance/backups",
    "log_file": "../../governance/logs/bdd-relationship-update.log"
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


class BDDScenario:
    """Represents a BDD scenario."""
    
    def __init__(self, feature_id: str, scenario_id: str, description: str, 
                 skill_id: str, rule_source: str):
        self.feature_id = feature_id
        self.scenario_id = scenario_id
        self.description = description
        self.skill_id = skill_id
        self.rule_source = rule_source
        self.association_status = "Pending"
        
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "feature_id": self.feature_id,
            "scenario_id": self.scenario_id,
            "description": self.description,
            "skill_id": self.skill_id,
            "rule_source": self.rule_source,
            "association_status": self.association_status
        }


class BDDRelationManager:
    """Manages BDD and Skill relationship updates."""
    
    def __init__(self):
        self.skills: Dict[str, Dict] = {}
        self.bdd_scenarios: List[BDDScenario] = []
        self.associations: List[Dict] = []
        
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
                    
                    # Extract BDD association
                    bdd_match = re.search(
                        r'## BDD Association Pre-embedding\s*\n\s*([^\n]+)', 
                        content
                    )
                    bdd_info = bdd_match.group(1).strip() if bdd_match else "to be associated"
                    
                    self.skills[skill_id] = {
                        "file": str(skill_file),
                        "bdd_info": bdd_info
                    }
                    count += 1
                    logger.info(f"Loaded Skill: {skill_id}")
                    
            except Exception as e:
                logger.error(f"Error loading {skill_file}: {str(e)}")
        
        logger.info(f"Total Skills loaded: {count}")
        return count
    
    def scan_bdd_features(self) -> int:
        """Scan BDD feature files for scenarios."""
        features_path = Path(CONFIG["bdd_features_dir"])
        if not features_path.exists():
            logger.warning(f"BDD features directory not found: {CONFIG['bdd_features_dir']}")
            logger.info("Creating directory structure...")
            features_path.mkdir(parents=True, exist_ok=True)
            return 0
        
        count = 0
        for feature_file in features_path.glob("*.feature"):
            try:
                with open(feature_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract feature ID
                feature_match = re.search(r'Feature:\s*(\S+)\s*-\s*(.+)', content)
                if feature_match:
                    feature_id = feature_match.group(1).strip()
                    feature_desc = feature_match.group(2).strip()
                    
                    # Extract scenarios
                    scenarios = re.findall(
                        r'Scenario:\s*(\S+)\s*-\s*(.+?)(?=Scenario:|Feature:|$)',
                        content,
                        re.DOTALL
                    )
                    
                    for scenario_id, scenario_content in scenarios:
                        # Look for Skill reference in tags or content
                        skill_match = re.search(r'@(\S+)', scenario_content)
                        skill_id = skill_match.group(1) if skill_match else "unknown"
                        
                        # Look for Rule_Source reference
                        rule_match = re.search(r'Rule_Source:\s*(.+)', scenario_content)
                        rule_source = rule_match.group(1).strip() if rule_match else "to be defined"
                        
                        scenario = BDDScenario(
                            feature_id=feature_id,
                            scenario_id=scenario_id.strip(),
                            description=scenario_content.strip()[:100],
                            skill_id=skill_id,
                            rule_source=rule_source
                        )
                        
                        self.bdd_scenarios.append(scenario)
                        count += 1
                        
            except Exception as e:
                logger.error(f"Error scanning {feature_file}: {str(e)}")
        
        logger.info(f"Total BDD scenarios found: {count}")
        return count
    
    def create_default_scenarios(self) -> int:
        """Create default BDD scenarios for Skills without associations."""
        count = 0
        
        for skill_id, skill_data in self.skills.items():
            if "to be associated" in skill_data["bdd_info"].lower():
                # Create default scenario
                scenario = BDDScenario(
                    feature_id=f"FT-{skill_id.replace('hkex-', '').upper()}",
                    scenario_id=f"TC-{skill_id.replace('hkex-', '').upper()}-001",
                    description=f"Default scenario for {skill_id}",
                    skill_id=skill_id,
                    rule_source="to be defined"
                )
                self.bdd_scenarios.append(scenario)
                count += 1
                logger.info(f"Created default scenario for: {skill_id}")
        
        logger.info(f"Default scenarios created: {count}")
        return count
    
    def associate_scenarios_with_skills(self) -> int:
        """Associate BDD scenarios with Skills."""
        count = 0
        
        for scenario in self.bdd_scenarios:
            if scenario.skill_id in self.skills:
                scenario.association_status = "Associated"
                self.associations.append({
                    "skill_id": scenario.skill_id,
                    "scenario_id": scenario.scenario_id,
                    "feature_id": scenario.feature_id,
                    "status": "Associated",
                    "timestamp": datetime.now().isoformat()
                })
                count += 1
                logger.info(f"Associated {scenario.scenario_id} with {scenario.skill_id}")
            else:
                scenario.association_status = "Orphaned"
                logger.warning(f"Orphaned scenario: {scenario.scenario_id}")
        
        logger.info(f"Total associations created: {count}")
        return count
    
    def update_relation_manager(self) -> bool:
        """Update the BDD relation manager file."""
        try:
            manager_path = Path(CONFIG["relation_manager_file"])
            
            # Create content
            content = self._generate_manager_content()
            
            # Create backup if file exists
            if manager_path.exists():
                backup_dir = Path(CONFIG["backup_dir"])
                backup_dir.mkdir(parents=True, exist_ok=True)
                backup_file = backup_dir / f"bdd-relation-manager-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
                
                with open(manager_path, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                
                with open(backup_file, 'w', encoding='utf-8') as f:
                    f.write(existing_content)
                logger.info(f"Backup created: {backup_file}")
            
            # Write new content
            manager_path.parent.mkdir(parents=True, exist_ok=True)
            with open(manager_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Relation manager updated: {manager_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error updating relation manager: {str(e)}")
            return False
    
    def _generate_manager_content(self) -> str:
        """Generate the BDD relation manager content."""
        content = f"""# BDD Relationship Manager

## Overview

This file manages the relationships between BDD scenarios and Copilot Skills.

**Version**: 1.4  
**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Responsible**: System  

---

## Association Summary

- **Total Skills**: {len(self.skills)}
- **Total BDD Scenarios**: {len(self.bdd_scenarios)}
- **Associated**: {len([a for a in self.associations if a['status'] == 'Associated'])}
- **Pending**: {len([a for a in self.associations if a['status'] == 'Pending'])}
- **Orphaned**: {len([s for s in self.bdd_scenarios if s.association_status == 'Orphaned'])}

---

## Association Table

| Skill ID | Scenario ID | Feature ID | Status | Last Updated |
|----------|-------------|------------|--------|--------------|
"""
        
        for assoc in self.associations:
            content += f"| {assoc['skill_id']} | {assoc['scenario_id']} | {assoc['feature_id']} | {assoc['status']} | {assoc['timestamp'][:10]} |\n"
        
        content += f"""
---

## BDD Scenarios Detail

"""
        
        for scenario in self.bdd_scenarios:
            content += f"""### {scenario.scenario_id}

- **Feature ID**: {scenario.feature_id}
- **Description**: {scenario.description}
- **Skill ID**: {scenario.skill_id}
- **Rule Source**: {scenario.rule_source}
- **Status**: {scenario.association_status}

"""
        
        content += f"""---

## Update Procedures

### Adding New Association

1. Create BDD scenario in feature file
2. Tag with Skill ID: `@{skill_id}`
3. Run this script to update associations
4. Verify in Association Table

### Modifying Association

1. Update scenario in feature file
2. Re-run this script
3. Verify changes in Association Table

### Removing Association

1. Remove tag from scenario
2. Re-run this script
3. Association will be marked as "Deprecated"

---

## Change History

| Version | Date | Changes | Updater |
|---------|------|---------|---------|
| 1.0 | {datetime.now().strftime('%Y-%m-%d')} | Initial creation | System |

---

*This file is automatically updated by the BDD Relationship Update Script.*
"""
        
        return content
    
    def generate_report(self) -> Dict:
        """Generate update report."""
        return {
            "timestamp": datetime.now().isoformat(),
            "total_skills": len(self.skills),
            "total_scenarios": len(self.bdd_scenarios),
            "associations": len(self.associations),
            "status": "success"
        }


def main():
    """Main execution function."""
    logger.info("=" * 60)
    logger.info("BDD Relationship Update Script")
    logger.info("=" * 60)
    
    try:
        # Initialize manager
        manager = BDDRelationManager()
        
        # Load Skills
        skill_count = manager.load_skills()
        if skill_count == 0:
            logger.error("No Skills found. Exiting.")
            return 1
        
        # Scan BDD features
        scenario_count = manager.scan_bdd_features()
        
        # Create default scenarios if needed
        if scenario_count == 0:
            logger.info("No existing BDD scenarios found. Creating defaults...")
            manager.create_default_scenarios()
        
        # Associate scenarios with Skills
        assoc_count = manager.associate_scenarios_with_skills()
        
        # Update relation manager
        if manager.update_relation_manager():
            logger.info("BDD relationship update completed successfully")
        else:
            logger.error("Failed to update relation manager")
            return 1
        
        # Generate report
        report = manager.generate_report()
        logger.info(f"Update report: {json.dumps(report, indent=2)}")
        
        return 0
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
