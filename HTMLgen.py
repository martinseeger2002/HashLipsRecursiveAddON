import json
import os

# Define file paths
metadata_path = './build/json/childtraitindex.json'
output_dir = './build/htmls/'

# Load JSON file
with open(metadata_path, 'r') as file:
    metadata = json.load(file)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# HTML template
html_template = """<!DOCTYPE html>
<html>
<head>
    <title>{name}</title>
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        canvas {{
            display: block;
            width: 100vw;
            height: 100vh;
            outline: none;
        }}
        #traitindex {{
            display: none;
        }}
    </style>
</head>
<body>
    <div id="traitindex">{traitindex}</div>
    <script src="/content/2fd9bda05feb18801319b80f8991be03f581a478bf1bcce130183e12c3f7d43ai0"></script>
    <script src="/content/<YourStichedImageJSInscriptionID>"></script>
</body>
</html>
"""

# Generate HTML files
for idx, item in enumerate(metadata, start=1):
    name = item['name']
    traitindex = item['traitindex']
    html_content = html_template.format(name=name, traitindex=traitindex)
    output_path = os.path.join(output_dir, f"html{idx:05d}.html")
    with open(output_path, 'w') as file:
        file.write(html_content)

print(f"Processed HTML files saved to {output_dir}")
