# DNA & RNA Sequence Analyser 🧬

A professional computational biology educational platform developed for CSC 442. This web-based application accepts DNA or RNA sequences, intelligently determines the sequence type, performs core molecular biology processes, and explains the biological meaning of each step in plain English.

## 🚀 Features

- **Intelligent Detection:** Automatically identifies if a sequence is DNA or RNA based on nucleotide composition.
- **Biologically Correct Pipeline:** Implements transcription and translation with support for both coding and template DNA strands.
- **Protein Characterisation:** Analyzes polypeptide chains for length, amino acid frequency, and hydrophobicity/polarity overview.
- **External Database Integration:** Queries the **UniProt REST API** to provide real-world functional context for generated protein sequences.
- **Educational Explanations:** Every step includes layperson-friendly biological explanations alongside sequence-specific transformations.
- **Flexible Input:** Supports manual text entry, file uploads (.txt, .fasta), and drag-and-drop.
- **Responsive UI:** Modern, scientific interface built with a mobile-first approach.

## 🧬 Biological Workflow

1. **Input:** Manual text, .txt file, or .fasta file.
2. **Normalization:** Removes whitespace and invalid characters.
3. **Detection:** Checks for T (DNA) or U (RNA).
4. **Transcription:** Converts DNA to mRNA (respecting strand selection).
5. **Translation:** Maps mRNA codons to amino acids using the standard genetic code.
6. **Analysis:** Builds the polypeptide chain and calculates protein properties.
7. **Lookup:** Searches UniProt for matching biological entries.

## 🏗️ Architecture

The project follows a modular layered architecture, separating biological logic from the web interface.

- **`app/`**: Flask web application (routes, templates, static files).
- **`core/`**: Biological engine (validation, transcription, translation, protein analysis, API lookup).
- **`database/`**: SQLite persistence for analysis history.
- **`app/utils/`**: Helper utilities for file handling and parsing.

## 🛠️ Tech Stack

- **Backend:** Python 3.12, Flask
- **Frontend:** HTML5, CSS3, JavaScript, Jinja2
- **Database:** SQLite
- **APIs:** UniProt REST API
- **Libraries:** Requests, Werkzeug

## 💻 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd DNA_and_RNA_sequence_analyser
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the platform:**
   Open `http://127.0.0.1:5000` in your web browser.

## 📁 Project Structure

```text
DNA_and_RNA_sequence_analyser/
├── app/
│   ├── routes/        # Flask route Blueprints
│   ├── static/        # CSS, JS, and images
│   ├── templates/     # Jinja2 HTML templates
│   ├── uploads/       # Temporary file storage
│   └── utils/         # File handling logic
├── core/
│   ├── detection.py      # DNA/RNA detection logic
│   ├── validation.py     # Normalization and validation
│   ├── transcription.py  # DNA -> RNA logic
│   ├── translation.py    # RNA -> Amino Acid logic
│   ├── codon_table.py    # Genetic code mapping
│   ├── protein.py        # Protein analysis utilities
│   ├── explanations.py   # Educational content templates
│   └── database_lookup.py # UniProt API integration
├── database/
│   ├── analyzer.db       # SQLite database file
│   └── schema.sql        # Database schema definition
├── app.py                # Main application entry point
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

## 🔮 Future Improvements

- Integration with NCBI BLAST for more comprehensive sequence alignment.
- 3D protein structure visualization using libraries like NGLView.
- Support for alternative genetic codes (e.g., mitochondrial DNA).
- User accounts to save and manage long-term analysis history.

## 📄 License

This project was developed for academic purposes as part of CSC 442.
