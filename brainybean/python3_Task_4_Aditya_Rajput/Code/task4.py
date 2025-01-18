from docx2pdf import convert
import os

def docx_to_pdf(docx_path, output_path=None):
    if not os.path.exists(docx_path):
        raise FileNotFoundError("The specified .docx file does not exist.")

    if not docx_path.lower().endswith('.docx'):
        raise ValueError("The provided file is not a .docx.")

    if output_path is None:
        output_path = os.path.splitext(docx_path)[0] + ".pdf"

    convert(docx_path, output_path)

    return output_path

if __name__ == "__main__":
    input_docx = "example.docx"
    output_pdf = docx_to_pdf(input_docx)
    print(f"PDF created at: {output_pdf}")