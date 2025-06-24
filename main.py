import os
import pandas as pd

# Import your local paths (this file should be excluded via .gitignore)
from config_local import ROOT_DIR, OUTPUT_PATH

data = []

# Walk through the directory tree to find .txt files
for subdir, _, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(subdir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
            except Exception as e:
                content = f"Error reading file: {e}"
            data.append({
                "File Name": file,
                "Folder Path": subdir,
                "Content": content
            })

# Create the output Excel spreadsheet
df = pd.DataFrame(data)
df.to_excel(OUTPUT_PATH, index=False)

print(f"Done! Spreadsheet saved as: {OUTPUT_PATH}")
