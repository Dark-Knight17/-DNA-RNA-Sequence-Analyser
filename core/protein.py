from typing import List, Dict, Tuple
from collections import Counter

AMINO_ACID_PROPERTIES = {
    'Ala': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Arg': {'polarity': 'Polar', 'charge': 'Positive'},
    'Asn': {'polarity': 'Polar', 'charge': 'Neutral'},
    'Asp': {'polarity': 'Polar', 'charge': 'Negative'},
    'Cys': {'polarity': 'Nonpolar', 'charge': 'Neutral'}, # Often considered nonpolar or slightly polar
    'Gln': {'polarity': 'Polar', 'charge': 'Neutral'},
    'Glu': {'polarity': 'Polar', 'charge': 'Negative'},
    'Gly': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'His': {'polarity': 'Polar', 'charge': 'Positive'},
    'Ile': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Leu': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Lys': {'polarity': 'Polar', 'charge': 'Positive'},
    'Met': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Phe': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Pro': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Ser': {'polarity': 'Polar', 'charge': 'Neutral'},
    'Thr': {'polarity': 'Polar', 'charge': 'Neutral'},
    'Trp': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
    'Tyr': {'polarity': 'Polar', 'charge': 'Neutral'},
    'Val': {'polarity': 'Nonpolar', 'charge': 'Neutral'},
}

def analyze_protein(codons: List[Dict[str, str]]) -> Tuple[Dict, str]:
    """
    Analyzes the translated codons to build the polypeptide chain and characterize the protein.
    Translation effectively stops at the first STOP codon.
    
    Args:
        codons: List of codon dictionaries containing 'name' and 'abbreviation'.
        
    Returns:
        Tuple containing a dictionary of analysis results and a biological explanation.
    """
    peptide_chain = []
    
    for codon in codons:
        if codon['abbreviation'] == 'STOP':
            break
        if codon['abbreviation'] not in ('Unk', 'Inc'):
            peptide_chain.append(codon)
            
    abbreviations = [aa['abbreviation'] for aa in peptide_chain]
    protein_sequence = "".join([aa[0] for aa in abbreviations if len(aa) > 0]) # Crude 1-letter approx? Actually we need 1-letter mapping for real sequence.
    
    # Precise 1-letter codes
    ONE_LETTER = {
        'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D', 'Cys': 'C', 'Gln': 'Q',
        'Glu': 'E', 'Gly': 'G', 'His': 'H', 'Ile': 'I', 'Leu': 'L', 'Lys': 'K',
        'Met': 'M', 'Phe': 'F', 'Pro': 'P', 'Ser': 'S', 'Thr': 'T', 'Trp': 'W',
        'Tyr': 'Y', 'Val': 'V'
    }
    
    protein_string = "".join(ONE_LETTER.get(aa, '?') for aa in abbreviations)
    length = len(abbreviations)
    
    # Frequencies
    freq = dict(Counter(abbreviations))
    
    # Characterization
    polar_count = 0
    nonpolar_count = 0
    
    for aa in abbreviations:
        prop = AMINO_ACID_PROPERTIES.get(aa)
        if prop:
            if prop['polarity'] == 'Polar':
                polar_count += 1
            elif prop['polarity'] == 'Nonpolar':
                nonpolar_count += 1
                
    hydrophobicity_overview = {
        "hydrophilic_polar": polar_count,
        "hydrophobic_nonpolar": nonpolar_count
    }
    
    analysis = {
        "peptide_chain": peptide_chain,
        "sequence_1_letter": protein_string,
        "length": length,
        "amino_acid_frequency": freq,
        "composition": hydrophobicity_overview
    }
    
    explanation = (
        "Amino acids are the building blocks of proteins. They link together to form a polypeptide chain. "
        "The properties of these amino acids (such as being polar or non-polar) determine how the chain folds into a functional 3D protein structure. "
        "Translation halts when a STOP codon is reached."
    )
    
    return analysis, explanation
