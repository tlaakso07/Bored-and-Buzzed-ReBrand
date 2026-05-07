import os

files = [
    '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website/BnB-Website-Prototype-v4.html',
    '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website/BnB-Website-Standalone.html'
]

replacements = [
    ("Load More - 647 remaining", "Load More (647 remaining)"),
    ("Blockberry - plus their full", "Blockberry. Plus, their full"),
    ("All sizes - 3.5g through 1g pre-rolls.", "Available in all sizes from 3.5g down to 1g pre-rolls."),
    ("edibles - the full 28 Herbs catalog", "edibles. The full 28 Herbs catalog"),
    ("place to shop - we're a space", "place to shop. We're a space"),
    ("what you're looking for - whether you're", "what you're looking for, whether you're"),
    ("meet &amp; greet - right here", "meet &amp; greet right here"),
    ("just an event - it was a reminder", "just an event; it was a reminder"),
    ("both times - knowledgeable", "both times. Very knowledgeable"),
    ("new to B&amp;B - you both win", "new to B&amp;B. You both win")
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Copy rewritten successfully!")
