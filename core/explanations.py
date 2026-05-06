def get_general_explanations() -> dict:
    """
    Returns general explanations for each biological step.
    """
    return {
        "detection": {
            "title": "Sequence Type Detection",
            "process": "The system analyzes the chemical composition of your sequence. DNA uses Thymine (T), while RNA uses Uracil (U). Both share Adenine (A), Cytosine (C), and Guanine (G)."
        },
        "transcription": {
            "title": "Transcription",
            "process": "Transcription is the process where a DNA segment is copied into RNA (mRNA) by the enzyme RNA polymerase. This mRNA then carries the genetic information out of the cell nucleus to the ribosome for protein synthesis."
        },
        "translation": {
            "title": "Translation",
            "process": "Translation is the process where ribosomes synthesize proteins using the genetic information carried by mRNA. The ribosome reads the mRNA in triplets called 'codons', each matching a specific amino acid."
        },
        "amino_acids": {
            "title": "Amino Acids & Polypeptides",
            "process": "Amino acids are organic compounds that combine to form proteins. A long chain of amino acids is called a polypeptide. The specific order of these amino acids determines the protein's final shape and function."
        },
        "protein": {
            "title": "Protein Characterisation",
            "process": "Proteins are large, complex molecules that play many critical roles in the body. They do most of the work in cells and are required for the structure, function, and regulation of the body's tissues and organs."
        }
    }

def get_sequence_explanation(step: str, context: dict) -> str:
    """
    Generates a sequence-specific explanation based on the step and context.
    """
    if step == "detection":
        return context.get("explanation", "")
    
    if step == "transcription":
        return context.get("explanation", "")
        
    if step == "translation":
        return context.get("explanation", "")
        
    if step == "protein":
        return context.get("explanation", "")
        
    return ""
