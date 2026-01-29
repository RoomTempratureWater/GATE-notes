import json

file_path = r'd:\GATE2027\GATE-notes\questions-filtered.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Keywords specific to today's notes (Graph Theory Basics)
    # High priority: degree sequence, Havel-Hakimi, Handshaking, counting edges/graphs
    high_priority_keywords = ["degree sequence", "havel", "hakimi", "handshaking", "sum of degrees", "maximum number of edges", "simple graph"]
    
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
        
        # Also check for simple degree problems
        if "degree" in q_text and "vertex" in q_text and "connected" not in q_text and score == 0:
             # Potential basic degree question
             if "sum" in q_text or "even" in q_text or "odd" in q_text:
                 score += 0.5
                 matches.append("degree_basic")

        if score > 0:
            selected_questions.append({
                'data': item,
                'score': score,
                'matches': matches
            })

    # Sort by score descending
    selected_questions.sort(key=lambda x: x['score'], reverse=True)

    print(f"Found {len(selected_questions)} highly relevant questions.")
    
    # Print top 5 in detail
    for i, sq in enumerate(selected_questions[:5]):
        q = sq['data']
        print(f"--- Question {i+1} ---")
        print(f"**{q['title']}**")
        print(f"Link: {q['link']}")
        print(f"Content: {q['question']}")
        print("\n")

except Exception as e:
    print(f"Error: {e}")
