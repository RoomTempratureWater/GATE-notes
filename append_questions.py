import json
import os

json_path = r'd:\GATE2027\GATE-notes\questions-filtered.json'
target_file_path = r'd:\GATE2027\GATE-notes\DM\short\Graph_Theory_Basics_Short.md'

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Keywords specific to today's notes
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
             if "sum" in q_text or "even" in q_text or "odd" in q_text:
                 score += 0.5

        if score > 0:
            selected_questions.append({
                'data': item,
                'score': score
            })

    # Sort by score descending
    selected_questions.sort(key=lambda x: x['score'], reverse=True)

    # Prepare markdown to append
    markdown_content = "\n\n---\n## Relevant PYQs\n"
    
    # Take top 3
    for i, sq in enumerate(selected_questions[:3]):
        q = sq['data']
        markdown_content += f"\n### {q['title']}\n"
        markdown_content += f"[Discussion Link]({q['link']})\n\n"
        markdown_content += f"{q['question']}\n"
        markdown_content += "\n---\n"

    # Append to file
    with open(target_file_path, 'a', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Successfully appended {min(3, len(selected_questions))} questions to {target_file_path}")

except Exception as e:
    print(f"Error: {e}")
