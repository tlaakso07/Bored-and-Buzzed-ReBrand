import os

files = [
    '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website/BnB-Website-Prototype-v4.html',
    '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website/BnB-Website-Standalone.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace em dash
    content = content.replace('—', '-')
    # Replace en dash
    content = content.replace('–', '-')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Dashes replaced successfully!")
