import os
import pandas as pd

# Hardcoded folder where the .txt files are
root_dir = r"C:\Users\bjhoare\OneDrive - AUCKLAND MUSEUM\Brodie's Files\Projects\FromThePage Migration\How to manage the honey bee export examples\plaintext\searchable_transcript_pages"

data = []

for subdir, _, files in os.walk(root_dir):
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

df = pd.DataFrame(data)

# Correct: save as an .xlsx file with full path
output_path = r"C:\Users\bjhoare\OneDrive - AUCKLAND MUSEUM\Brodie's Files\Projects\FromThePage Migration\How to manage the honey bee export examples\plaintext\processed_transcript_pages.xlsx"
df.to_excel(output_path, index=False)

print(f"Done! Spreadsheet saved as: {output_path}")
