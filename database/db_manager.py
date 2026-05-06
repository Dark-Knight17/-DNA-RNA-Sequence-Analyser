import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'analyzer.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database with the schema."""
    if not os.path.exists(DB_PATH):
        conn = get_db_connection()
        with open(SCHEMA_PATH, 'r') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

def save_analysis(sequence, sequence_type, strand_type, mrna, protein):
    """Saves an analysis record to the database."""
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO analysis_history (sequence, sequence_type, strand_type, mrna_sequence, protein_sequence) VALUES (?, ?, ?, ?, ?)',
        (sequence, sequence_type, strand_type, mrna, protein)
    )
    conn.commit()
    conn.close()

def get_history(limit=10):
    """Retrieves the latest analysis history."""
    conn = get_db_connection()
    history = conn.execute(
        'SELECT * FROM analysis_history ORDER BY timestamp DESC LIMIT ?',
        (limit,)
    ).fetchall()
    conn.close()
    return history
