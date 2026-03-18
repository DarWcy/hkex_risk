#!/usr/bin/env python3
"""
Rule Extractor Script
Parses MD files with structured IDs, extracts atomic rules, validates rule atomicity and uniqueness,
converts rules to JSON format, generates coverage reports, and supports incremental updates.
"""

import json
import re
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple
import hashlib


class RuleExtractor:
    """Main class for extracting and managing atomic rules from MD files."""
    
    def __init__(self, source_dir: str = "docs/source-files", 
                 output_dir: str = "docs/rules",
                 schema_file: str = "config/rule-schema.json"):
        """
        Initialize the RuleExtractor.
        
        Args:
            source_dir: Directory containing MD files with structured IDs
            output_dir: Directory for output JSON files
            schema_file: Path to JSON schema file
        """
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.schema_file = Path(schema_file)
        self.rules: List[Dict] = []
        self.rule_ids: Set[str] = set()
        self.coverage_data: Dict[str, Dict] = {}
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Load schema if it exists
        self.schema = self._load_schema()
    
    def _load_schema(self) -> Optional[Dict]:
        """Load the JSON schema for rule validation."""
        if self.schema_file.exists():
            with open(self.schema_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def parse_md_file(self, file_path: Path) -> List[Dict]:
        """
        Parse a single MD file and extract atomic rules.
        
        Args:
            file_path: Path to the MD file
            
        Returns:
            List of extracted rules
        """
        rules = []
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract structured IDs and their associated content
        pattern = r'([A-Z]{2,4}-[A-Z]{3,10}-\d{3})\s*\n\s*([^\n]+)'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            structured_id = match.group(1)
            heading = match.group(2).strip()
            
            # Extract atomic rules from this section
            atomic_rules = self._extract_atomic_rules(
                content, structured_id, heading, file_path
            )
            rules.extend(atomic_rules)
        
        return rules
    
    def _extract_atomic_rules(self, content: str, structured_id: str, 
                           heading: str, file_path: Path) -> List[Dict]:
        """
        Extract atomic rules from a section of the MD file.
        
        Args:
            content: Full content of the MD file
            structured_id: Structured ID of the section
            heading: Heading of the section
            file_path: Path to the MD file
            
        Returns:
            List of atomic rules
        """
        rules = []
        
        # Find the section content
        section_pattern = rf'{re.escape(structured_id)}\s*\n\s*{re.escape(heading)}(.*?)(?=\n[A-Z]{{2,4}}-[A-Z]{{3,10}}-\d{{3}}|\Z)'
        section_match = re.search(section_pattern, content, re.DOTALL)
        
        if not section_match:
            return rules
        
        section_content = section_match.group(1)
        
        # Extract domain from structured ID
        domain = structured_id.split('-')[0]
        
        # Generate atomic rule ID
        rule_id = f"RULE-{domain}-{len(self.rule_ids) + 1:03d}"
        
        # Extract rule statements (one per sentence or bullet point)
        rule_statements = self._extract_rule_statements(section_content)
        
        for i, statement in enumerate(rule_statements):
            rule = {
                "rule_id": f"{rule_id}-{i+1:02d}" if len(rule_statements) > 1 else rule_id,
                "domain": domain,
                "structured_id": structured_id,
                "statement": statement,
                "conditions": self._extract_conditions(section_content),
                "exceptions": self._extract_exceptions(section_content),
                "references": self._extract_references(section_content),
                "coverage": "covered",
                "source": str(file_path.relative_to(self.source_dir.parent)),
                "version": "v14",
                "created_at": datetime.now().isoformat() + "Z",
                "heading": heading
            }
            rules.append(rule)
            self.rule_ids.add(rule["rule_id"])
        
        return rules
    
    def _extract_rule_statements(self, content: str) -> List[str]:
        """
        Extract individual rule statements from content.
        
        Args:
            content: Section content
            
        Returns:
            List of rule statements
        """
        statements = []
        
        # Split by bullet points or numbered lists
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith(('-', '*', '•')) or re.match(r'^\d+\.', line):
                statement = re.sub(r'^[-*•]\s*|^\d+\.\s*', '', line).strip()
                if statement and len(statement) > 10:
                    statements.append(statement)
            elif line and not line.startswith('#') and len(line) > 20:
                # Treat as a rule statement if it's a substantial paragraph
                statements.append(line)
        
        return statements
    
    def _extract_conditions(self, content: str) -> List[str]:
        """
        Extract applicable conditions from content.
        
        Args:
            content: Section content
            
        Returns:
            List of conditions
        """
        conditions = []
        
        # Look for condition keywords
        condition_patterns = [
            r'when\s+(.+?)(?:\.|,)',
            r'if\s+(.+?)(?:\.|,)',
            r'provided\s+that\s+(.+?)(?:\.|,)',
            r'condition:\s*(.+?)(?:\.|,)',
            r'requirement:\s*(.+?)(?:\.|,)'
        ]
        
        for pattern in condition_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                condition = match.group(1).strip()
                if condition and len(condition) > 5:
                    conditions.append(condition)
        
        return conditions
    
    def _extract_exceptions(self, content: str) -> List[str]:
        """
        Extract exception cases from content.
        
        Args:
            content: Section content
            
        Returns:
            List of exceptions
        """
        exceptions = []
        
        # Look for exception keywords
        exception_patterns = [
            r'except\s+(.+?)(?:\.|,)',
            r'unless\s+(.+?)(?:\.|,)',
            r'exception:\s*(.+?)(?:\.|,)',
            r'exclusion:\s*(.+?)(?:\.|,)'
        ]
        
        for pattern in exception_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                exception = match.group(1).strip()
                if exception and len(exception) > 5:
                    exceptions.append(exception)
        
        return exceptions
    
    def _extract_references(self, content: str) -> List[str]:
        """
        Extract cross-references from content.
        
        Args:
            content: Section content
            
        Returns:
            List of references
        """
        references = []
        
        # Look for structured ID references
        ref_pattern = r'[A-Z]{2,4}-[A-Z]{3,10}-\d{3}'
        matches = re.findall(ref_pattern, content)
        references.extend(matches)
        
        return list(set(references))
    
    def validate_atomicity(self, rule: Dict) -> Tuple[bool, List[str]]:
        """
        Validate that a rule is atomic (represents a single requirement).
        
        Args:
            rule: Rule dictionary
            
        Returns:
            Tuple of (is_valid, issues)
        """
        issues = []
        
        # Check if statement is too long (might contain multiple requirements)
        if len(rule['statement']) > 500:
            issues.append("Rule statement is too long and may contain multiple requirements")
        
        # Check for conjunctions that might indicate multiple requirements
        conjunctions = [' and ', ' or ', ' as well as ', ' in addition to ']
        for conjunction in conjunctions:
            if conjunction.lower() in rule['statement'].lower():
                issues.append(f"Rule statement contains '{conjunction}' which may indicate multiple requirements")
        
        # Check for multiple sentences
        sentences = re.split(r'[.!?]', rule['statement'])
        if len([s for s in sentences if s.strip()]) > 2:
            issues.append("Rule statement contains multiple sentences and may not be atomic")
        
        return len(issues) == 0, issues
    
    def validate_uniqueness(self, rule: Dict, existing_rules: List[Dict]) -> Tuple[bool, List[str]]:
        """
        Validate that a rule is unique (no duplicates).
        
        Args:
            rule: Rule dictionary
            existing_rules: List of existing rules
            
        Returns:
            Tuple of (is_valid, issues)
        """
        issues = []
        
        # Check for duplicate rule IDs
        if rule['rule_id'] in self.rule_ids:
            issues.append(f"Rule ID '{rule['rule_id']}' already exists")
        
        # Check for duplicate statements
        for existing_rule in existing_rules:
            if existing_rule['rule_id'] == rule['rule_id']:
                continue
            
            # Calculate similarity
            similarity = self._calculate_similarity(
                rule['statement'], existing_rule['statement']
            )
            
            if similarity > 0.8:
                issues.append(
                    f"Rule statement is very similar to existing rule '{existing_rule['rule_id']}' "
                    f"(similarity: {similarity:.2f})"
                )
        
        return len(issues) == 0, issues
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate similarity between two texts using simple word overlap.
        
        Args:
            text1: First text
            text2: Second text
            
        Returns:
            Similarity score between 0 and 1
        """
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def validate_against_schema(self, rule: Dict) -> Tuple[bool, List[str]]:
        """
        Validate a rule against the JSON schema.
        
        Args:
            rule: Rule dictionary
            
        Returns:
            Tuple of (is_valid, issues)
        """
        issues = []
        
        if not self.schema:
            return True, []
        
        # Check required fields
        required_fields = [
            'rule_id', 'domain', 'statement', 'conditions', 
            'exceptions', 'references', 'coverage', 'source', 'version'
        ]
        
        for field in required_fields:
            if field not in rule:
                issues.append(f"Missing required field: {field}")
        
        # Validate field types
        if 'statement' in rule and not isinstance(rule['statement'], str):
            issues.append("Field 'statement' must be a string")
        
        if 'conditions' in rule and not isinstance(rule['conditions'], list):
            issues.append("Field 'conditions' must be a list")
        
        if 'exceptions' in rule and not isinstance(rule['exceptions'], list):
            issues.append("Field 'exceptions' must be a list")
        
        if 'references' in rule and not isinstance(rule['references'], list):
            issues.append("Field 'references' must be a list")
        
        return len(issues) == 0, issues
    
    def process_all_files(self) -> List[Dict]:
        """
        Process all MD files in the source directory.
        
        Returns:
            List of all extracted rules
        """
        md_files = list(self.source_dir.glob("*.md"))
        
        for md_file in md_files:
            print(f"Processing: {md_file.name}")
            rules = self.parse_md_file(md_file)
            self.rules.extend(rules)
            print(f"  Extracted {len(rules)} rules")
        
        return self.rules
    
    def validate_all_rules(self) -> Dict[str, List[Dict]]:
        """
        Validate all extracted rules.
        
        Returns:
            Dictionary with validation results
        """
        validation_results = {
            'valid': [],
            'invalid': [],
            'warnings': []
        }
        
        for rule in self.rules:
            issues = []
            
            # Validate atomicity
            is_atomic, atomicity_issues = self.validate_atomicity(rule)
            issues.extend(atomicity_issues)
            
            # Validate uniqueness
            is_unique, uniqueness_issues = self.validate_uniqueness(rule, self.rules)
            issues.extend(uniqueness_issues)
            
            # Validate against schema
            is_schema_valid, schema_issues = self.validate_against_schema(rule)
            issues.extend(schema_issues)
            
            # Categorize rule
            if len(issues) == 0:
                validation_results['valid'].append(rule)
            else:
                rule['validation_issues'] = issues
                validation_results['invalid'].append(rule)
        
        return validation_results
    
    def generate_coverage_report(self) -> Dict:
        """
        Generate a coverage report for all rules.
        
        Returns:
            Coverage report dictionary
        """
        total_rules = len(self.rules)
        covered_rules = sum(1 for rule in self.rules if rule['coverage'] == 'covered')
        
        # Group rules by domain
        domain_coverage = {}
        for rule in self.rules:
            domain = rule['domain']
            if domain not in domain_coverage:
                domain_coverage[domain] = {'total': 0, 'covered': 0}
            domain_coverage[domain]['total'] += 1
            if rule['coverage'] == 'covered':
                domain_coverage[domain]['covered'] += 1
        
        coverage_report = {
            'total_rules': total_rules,
            'covered_rules': covered_rules,
            'coverage_percentage': (covered_rules / total_rules * 100) if total_rules > 0 else 0,
            'domain_coverage': domain_coverage,
            'generated_at': datetime.now().isoformat() + "Z"
        }
        
        return coverage_report
    
    def save_to_json(self, output_file: str = "atomic-rules.json") -> None:
        """
        Save all rules to a JSON file.
        
        Args:
            output_file: Name of the output file
        """
        output_path = self.output_dir / output_file
        
        # Generate metadata
        metadata = {
            'total_rules': len(self.rules),
            'covered_rules': sum(1 for rule in self.rules if rule['coverage'] == 'covered'),
            'version': 'v14',
            'generated_at': datetime.now().isoformat() + "Z",
            'source_directory': str(self.source_dir),
            'schema_version': '1.0' if self.schema else None
        }
        
        # Create output structure
        output = {
            'rules': self.rules,
            'metadata': metadata,
            'coverage_report': self.generate_coverage_report()
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(self.rules)} rules to {output_path}")
    
    def load_existing_rules(self, input_file: str = "atomic-rules.json") -> List[Dict]:
        """
        Load existing rules from a JSON file for incremental updates.
        
        Args:
            input_file: Name of the input file
            
        Returns:
            List of existing rules
        """
        input_path = self.output_dir / input_file
        
        if not input_path.exists():
            return []
        
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        existing_rules = data.get('rules', [])
        
        # Load existing rule IDs
        for rule in existing_rules:
            self.rule_ids.add(rule['rule_id'])
        
        print(f"Loaded {len(existing_rules)} existing rules from {input_path}")
        return existing_rules
    
    def incremental_update(self, existing_rules: List[Dict]) -> Dict:
        """
        Perform incremental update by comparing new rules with existing rules.
        
        Args:
            existing_rules: List of existing rules
            
        Returns:
            Dictionary with update results
        """
        update_results = {
            'added': [],
            'modified': [],
            'deleted': [],
            'unchanged': []
        }
        
        # Create a mapping of existing rules by ID
        existing_rules_map = {rule['rule_id']: rule for rule in existing_rules}
        
        # Check for new and modified rules
        for new_rule in self.rules:
            rule_id = new_rule['rule_id']
            
            if rule_id not in existing_rules_map:
                # New rule
                update_results['added'].append(new_rule)
            else:
                # Check if modified
                existing_rule = existing_rules_map[rule_id]
                if self._is_rule_modified(new_rule, existing_rule):
                    update_results['modified'].append(new_rule)
                else:
                    update_results['unchanged'].append(new_rule)
        
        # Check for deleted rules
        existing_rule_ids = set(existing_rules_map.keys())
        new_rule_ids = set(rule['rule_id'] for rule in self.rules)
        deleted_rule_ids = existing_rule_ids - new_rule_ids
        
        for rule_id in deleted_rule_ids:
            update_results['deleted'].append(existing_rules_map[rule_id])
        
        return update_results
    
    def _is_rule_modified(self, rule1: Dict, rule2: Dict) -> bool:
        """
        Check if two rules are different.
        
        Args:
            rule1: First rule
            rule2: Second rule
            
        Returns:
            True if rules are different, False otherwise
        """
        # Compare key fields
        key_fields = ['statement', 'conditions', 'exceptions', 'references']
        
        for field in key_fields:
            if rule1.get(field) != rule2.get(field):
                return True
        
        return False
    
    def generate_reverification_report(self, old_rules: List[Dict], 
                                    new_rules: List[Dict]) -> Dict:
        """
        Generate a re-verification report comparing old and new rules.
        
        Args:
            old_rules: List of old rules
            new_rules: List of new rules
            
        Returns:
            Re-verification report dictionary
        """
        report = {
            'summary': {
                'total_old_rules': len(old_rules),
                'total_new_rules': len(new_rules),
                'added_rules': 0,
                'modified_rules': 0,
                'deleted_rules': 0,
                'unchanged_rules': 0
            },
            'added_rules': [],
            'modified_rules': [],
            'deleted_rules': [],
            'unchanged_rules': [],
            'validation_results': {},
            'generated_at': datetime.now().isoformat() + "Z"
        }
        
        # Create mappings
        old_rules_map = {rule['rule_id']: rule for rule in old_rules}
        new_rules_map = {rule['rule_id']: rule for rule in new_rules}
        
        # Compare rules
        all_rule_ids = set(old_rules_map.keys()) | set(new_rules_map.keys())
        
        for rule_id in all_rule_ids:
            if rule_id in new_rules_map and rule_id not in old_rules_map:
                # Added rule
                report['added_rules'].append(new_rules_map[rule_id])
                report['summary']['added_rules'] += 1
            elif rule_id in old_rules_map and rule_id not in new_rules_map:
                # Deleted rule
                report['deleted_rules'].append(old_rules_map[rule_id])
                report['summary']['deleted_rules'] += 1
            elif rule_id in old_rules_map and rule_id in new_rules_map:
                # Check if modified
                if self._is_rule_modified(new_rules_map[rule_id], old_rules_map[rule_id]):
                    report['modified_rules'].append({
                        'rule_id': rule_id,
                        'old': old_rules_map[rule_id],
                        'new': new_rules_map[rule_id]
                    })
                    report['summary']['modified_rules'] += 1
                else:
                    report['unchanged_rules'].append(new_rules_map[rule_id])
                    report['summary']['unchanged_rules'] += 1
        
        # Validate new rules
        validation_results = self.validate_all_rules()
        report['validation_results'] = {
            'valid_count': len(validation_results['valid']),
            'invalid_count': len(validation_results['invalid']),
            'invalid_rules': [
                {'rule_id': rule['rule_id'], 'issues': rule['validation_issues']}
                for rule in validation_results['invalid']
            ]
        }
        
        return report


def main():
    """Main function to run the rule extractor."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Extract atomic rules from MD files and convert to JSON format"
    )
    parser.add_argument(
        '--source-dir', 
        default='docs/source-files',
        help='Directory containing MD files with structured IDs'
    )
    parser.add_argument(
        '--output-dir',
        default='docs/rules',
        help='Directory for output JSON files'
    )
    parser.add_argument(
        '--schema-file',
        default='config/rule-schema.json',
        help='Path to JSON schema file'
    )
    parser.add_argument(
        '--output-file',
        default='atomic-rules.json',
        help='Name of the output JSON file'
    )
    parser.add_argument(
        '--incremental',
        action='store_true',
        help='Perform incremental update using existing rules'
    )
    parser.add_argument(
        '--reverify',
        action='store_true',
        help='Generate re-verification report comparing old and new rules'
    )
    
    args = parser.parse_args()
    
    # Initialize extractor
    extractor = RuleExtractor(
        source_dir=args.source_dir,
        output_dir=args.output_dir,
        schema_file=args.schema_file
    )
    
    # Process all MD files
    print("Processing MD files...")
    extractor.process_all_files()
    print(f"Total rules extracted: {len(extractor.rules)}")
    
    # Validate all rules
    print("\nValidating rules...")
    validation_results = extractor.validate_all_rules()
    print(f"Valid rules: {len(validation_results['valid'])}")
    print(f"Invalid rules: {len(validation_results['invalid'])}")
    
    # Print invalid rule details
    for rule in validation_results['invalid']:
        print(f"\nInvalid rule: {rule['rule_id']}")
        for issue in rule['validation_issues']:
            print(f"  - {issue}")
    
    # Generate coverage report
    print("\nGenerating coverage report...")
    coverage_report = extractor.generate_coverage_report()
    print(f"Total rules: {coverage_report['total_rules']}")
    print(f"Covered rules: {coverage_report['covered_rules']}")
    print(f"Coverage percentage: {coverage_report['coverage_percentage']:.2f}%")
    
    # Handle incremental update
    if args.incremental:
        print("\nLoading existing rules for incremental update...")
        existing_rules = extractor.load_existing_rules(args.output_file)
        
        print("\nPerforming incremental update...")
        update_results = extractor.incremental_update(existing_rules)
        print(f"Added rules: {len(update_results['added'])}")
        print(f"Modified rules: {len(update_results['modified'])}")
        print(f"Deleted rules: {len(update_results['deleted'])}")
        print(f"Unchanged rules: {len(update_results['unchanged'])}")
    
    # Handle re-verification
    if args.reverify:
        print("\nLoading existing rules for re-verification...")
        existing_rules = extractor.load_existing_rules(args.output_file)
        
        print("\nGenerating re-verification report...")
        reverify_report = extractor.generate_reverification_report(
            existing_rules, extractor.rules
        )
        
        # Save re-verification report
        report_path = extractor.output_dir / f"reverification-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(reverify_report, f, indent=2, ensure_ascii=False)
        print(f"Re-verification report saved to: {report_path}")
        
        # Print summary
        print(f"\nRe-verification Summary:")
        print(f"  Old rules: {reverify_report['summary']['total_old_rules']}")
        print(f"  New rules: {reverify_report['summary']['total_new_rules']}")
        print(f"  Added: {reverify_report['summary']['added_rules']}")
        print(f"  Modified: {reverify_report['summary']['modified_rules']}")
        print(f"  Deleted: {reverify_report['summary']['deleted_rules']}")
        print(f"  Unchanged: {reverify_report['summary']['unchanged_rules']}")
    
    # Save to JSON
    print(f"\nSaving rules to JSON...")
    extractor.save_to_json(args.output_file)
    
    print("\nDone!")


if __name__ == "__main__":
    main()