# PDF Translator from English to Traditional Chinese

A specialized tool that transforms English PDF documents into Traditional Chinese using Google's Gemini AI. This application intelligently processes PDFs by extracting both textual content and visual elements, then generates high-quality LaTeX code that maintains the original document's layout while providing accurate Chinese translations.

## Features

- **PDF Processing**: Extract text with position information and convert pages to images
- **AI-Powered Translation**: Generate LaTeX code using Google Gemini AI
- **LaTeX Compilation**: Automatically compile LaTeX to PDF using XeLaTeX
- **Structured Output**: Organized directory structure for images, text, LaTeX, and output PDFs

## Requirements

- Python 3.8+
- Google Gemini API key
- LaTeX distribution with XeLaTeX

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file_translator.git
   cd file_translator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install LaTeX distribution:
   - **macOS**: `brew install --cask mactex` or download from [MacTeX website](https://www.tug.org/mactex/)
   - **Windows**: Install [MiKTeX](https://miktex.org/download) or [TeX Live](https://tug.org/texlive/windows.html)
   - **Linux**: `sudo apt install texlive-xetex texlive-fonts-recommended texlive-fonts-extra`

5. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

1. Update the file path in `run.py` to point to your PDF:
   ```python
   file_path = "/path/to/your/document.pdf"
   ```

2. Run the translator:
   ```bash
   python -m file_translater.run
   ```

3. The process will:
   - Extract images to `img/[filename]/`
   - Extract text to `text/[filename]/`
   - Generate LaTeX in `latex/[filename]/[filename].tex`
   - Create translated PDF in `translated_pdf/[filename]/[filename]_translated.pdf`

## Project Structure

```
file_translater/
├── model/
│   ├── __init__.py     # Gemini API integration
│   └── model.py        # AI model implementation
├── util/
│   ├── __init__.py     # Utility functions
│   ├── latex.py        # LaTeX to PDF conversion
│   └── pdf.py          # PDF processing utilities
├── run.py              # Main execution script
└── .env                # Environment variables
```

## Troubleshooting

- **LaTeX Compilation Errors**: Ensure XeLaTeX is installed and in your PATH
- **API Key Issues**: Verify your Gemini API key in the `.env` file
- **Path Problems**: Use absolute paths or ensure correct relative paths

## License

[MIT License](LICENSE)

## Acknowledgements

- Google Gemini AI for providing the translation capabilities
- The LaTeX community for the document formatting system