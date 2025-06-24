# txtFileFlattener

**txtFileFlattener** is a Python script that recursively scans a folder for `.txt` files and compiles their content into a single Excel spreadsheet. It is designed to support tasks like migrating page-level transcripts, reviewing OCR output, or preparing bulk content for cataloguing or search indexing.

## Features

- Recursively searches through subfolders for `.txt` files
- Captures the file name, folder path, and text content
- Outputs a structured `.xlsx` spreadsheet
- Suitable for working with exported digital texts or transcription data

## How It Works

1. The script looks inside a specified root directory (`root_dir`) for `.txt` files, including in subfolders.
2. For each file, it reads the full text and stores:
   - File name
   - Folder path
   - Text content
3. The combined results are saved as an Excel spreadsheet (`output_path`).

## Requirements

- Python 3.7+
- `pandas`
- `openpyxl`

Install requirements with:

```bash
pip install pandas openpyxl
