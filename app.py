from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI()

MAX_WORDS = 6000

def generate_comment(code, detail):
    prompt = f"Explain the following code in {'brief' if detail == 'brief' else 'detailed'} comments:\n\n{code}\n\n# Explanation:"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.3
    )
    
    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    warning = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        detail = request.form.get("detail", "detailed")

        if len(code.split()) > MAX_WORDS:
            warning = "Your code is too long. Please shorten or split it."
        elif code:
            explanation = generate_comment(code, detail)

    return render_template("index.html", explanation=explanation, warning=warning)

if __name__ == "__main__":
    app.run(debug=True)
