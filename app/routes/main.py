from flask import Blueprint, render_template, request, flash, redirect, url_for
from core.validation import normalize_sequence, validate_sequence, SequenceValidationError
from core.detection import detect_sequence_type
from core.transcription import transcribe
from core.translation import translate
from core.protein import analyze_protein
from core.explanations import get_general_explanations
from app.utils.file_handlers import handle_uploaded_file

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    sequence = ""
    
    # Check for manual input
    if 'sequence' in request.form and request.form['sequence'].strip():
        sequence = normalize_sequence(request.form['sequence'])
    
    # Check for file upload
    elif 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            try:
                sequence = handle_uploaded_file(file)
            except Exception as e:
                flash(f"Error processing file: {str(e)}", "error")
                return redirect(url_for('main.index'))
    
    if not sequence:
        flash("Please provide a sequence or upload a file.", "error")
        return redirect(url_for('main.index'))
    
    try:
        # 1. Validation
        validate_sequence(sequence)
        
        # 2. Detection
        seq_type, det_explanation = detect_sequence_type(sequence)
        
        # 3. Handle DNA Strand Selection (if DNA)
        strand_type = request.form.get('strand_type', 'coding')
        
        # 4. Transcription
        mrna, trans_explanation = transcribe(sequence, seq_type, strand_type)
        
        # 5. Translation
        codons, translate_explanation = translate(mrna)
        
        # 6. Protein Characterisation
        protein_analysis, protein_explanation = analyze_protein(codons)
        
        # 7. Explanations
        general_explanations = get_general_explanations()
        
        results = {
            "original_sequence": sequence,
            "sequence_type": seq_type,
            "strand_type": strand_type,
            "detection": {
                "explanation": det_explanation,
                "general": general_explanations['detection']
            },
            "transcription": {
                "mrna": mrna,
                "explanation": trans_explanation,
                "general": general_explanations['transcription']
            },
            "translation": {
                "codons": codons,
                "explanation": translate_explanation,
                "general": general_explanations['translation']
            },
            "protein": {
                "analysis": protein_analysis,
                "explanation": protein_explanation,
                "general": general_explanations['protein']
            }
        }
        
        return render_template('results.html', results=results)
        
    except SequenceValidationError as e:
        flash(str(e), "error")
        return redirect(url_for('main.index'))
    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('main.index'))
