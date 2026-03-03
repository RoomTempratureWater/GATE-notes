import json

file_path = r'd:\GATE2027\GATE-notes\questions-filtered.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Keywords specific to Group Theory
    high_priority_keywords = ["subgroup", "cyclic group", "generator", "lagrange", "group theory", "semi group", "monoid", "abelian group", "algebraic structure"]
    
    selected_questions = []

    for item in data:
        q_text = item.get('question', '').lower()
        title = item.get('title', '')
        
        score = 0
        matches = []
        for kw in high_priority_keywords:
            if kw in q_text:
                score += 1
                matches.append(kw)
        
        # Also check for specific phrases
        if "identity element" in q_text or "inverse element" in q_text or "binary operation is associative" in q_text or "mathematical group" in q_text:
             score += 0.5
             matches.append("group_properties")

        if score > 0:
            # exclude COA/architecture words just in case
            if "cache" not in q_text and "associative mapping" not in q_text:
                selected_questions.append({
                    'data': item,
                    'score': score,
                    'matches': matches
                })

    # Sort by score descending
    selected_questions.sort(key=lambda x: x['score'], reverse=True)

    print(f"Found {len(selected_questions)} highly relevant questions.")
    
    # Print top 5 in detail to a file
    with open('qt.md', 'w', encoding='utf-8') as out_f:
        for i, sq in enumerate(selected_questions[:5]):
            q = sq['data']
            out_f.write(f"--- Question {i+1} ---\n")
            out_f.write(f"**{q['title']}**\n")
            out_f.write(f"Link: {q['link']}\n")
            out_f.write(f"Content: {q['question']}\n\n")

except Exception as e:
    print(f"Error: {e}")
