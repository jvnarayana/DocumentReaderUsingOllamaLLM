# DocumentReaderUsingOllamaLLM
AI Agent to classify PDF documents and extract document details using OCR and Ollama LLM.
# Document Segregator

A simple Python script to classify PDF documents and extract document details using OCR and Ollama LLM.

## Features

- Extracts text from PDFs using `pdfplumber`
- Falls back to OCR using `pdf2image` + `pytesseract`
- Classifies documents into categories like Finance, Work, Legal, etc.
- Extracts summary information from the document using an Ollama model

## Requirements

- Python 3.13+
- `pdfplumber`
- `pdf2image`
- `pytesseract`
- `Pillow`
- `langchain-ollama`
- `watchdog`
- Ollama local runtime with a downloaded model

## macOS setup

Install system dependencies:

```bash
brew install poppler tesseract

Install Python dependencies in your venv:
source .venv/personalStuffOrganizer/bin/activate
pip install pdfplumber pdf2image pytesseract pillow langchain-ollama watchdog

**Pull or verify installed Ollama model:**

ollama list
ollama pull mistral

**Run the script directly:
**
python "/Users/venkatajadda/AI Projects/.venv/personalStuffOrganizer/segregator.py"

The script currently uses:
test_file = **"/Users/venkatajadda/Downloads/Venkat_Jadda_Doc.pdf"**

Change test_file to your PDF path.

**How it works**
1. read_pdf(file_path) tries to extract text with pdfplumber
2. If no text is found, extract_text_with_ocr(file_path) converts PDF pages to images and runs OCR classify_text(text) sends a prompt to OllamaLLM  and returns one of the predefined categories extract_document_info(text) gets a short summary of the document contents

**Categories:**

Finance
Work
Personal
Healthcare
Taxes
Images
Media
Education
Legal
Others
Notes

**Make sure tesseract is on your PATH.**
If OCR is needed, make sure poppler is installed.
If the model returns verbose output, tighten the prompt or use a model with better instruction-following.

Sample Output looks like this:
<img width="1512" height="982" alt="Screenshot 2026-05-23 at 2 21 40 AM" src="https://github.com/user-attachments/assets/08411b87-4d7a-4531-b659-815be207fb5a" />


