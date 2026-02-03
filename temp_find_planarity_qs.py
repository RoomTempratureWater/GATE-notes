import json

json_path = r'd:\GATE2027\GATE-notes\questions-filtered.json'

keywords = [
    "planar", "planarity", "kuratowski", "euler's formula", "regions", "faces"
]

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    matches = []
    
    for item in data:
        q_text = item.get('question', '').lower()
        title = item.get('title', '')
        
        found = False
        for kw in keywords:
            if kw in q_text or kw in title.lower():
                found = True
                break
        
        if found:
            matches.append(item)

    # Sort matching questions by year (newest first logic approx)
    matches.sort(key=lambda x: x['title'], reverse=True)

    print(f"Found {len(matches)} relevant questions.")

    if matches:
        print(json.dumps(matches[:5], indent=2))
    else:
        print("No matches found.")

except Exception as e:
    print(f"Error: {e}")
