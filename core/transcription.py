from typing import Tuple

def transcribe(sequence: str, sequence_type: str, strand_type: str = "coding") -> Tuple[str, str]:
    """
    Transcribes a sequence into mRNA and provides an explanation.
    
    Args:
        sequence (str): The normalized biological sequence.
        sequence_type (str): "DNA", "RNA", or "DNA/RNA".
        strand_type (str): "coding" (non-template) or "template". Defaults to "coding".
        
    Returns:
        Tuple[str, str]: (mRNA sequence, explanation)
    """
    if sequence_type == "RNA":
        explanation = "The sequence is already RNA, so the transcription step is unnecessary. It can be directly translated into a protein."
        return sequence, explanation
        
    if strand_type == "coding":
        # Coding strand (non-template) matches the mRNA sequence, just with T replaced by U.
        mrna = sequence.replace('T', 'U')
        explanation = "Since this is the coding (non-template) strand, its sequence is almost identical to the resulting mRNA. The only difference is that thymine (T) is replaced by uracil (U) during transcription."
        return mrna, explanation
        
    elif strand_type == "template":
        # Template strand generates complementary RNA.
        # A -> U, T -> A, C -> G, G -> C
        complement_map = str.maketrans('ATCG', 'UAGC')
        mrna = sequence.translate(complement_map)
        explanation = "Since this is the template strand, RNA polymerase builds a complementary mRNA strand. Adenine (A) pairs with uracil (U), thymine (T) pairs with adenine (A), cytosine (C) pairs with guanine (G), and guanine (G) pairs with cytosine (C)."
        return mrna, explanation
        
    else:
        # Fallback for unexpected cases
        return sequence.replace('T', 'U'), "Transcription converts DNA into mRNA by substituting thymine (T) with uracil (U) or generating a complementary sequence."
