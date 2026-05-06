CREATE TABLE IF NOT EXISTS analysis_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence TEXT NOT NULL,
    sequence_type TEXT NOT NULL,
    strand_type TEXT,
    mrna_sequence TEXT,
    protein_sequence TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
