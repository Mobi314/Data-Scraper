import os
from file_handler.pdf_handler import extract_pdf_text
from file_handler.docx_handler import extract_docx_text
from file_handler.excel_handler import extract_excel_data

def main():
    directory = 'path_to_files'
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            text = extract_pdf_text(os.path.join(directory, filename))
            print(f"Extracted text from {filename}: {text}")
        elif filename.endswith('.docx'):
            text = extract_docx_text(os.path.join(directory, filename))
            print(f"Extracted text from {filename}: {text}")
        elif filename.endswith('.xlsx'):
            data = extract_excel_data(os.path.join(directory, filename))
            print(f"Extracted data from {filename}: {data}")
        else:
            print(f"Unsupported file type: {filename}")

if __name__ == '__main__':
    main()
