import os
import shutil
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

    words1 = set(text1.split())
    words2 = set(text2.split())

    words1 = set(text1.split())
    words2 = set(text2.split())

    if words1 != words2:
        messagebox.showinfo("Popup","The content of the PDF files is the same.")
    else:
        messagebox.showinfo("Popup","The content of the PDF files is different.")
        os.remove(file2_path)
        copy_file('./file/2024-04-12-simas-saham-unggulan-prospectus copy.pdf','/Users/rohmatdasuki/Documents/')
     
def copy_file(source_file, destination_folder):
    # Check if the source file exists
    if os.path.exists(source_file):
        # Check if the destination folder exists, create it if it doesn't
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Construct the full path to the destination file
        destination_file = os.path.join(destination_folder, os.path.basename(source_file))

        # Copy the file to the destination folder
        shutil.copyfile(source_file, destination_file)
        print(f"The file '{source_file}' has been successfully copied to '{destination_file}'.")
    else:
        print(f"The source file '{source_file}' does not exist.")