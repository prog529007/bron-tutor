import subprocess
from openai import OpenAI

# Replace with your own API key to test!
openai_api_key = 'YOUR-API-KEY'
openai = OpenAI(api_key=openai_api_key)

def generate_code(prompt):
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt = prompt,
            max_tokens = 1500,
            n = 1,
            stop = None,
            temperature = 0.7,
        )
        manim_code = response.choices[0].text.strip()
        return manim_code
    except Exception as e:
        return e

def run_code(code):
    with open('generated_code.py', 'w') as f:
        f.write(code)
    try:
        result = subprocess.run(['manim', '-pql', 'generated_code.py', 'Solution'], capture_output=True, text=True, timeout=100)
        output = result.stdout.strip()
        if "Traceback (most recent call last)" in output:
            error_start_index = output.find("Traceback (most recent call last)")
            error_message = output[error_start_index:]
            return f"Error: {error_message}"
        else:
            return output
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out."
    except Exception as e:
        return f"Error: {e}"

def refine_code(prompt, error_message):
    refined_prompt = f"{prompt}\n Error message: {error_message}\n"
    refined_code = generate_code(refined_prompt)
    return refined_code

def main():
    initial_prompt = """ 
    Can you generate Manim code in order to respond to the following prompt 
    "Explain fundamental linear algebra to me.". Ensure that your response is properly formatted and the manim works well. 
    Make sure you call the main class which will be run "Solution". 
    Important: Ensure that your response doesn't contain anything but code. Your solution must start with the code "from manim import *".
    Also, make sure you don't use "TexMobject" or "Text" for LaTeX lines, and instead use "Tex". Also, make sure in the LaTeX terms you aren't putting "\\" by mistake instead of single "\" for functions.
    Finally, inside the Text blocks, make sure you have a space before using "\frac{}{}". In order to use a function, write "\", not "\\". 
    For example, Tex(r"$\begin{equation}$"). When you use "Tex", don't pass in "font" and "size" parameters.
    Very very important: Sometimes, the text goes out of frame, so make sure the manim you write ensures that the text is in frame!
    Make wise use of shapes in order to better explain the concepts. You can easily make circles, squares, etc in manim.
    """
    
    generated_code = generate_code(initial_prompt)
    print("Generated Code:\n", generated_code)

    initial_output = run_code(generated_code)
    print("Initial Output:\n", initial_output)

    if "Traceback (most recent call last)" in initial_output:
        error_message = initial_output.find("Traceback (most recent call last)")
        refined_code = refine_code(initial_prompt, error_message)
        print("Refined Code:\n", refined_code)

        refined_output = run_code(refined_code)
        print("Refined Output:\n", refined_output)

if __name__ == "__main__":
    main()
