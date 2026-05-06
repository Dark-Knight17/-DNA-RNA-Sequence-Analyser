## Project Overview

This project is a web-based computational biology application developed for CSC 442 (Computational Biology & Interdisciplinary Studies).

The application accepts DNA or RNA sequences, intelligently determines the sequence type, performs core molecular biology processes, and explains the biological meaning of each step in plain English.

The system walks the user through:

1. Sequence input
2. Sequence type detection
3. DNA strand selection (if applicable)
4. Transcription
5. Translation
6. Amino acid / polypeptide analysis
7. Protein characterisation
8. External biological database lookup

The application must prioritize:
- scientific correctness
- explainability
- usability
- modularity
- maintainability

---

# PRIMARY OBJECTIVE

Build a professional web-based bioinformatics application that:
- processes nucleotide sequences correctly
- explains biological processes clearly to non-scientists
- integrates with real biological databases
- provides a clean modern user experience
- demonstrates strong software engineering practices

---

# REQUIRED TECHNOLOGY STACK

Language:
- Python 3.12+

Backend:
- Flask

Frontend:
- HTML
- CSS
- JavaScript
- Jinja templates

Database:
- SQLite (via Python sqlite3 standard library)

External APIs:
- UniProt API and/or NCBI BLAST API

Optional Libraries:
- Biopython
- requests

---

# CORE BIOLOGICAL PIPELINE

The system must implement the following biological workflow:

Input Sequence
→ Detect DNA/RNA
→ Validate Sequence
→ Determine DNA Strand Type
→ Transcription
→ Translation
→ Amino Acid Chain
→ Protein Characterisation
→ External Database Search

---

# INPUT REQUIREMENTS

The system must support ALL THREE input methods:

1. Manual typing/pasting into a textarea
2. File upload
3. Drag-and-drop file upload

Supported file types:
- .txt
- .fasta

The application must:
- normalize whitespace
- remove invalid formatting
- preserve biological correctness
- handle uppercase/lowercase input safely

---

# SEQUENCE VALIDATION REQUIREMENTS

## DNA Rules

Allowed bases:
- A
- T
- C
- G

## RNA Rules

Allowed bases:
- A
- U
- C
- G

## Invalid Sequences

The system must detect:
- mixed T and U usage
- invalid characters
- empty sequences
- malformed FASTA input

The system must display:
- clear validation feedback
- human-readable explanations

---

# SEQUENCE TYPE DETECTION

The system must automatically determine:
- DNA
- RNA
- Invalid

Detection explanations must:
- use plain English
- explain why the sequence was classified that way
- be understandable by non-biologists

Example:
"This sequence was identified as RNA because it contains uracil (U), which is found in RNA instead of thymine (T)."

---

# DNA STRAND TYPE HANDLING

If the sequence is DNA:
- ask the user to specify strand type

Supported strand types:
- Non-template strand (coding/sense strand)
- Template strand (antisense strand)

This selection MUST affect transcription logic correctly.

Do NOT show this option for RNA input.

---

# TRANSCRIPTION REQUIREMENTS

The application must:
- generate mRNA correctly
- display original sequence
- display resulting mRNA
- explain the transformation

## Rules

For coding/non-template DNA:
- replace T with U

For template DNA:
- generate complementary RNA

For RNA input:
- explain that transcription is unnecessary or already represented

The system must include:
- biological explanation
- sequence-specific explanation

---

# TRANSLATION REQUIREMENTS

The application must:
- translate mRNA into codons
- map codons to amino acids
- detect start codons
- detect stop codons
- handle incomplete codons safely

Display:
- codon
- amino acid name
- amino acid abbreviation

Example:

| Codon | Amino Acid | Abbreviation |
|---|---|---|
| AUG | Methionine | Met |
| UUU | Phenylalanine | Phe |

---

# CODON TABLE REQUIREMENTS

Implement a complete standard genetic code mapping.

Store codon mappings centrally in reusable configuration/constants.

---

# AMINO ACID / POLYPEPTIDE REQUIREMENTS

Display:
- ordered amino acid chain
- full amino acid names
- abbreviations
- peptide sequence

The application must explain:
- what amino acids are
- what a polypeptide chain is
- how proteins are formed from amino acids

---

# PROTEIN CHARACTERISATION REQUIREMENTS

The system must:
- produce final protein sequence
- analyze protein properties

Suggested characterisation:
- length
- molecular composition
- hydrophobicity overview
- polarity overview
- amino acid frequency

The application must explain:
- what proteins are
- how proteins arise biologically
- why protein structure matters

---

# EXTERNAL DATABASE INTEGRATION

The application must query at least ONE external biological database.

Preferred:
- UniProt API

Optional:
- NCBI BLAST

The system must:
- search using protein sequence
- display real-world matches

Display:
- protein name
- organism
- protein function
- accession/reference ID

Handle:
- failed searches
- empty results
- rate limiting
- API errors gracefully

---

# EXPLANATION REQUIREMENTS (CRITICAL)

For EVERY major step:
- Detection
- Transcription
- Translation
- Amino Acids
- Protein

The application MUST explain:

1. What the biological process is
2. How it was performed on the user's specific sequence

These explanations MUST:
- use plain English
- avoid excessive jargon
- remain scientifically accurate
- be understandable to non-scientists

This is a grading requirement.

---

# USER INTERFACE REQUIREMENTS

The UI must:
- be modern and clean
- feel scientific/professional
- be responsive
- support drag-and-drop uploads
- provide clear step-by-step visualization
- provide readable tables and outputs

Suggested sections:
- Input Panel
- Detection Results
- Transcription Results
- Translation Results
- Amino Acid Chain
- Protein Analysis
- Database Lookup Results

---

# ARCHITECTURE REQUIREMENTS

Use modular layered architecture.

Suggested structure:

project-root/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── uploads/
│   └── utils/
│
├── core/
│   ├── detection.py
│   ├── validation.py
│   ├── transcription.py
│   ├── translation.py
│   ├── codon_table.py
│   ├── protein.py
│   ├── explanations.py
│   └── database_lookup.py
│
├── database/
│   └── analyzer.db
│
├── docs/
│
├── requirements.txt
├── .gitignore
├── README.md
└── Gemini.md

---

# DATABASE REQUIREMENTS

Use SQLite for:
- sequence history
- analysis history
- uploaded file metadata
- cached API results (optional)

Suggested schema:
- id
- sequence
- sequence_type
- strand_type
- mrna_sequence
- protein_sequence
- timestamp

---

# VALIDATION REQUIREMENTS

Reject:
- empty input
- invalid characters
- mixed DNA/RNA symbols
- malformed FASTA files

Provide:
- precise error messages
- friendly explanations

---

# SOFTWARE ENGINEERING REQUIREMENTS

Code must:
- be modular
- use reusable services
- avoid duplicated logic
- use type hints where reasonable
- include structured error handling
- separate UI from biological logic

Avoid:
- giant route files
- deeply nested logic
- hardcoded biological mappings everywhere
- duplicated codon logic

---

# GIT WORKFLOW REQUIREMENTS (CRITICAL)

After EVERY meaningful atomic implementation step:
- create a git commit immediately

Commits MUST be:
- small
- isolated
- descriptive
- logically scoped

Use conventional commit style where appropriate.

Examples:
- feat(core): implement DNA/RNA detection
- feat(transcription): add template strand transcription
- feat(upload): support FASTA uploads
- feat(api): integrate UniProt search
- fix(validation): reject mixed thymine and uracil
- refactor(core): extract codon translation service

NEVER:
- batch unrelated changes
- create giant commits
- mix refactors and features unnecessarily

---

# REQUIRED DEVELOPMENT PROCESS

For EVERY implementation step:

1. Inspect repository structure first
2. Explain intended change briefly
3. Implement only the scoped change
4. Verify imports and execution flow
5. Run sanity checks
6. Commit immediately after completion

The repository should remain runnable throughout development.

---

# IMPLEMENTATION ORDER (STRICT)

## PHASE 1 — CORE BIOLOGICAL ENGINE

Build:
- sequence normalization
- validation system
- DNA/RNA detection
- transcription engine
- codon translation engine
- amino acid mapping
- protein characterization utilities

Commit incrementally.

---

## PHASE 2 — FILE INPUT SYSTEM

Build:
- text input handling
- FASTA parsing
- file uploads
- drag-and-drop support

Commit incrementally.

---

## PHASE 3 — BIOLOGICAL EXPLANATION SYSTEM

Build:
- layperson explanations
- sequence-specific explanations
- educational result formatting

Commit incrementally.

---

## PHASE 4 — FLASK WEB APPLICATION

Build:
- Flask app structure
- routes
- templates
- responsive frontend
- drag-and-drop UI
- results visualization

Commit incrementally.

---

## PHASE 5 — EXTERNAL DATABASE INTEGRATION

Build:
- UniProt and/or BLAST integration
- protein lookup
- result parsing
- graceful error handling

Commit incrementally.

---

# DEPLOYMENT CLARIFICATION

IMPORTANT:

Do NOT:
- deploy the application
- configure CI/CD
- automate hosting
- provision infrastructure

The user will handle deployment manually.

However:
- requirements.txt MUST exist
- .gitignore MUST exist
- environment variable support should exist
- Flask app should remain deployment-ready
- project should remain Render/Railway compatible

---

# README REQUIREMENTS

Generate a professional README containing:

- project overview
- biological workflow explanation
- architecture overview
- folder structure
- setup instructions
- dependency installation
- commands for running the app
- API configuration instructions
- screenshots placeholders
- future improvements

---

# FINAL DELIVERABLE EXPECTATIONS

The final project must:
- fully implement assignment requirements
- be scientifically correct
- provide understandable explanations
- use professional architecture
- maintain clean commit history
- be maintainable and readable
- function reliably

The final application should feel like a polished bioinformatics educational platform, not a prototype.