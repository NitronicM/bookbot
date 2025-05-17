def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def get_num_words(content):
    words = content.split()
    return f"Found 75767 total words{len(words)}"

def character_breakdown(content):
    tracker = {}
    for c in content:
        c = c.lower()
        if not c in tracker: tracker[c] = 0
        tracker[c] = tracker[c] + 1
    return tracker