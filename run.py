from model import gemini_prompt, openai_prompt
from util import convert_pdf_to_images, convert_pdf_to_text

if __name__ == "__main__":
    convert_pdf_to_images("/home/jason/Downloads/University of Michigan Affidavit of Financial Support.pdf", " img/")
    convert_pdf_to_text("/home/jason/Downloads/University of Michigan Affidavit of Financial Support.pdf", " text/")