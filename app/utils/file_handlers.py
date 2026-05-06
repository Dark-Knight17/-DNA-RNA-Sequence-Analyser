import os
from werkzeug.utils import secure_filename
from core.fasta import is_fasta, parse_fasta
from core.validation import normalize_sequence

ALLOWED_EXTENSIONS = {'txt', 'fasta'}

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_uploaded_file(file_storage) -> str:
    """
    Processes an uploaded file and returns the biological sequence string.
    Handles .txt and .fasta files.
    """
    if not file_storage or file_storage.filename == '':
        return ""
        
    content = file_storage.read().decode('utf-8')
    
    if is_fasta(content):
        parsed = parse_fasta(content)
        if parsed:
            # We take the first sequence if multiple are present for this application
            return normalize_sequence(parsed[0]['sequence'])
    
    # Otherwise treat as plain text
    return normalize_sequence(content)
