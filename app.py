from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_WORDS = 6000

def generate_comment(code, detail, model, temperature):
    prompt = f"Explain the following code in {'brief' if detail == 'brief' else 'detailed'} comments:\n\n{code}\n\n# Explanation:"

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=temperature
    )
    
    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    warning = ""
    code = ""
    model = "gpt-4o"
    temperature = 0.3
    detail = "detailed"

    if request.method == "POST":
        code = request.form.get("code", "")
        detail = request.form.get("detail", "detailed")
        model = request.form.get("model", "gpt-4o")
        temperature = float(request.form.get("temperature", 0.3))

        if len(code.split()) > MAX_WORDS:
            warning = "Your code is too long. Please shorten or split it."
        elif code:
            explanation = generate_comment(code, detail, model, temperature)

    return render_template("index.html",
                           explanation=explanation,
                           warning=warning,
                           selected_model=model,
                           temperature=temperature,
                           code=code,
                           detail=detail)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
