import json

json_path_ = r'd:\gate2027\gate-notes\questions-filtered.json'

keywords_ = [
    "reflexive", "symmetric", "antisymmetric", "anti-symmetric", "equivalence relation", 
    "partial order", "total number of relations", "transitive"
]

try:
    with open(json_path_, 'r', encoding='utf-8') as f:
        data_ = json.load(f)

    matches_ = []
    
    for item in data_:
        q_text_ = item.get('question', '').lower()
        title_ = item.get('title', '')
        
        found_ = False
        for kw_ in keywords_:
            if kw_ in q_text_:
                found_ = True
                break
        
        if found_:
            matches_.append(item)

    matches_.sort(key=lambda x: x['title'], reverse=True)

    with open(r'd:\GATE2027\GATE-notes\temp_qs.md', 'w', encoding='utf-8') as f:
        if matches_:
            f.write(f"Found {len(matches_)} relevant questions.\n")
            for q in matches_[:5]:
                f.write(f"\n### {q['title']}\n")
                f.write(f"[Discussion Link]({q['link']})\n\n")
                f.write(f"{q['question']}\n")
                f.write("\n---\n")
        else:
            f.write("No matches found.")

except Exception as e:
    print(f"Error: {e}")
