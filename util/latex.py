import subprocess
import os
from pathlib import Path

def convert_latex_to_pdf(input_tex_file, output_pdf_path):
    """
    Convert a LaTeX file to PDF using XeLaTeX
    
    Args:
        input_tex_file: Path to the input .tex file
        output_pdf_path: Path where the output PDF should be saved
    """
    # Convert to Path objects if they're strings
    input_tex_file = Path(input_tex_file)
    output_pdf_path = Path(output_pdf_path)
    
    # Ensure output directory exists
    os.makedirs(output_pdf_path.parent, exist_ok=True)
    
    # Get absolute paths
    input_tex_file_abs = input_tex_file.absolute()
    output_dir_abs = output_pdf_path.parent.absolute()
    output_name = output_pdf_path.stem
    
    try:
        # Run XeLaTeX command with proper working directory and absolute paths
        result = subprocess.run(
            ["xelatex", 
                "-interaction=nonstopmode",
                f"-output-directory={output_dir_abs}",
                f"-jobname={output_name}",
                f"{input_tex_file_abs}"],
            capture_output=True,
            text=True,
            check=True,
            cwd=os.getcwd()  # Run from current directory
        )
        
        print(f"Successfully compiled LaTeX to PDF. Output saved as: {output_pdf_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LaTeX: {e}")
        print(f"XeLaTeX stdout: {e.stdout}")
        print(f"XeLaTeX stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("XeLaTeX not found. Please make sure XeLaTeX is installed and in your PATH.")
        print("You can install it with MacTeX (https://www.tug.org/mactex/) on macOS.")
        return False
