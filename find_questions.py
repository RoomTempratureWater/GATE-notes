import json

json_path = r'd:\GATE2027\GATE-notes\questions-filtered.json'

keywords = [
    "chomsky", "regular language", "finite automata", "context free grammar", 
    "turing machine", "regular expression", "context sensitive", "unrestricted grammar", "push down automata"
]

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matches = []
    
    for item in data:
        q_text = item.get('question', '').lower()
        title = item.get('title', '')
        
        # Simple keyword matching
        found = False
        for kw in keywords:
            if kw in q_text:
                found = True
                break
        
        if found:
            # ensure no math/dm overlap if possible, but let's just group them by score
            score = sum(1 for kw in keywords if kw in q_text)
            matches.append({'data': item, 'score': score})

    # Sort matching questions by score, then by title
    matches.sort(key=lambda x: (x['score'], x['data']['title']), reverse=True)

    print(f"Found {len(matches)} relevant questions.")

    if matches:
        markdown_content = "\n\n---\n## Relevant PYQs\n"
        
        # Select top 5 relevant ones
        for m in matches[:5]:
            q = m['data']
            markdown_content += f"\n### {q['title']}\n"
            markdown_content += f"[Discussion Link]({q['link']})\n\n"
            markdown_content += f"{q['question']}\n"
            markdown_content += "\n---\n"

        with open(r'd:\GATE2027\GATE-notes\TOC\long\Basics_and_Chomsky_Hierarchy_Long.md', 'a', encoding='utf-8') as f:
            f.write(markdown_content)
        with open(r'd:\GATE2027\GATE-notes\TOC\short\Basics_and_Chomsky_Hierarchy_Short.md', 'a', encoding='utf-8') as f:
            f.write(markdown_content)
        print("Written to both long and short notes successfully.")
    else:
        print("No matches found.")

except Exception as e:
    print(f"Error: {e}")
