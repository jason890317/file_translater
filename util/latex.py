import subprocess
import os

def convert_latex_to_pdf(input_tex_file, output_pdf_name):

    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(current_dir))  # Go up two levels
    
    try:
        # Run XeLaTeX command in the directory where the .tex file is
        result = subprocess.run(
            ["xelatex", 
                "-interaction=nonstopmode",
                f"-jobname={os.path.splitext(output_pdf_name)[0]}",  # Set output filename without extension
                input_tex_file],
            capture_output=True,
            text=True,
            check=True
        )
        
        print(f"Successfully compiled LaTeX to PDF. Output saved as: {output_pdf_name}")
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
