from langchain_ollama import OllamaLLM
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pdfplumber
import pytesseract
from PIL import Image
import pdf2image
import os

llm = OllamaLLM(model="mistral")  
def extract_text_with_ocr(file_path):
    """Extract text from image-based PDFs using OCR"""
    text = ""
    try:
        images = pdf2image.convert_from_path(file_path)
        for image in images:
            extracted = pytesseract.image_to_string(image)
            if extracted:
                text += extracted
    except Exception as e:
        print(f"OCR error: {e}")
    return text

def read_pdf(file_path):
    text = ""
    
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
    
    # If no text extracted, try OCR
    if not text.strip():
        print("No text found, attempting OCR...")
        text = extract_text_with_ocr(file_path)
    
    return text

def classify_text(text):
    if not text.strip():
        return "Others"
    
    prompt = f"""Classify this document into ONE of these categories only: {', '.join(CATEGORIES)}

Reply with ONLY the category name, nothing else.

Document:
{text[:2000]}"""
    
    response = llm.invoke(prompt).strip()
    
    # Ensure response is a valid category
    for category in CATEGORIES:
        if category.lower() in response.lower():
            return category
    
    return "Others"

CATEGORIES = [
    "Finance",
    "Work",
    "Personal",
    "Healthcare",
    "Taxes",
    "Images",
    "Media",
    "Education",
    "Legal",
    "Others"
]

def extract_document_info(text):
    """Extract detailed information about the document"""
    prompt = f"""Based on this document, provide:
1. Document Type (e.g., contract, invoice, report, form, etc.)
2. Main Purpose (brief description)
3. Key Details (2-3 bullet points)

Document:
{text[:3000]}"""
    
    response = llm.invoke(prompt).strip()
    return response

def process_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    
    if extension == ".pdf":
        text = read_pdf(file_path)
        print(f"Extracted text length: {len(text)}")
    else:
        return
    
    category = classify_text(text)
    print(f"Category: {category}")
    
    info = extract_document_info(text)
    print(f"\nDocument Details:\n{info}")

if __name__ == "__main__":
    test_file = "/Users/venkatajadda/Downloads/Venkat_Jadda_Doc.pdf"
    process_file(test_file)
