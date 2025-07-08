import os
import pandas as pd
import re
from config_local import PARENT_DIR, OUTPUT_BASE_DIR

def natural_sort_key(filename):
    """Return a tuple to safely sort files like 1.txt, 10.txt, cover.txt."""
    base = os.path.splitext(filename)[0]
    match = re.match(r"(\d+)", base)
    if match:
        return (0, int(match.group(1)))
    else:
        return (1, base.lower())

for work_folder in os.listdir(PARENT_DIR):
    work_path = os.path.join(PARENT_DIR, work_folder)
    transcript_path = os.path.join(work_path, "plaintext", "verbatim_transcript_pages")

    if not os.path.isdir(transcript_path):
        print(f"⚠ Skipped (no transcript folder): {work_folder}")
        continue

    # Extract the last word as the folder's ID (textafter)
    folder_id = work_folder.strip().split(" ")[-1]

    data = []
    files = sorted(os.listdir(transcript_path), key=natural_sort_key)

    for file in files:
        if not file.endswith(".txt"):
            continue

        file_path = os.path.join(transcript_path, file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
        except Exception as e:
            content = f"Error reading file: {e}"

        base_filename = os.path.splitext(file)[0]
        match = re.match(r"(\d+)", base_filename)
        if match:
            padded_number = match.group(1).zfill(4)
            custom_id = f"{folder_id}-{padded_number}"
        else:
            custom_id = f"{folder_id}-{base_filename}"

        data.append({
            "File Name": file,
            "Folder Path": transcript_path,
            "Custom ID": custom_id,       # now before content
            "Content": content
        })

    if data:
        df = pd.DataFrame(data)
        os.makedirs(OUTPUT_BASE_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_BASE_DIR, f"{work_folder}.xlsx")
        df.to_excel(output_path, index=False)
        print(f"Processed: {work_folder} → {output_path}")
    else:
        print(f"⚠ No text files found in: {work_folder}")
