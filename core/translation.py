from typing import List, Dict, Tuple
from core.codon_table import CODON_TABLE

def translate(mrna: str) -> Tuple[List[Dict[str, str]], str]:
    """
    Translates an mRNA sequence into a list of codons and their corresponding amino acids.
    Detects start and stop codons.
    
    Args:
        mrna (str): The mRNA sequence.
        
    Returns:
        Tuple[List[Dict[str, str]], str]: (List of mapped codons, explanation)
    """
    codons = []
    
    # Read sequence in chunks of 3
    for i in range(0, len(mrna), 3):
        codon_seq = mrna[i:i+3]
        if len(codon_seq) < 3:
            codons.append({
                "codon": codon_seq,
                "name": "Incomplete",
                "abbreviation": "Inc"
            })
            continue
            
        amino_acid_info = CODON_TABLE.get(codon_seq, ("Unknown", "Unk"))
        codons.append({
            "codon": codon_seq,
            "name": amino_acid_info[0],
            "abbreviation": amino_acid_info[1]
        })
        
    explanation = "During translation, the ribosome reads the mRNA sequence three letters at a time. Each three-letter group is called a codon, which corresponds to a specific amino acid. The sequence of amino acids folds to become a functional protein."
    
    return codons, explanation
