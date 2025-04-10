from model import gemini_prompt
from util import convert_pdf_to_images, convert_pdf_to_text,get_latex_from_response_text,convert_latex_to_pdf
from pathlib import Path

if __name__ == "__main__":
    file_path="/Users/jasoncyhsu/Downloads/MDS Program Guide updated2.pdf"
    path = Path(file_path)
    stem = path.stem  # 'MDS Program Guide updated2'
    convert_pdf_to_images(file_path, "img/")
    prompt=convert_pdf_to_text(file_path, "text/")
    gemini_result=gemini_prompt(str(prompt),"img/")

    latex=get_latex_from_response_text(gemini_result)
    
    with open("output.tex", "w", encoding="utf-8") as f:
        f.write(latex)
    
    output_pdf_name = f"{stem}_translated.pdf"
    convert_latex_to_pdf("output.tex", output_pdf_name)