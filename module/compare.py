import fitz  # PyMuPDF
from tkinter import messagebox

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf_file:
        for page_num in range(pdf_file.page_count):
            page = pdf_file.load_page(page_num)
            text += page.get_text()
    return text

def compare_pdf_content(file1_path, file2_path):
    text1 = extract_text_from_pdf(file1_path)
    text2 = extract_text_from_pdf(file2_path)

    if text1 == text2:
        messagebox.showinfo("Popup","The content of the PDF files is the same.")
    else:
        messagebox.showinfo("Popup","The content of the PDF files is different.")