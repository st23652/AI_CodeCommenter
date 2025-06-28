from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file (e.g., OPENAI_API_KEY)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client using API key from environment variable
client = OpenAI()

# Set maximum allowed word count for input code
MAX_WORDS = 6000

def generate_comment(code: str, detail: str, model: str, temperature: float) -> str:
    """
    Generates an explanation for the given code using OpenAI's chat model.
    
    Parameters:
        code (str): The input source code to explain
        detail (str): 'brief' or 'detailed' level of comment
        model (str): OpenAI model to use (e.g., 'gpt-4o')
        temperature (float): Temperature for creativity (0.0 to 1.0)
    
    Returns:
        str: AI-generated explanation
    """
    prompt = f"Explain the following code in {'brief' if detail == 'brief' else 'detailed'} comments:\n\n{code}\n\n# Explanation:"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,       # You can adjust this based on output size needs
        temperature=temperature
    )

    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    warning = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        detail = request.form.get("detail", "detailed")
        model = request.form.get("model", "gpt-4o")
        temperature = float(request.form.get("temperature", 0.3))

        if len(code.split()) > MAX_WORDS:
            warning = "⚠️ Your code is too long. Please shorten or split it into parts."
        elif code.strip():
            explanation = generate_comment(code, detail, model, temperature)

    return render_template("index.html", explanation=explanation, warning=warning)

if __name__ == "__main__":
    # Use Render's provided $PORT if available, fallback to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
