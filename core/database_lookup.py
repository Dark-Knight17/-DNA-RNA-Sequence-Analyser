import requests
from typing import List, Dict, Optional

def search_uniprot(protein_sequence: str) -> List[Dict]:
    """
    Searches UniProt for proteins matching the given sequence.
    Returns a list of matching protein details.
    """
    if not protein_sequence or len(protein_sequence) < 5:
        return []

    # UniProt REST API Search
    # Note: For exact sequence matches, searching by sequence in UniProtKB
    url = "https://rest.uniprot.org/uniprotkb/search"
    params = {
        "query": f"sequence:{protein_sequence}",
        "format": "json",
        "fields": "accession,protein_name,organism_name,function_cc",
        "size": 5 # Limit to top 5 results
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for entry in data.get('results', []):
            primary_accession = entry.get('primaryAccession')
            
            protein_desc = entry.get('proteinDescription', {})
            recommended_name = protein_desc.get('recommendedName', {})
            protein_name = recommended_name.get('fullName', {}).get('value', "Unknown Protein")
            
            organism = entry.get('organism', {}).get('scientificName', "Unknown Organism")
            
            # Extract function
            comments = entry.get('comments', [])
            function = "No functional description available."
            for comment in comments:
                if comment.get('commentType') == 'FUNCTION':
                    texts = comment.get('texts', [])
                    if texts:
                        function = texts[0].get('value', function)
                        break
            
            results.append({
                "accession": primary_accession,
                "name": protein_name,
                "organism": organism,
                "function": function,
                "url": f"https://www.uniprot.org/uniprotkb/{primary_accession}/entry"
            })
            
        return results
        
    except requests.exceptions.RequestException as e:
        print(f"UniProt API Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected Error in UniProt Lookup: {e}")
        return []
