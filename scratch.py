import base64
import os
import re

html_path = '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website/BnB-Website-Prototype-v4.html'
out_path = '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website/BnB-Website-Standalone.html'
base_dir = '/Users/trevorlaakso/Desktop/Buzzed Rebrand/Website'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_local_img(match):
    path = match.group(2)
    if not path.startswith('../'):
        return match.group(0)
    
    abs_path = os.path.normpath(os.path.join(base_dir, path))
    try:
        with open(abs_path, 'rb') as img_f:
            b64 = base64.b64encode(img_f.read()).decode('utf-8')
        ext = os.path.splitext(abs_path)[1][1:].lower()
        if ext == 'svg':
            ext = 'svg+xml'
        return f'{match.group(1)}="data:image/{ext};base64,{b64}"'
    except Exception as e:
        print(f"Failed to read {abs_path}: {e}")
        return match.group(0)

# Replace src="..."
content = re.sub(r'(src)=["\']([^"\']+)["\']', replace_local_img, content)

def replace_url(match):
    full_match = match.group(0)
    path = match.group(1)
    if not path.startswith('../'):
        return full_match
    
    abs_path = os.path.normpath(os.path.join(base_dir, path))
    try:
        with open(abs_path, 'rb') as img_f:
            b64 = base64.b64encode(img_f.read()).decode('utf-8')
        ext = os.path.splitext(abs_path)[1][1:].lower()
        if ext == 'svg':
            ext = 'svg+xml'
        return f'url("data:image/{ext};base64,{b64}")'
    except Exception as e:
        print(f"Failed to read {abs_path}: {e}")
        return full_match

content = re.sub(r'url\(["\']?([^"\'\)]+)["\']?\)', replace_url, content)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created BnB-Website-Standalone.html with Base64 images!")
