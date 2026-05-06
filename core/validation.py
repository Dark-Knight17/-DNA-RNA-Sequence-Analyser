import re

class SequenceValidationError(Exception):
    """Exception raised for invalid sequences."""
    pass

def normalize_sequence(sequence: str) -> str:
    """
    Normalizes a biological sequence by removing whitespace, numbers, and converting to uppercase.
    """
    if not sequence:
        return ""
    # Remove all whitespace, numbers, and convert to uppercase
    normalized = re.sub(r'[\s\d]+', '', sequence).upper()
    return normalized

def validate_sequence(sequence: str) -> bool:
    """
    Validates that a normalized sequence contains only valid nucleotides (A, T, C, G, U).
    Also checks for the invalid mixing of T and U.
    Returns True if valid, raises SequenceValidationError otherwise.
    """
    if not sequence:
        raise SequenceValidationError("Sequence cannot be empty.")
    
    # Check for invalid characters
    invalid_chars = set(sequence) - set('ATCGU')
    if invalid_chars:
        raise SequenceValidationError(f"Sequence contains invalid characters: {', '.join(invalid_chars)}")
        
    # Check for mixed T and U
    if 'T' in sequence and 'U' in sequence:
        raise SequenceValidationError("Sequence cannot contain both Thymine (T) and Uracil (U).")
        
    return True
