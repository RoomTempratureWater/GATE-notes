import json

json_path = r'd:\GATE2027\GATE-notes\questions-filtered.json'
target_file_path = r'd:\GATE2027\GATE-notes\DM\short\Graph_Theory_Connectivity_Short.md'


keywords = [
    "adjacency matrix", "eigen value", "eigen vector", "spectrum", 
    "characteristic equation", "linear algebra"
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
            matches.append(item)

    # Sort matching questions by year (newest first logic approx)
    # Assuming title contains year like "GATE CSE 2023"
    matches.sort(key=lambda x: x['title'], reverse=True)

    print(f"Found {len(matches)} relevant questions.")

    if matches:
        markdown_content = "\n\n---\n## Relevant PYQs\n"
        
        # Select top 5 relevant ones
        for q in matches[:5]:
            markdown_content += f"\n### {q['title']}\n"
            markdown_content += f"[Discussion Link]({q['link']})\n\n"
            markdown_content += f"{q['question']}\n"
            markdown_content += "\n---\n"

        print(markdown_content)
    else:
        print("No matches found.")

except Exception as e:
    print(f"Error: {e}")

