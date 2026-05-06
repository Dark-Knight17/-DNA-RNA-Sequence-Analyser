import re
from typing import List, Dict

def parse_fasta(content: str) -> List[Dict[str, str]]:
    """
    Parses FASTA format string content.
    Returns a list of dictionaries with 'header' and 'sequence'.
    """
    results = []
    # Split by '>' and filter out empty strings
    entries = content.split('>')
    for entry in entries:
        if not entry.strip():
            continue
            
        lines = entry.strip().splitlines()
        if not lines:
            continue
            
        header = lines[0]
        # Join the rest of the lines and remove any whitespace/newlines
        sequence = "".join(line.strip() for line in lines[1:])
        results.append({
            "header": header,
            "sequence": sequence
        })
        
    return results

def is_fasta(content: str) -> bool:
    """
    Quick check if the content appears to be in FASTA format.
    """
    return content.strip().startswith('>')
