from typing import Tuple

def detect_sequence_type(sequence: str) -> Tuple[str, str]:
    """
    Detects if a sequence is DNA or RNA and provides a plain English explanation.
    Assumes the sequence has been normalized and validated.
    
    Returns:
        Tuple[str, str]: (Sequence Type, Explanation)
    """
    if not sequence:
        return "Unknown", "The sequence is empty."
        
    if 'U' in sequence:
        return "RNA", "This sequence was identified as RNA because it contains uracil (U), which is found in RNA instead of thymine (T)."
    elif 'T' in sequence:
        return "DNA", "This sequence was identified as DNA because it contains thymine (T), which is found in DNA instead of uracil (U)."
    else:
        # Contains only A, C, G
        return "DNA/RNA", "This sequence could be either DNA or RNA because it contains only adenine (A), cytosine (C), and guanine (G), which are common to both. We will treat it as DNA by default, but it can also act as RNA."
