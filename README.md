# AI File Analyzer

A simple PDF analysis web app built with Python, Streamlit, and PyMuPDF.

## Features

- Upload a PDF file
- Count pages, words, and characters
- Calculate average words per page
- Extract and display selectable PDF text
- Download extracted text as a `.txt` file

## Requirements

- Python 3.10 or newer
- pip

## Run locally

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL printed in the terminal.

## Limitations

This app extracts selectable text from PDFs. It does not perform OCR on scanned pages and does not generate AI summaries.
