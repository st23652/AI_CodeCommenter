# AI Code Commenter 
AI Code Commenter is a web application that automatically generates detailed or brief explanatory comments for your source code using OpenAI's GPT models. It helps developers understand, document, and maintain their code efficiently.

## Features 
- Paste any code snippet and get detailed or brief explanations as comments.
- Choose between GPT-4o and GPT-3.5 Turbo models.
- Adjust creativity with a temperature slider (0 to 1).
- Dark mode toggle for comfortable viewing day or night.
- Copy explanation text to clipboard.
- Download explanation as a text file.
- Deployable on Render or any Python-friendly hosting.

## Technologies Used 
- **Python 3.13+**
- **Flask**
- Lightweight web framework
- **OpenAI Python SDK**
- For AI-powered code explanation
- **python-dotenv**
- Manage environment variables securely
- **Render**
- Deployment platform (optional)
- **HTML, CSS, JavaScript**
- Frontend with dark mode and UI features

## Installation and Setup 
### Prerequisites 
- Python 3.13 or higher
- An OpenAI API key (sign up at [OpenAI](https://platform.openai.com/signup))
- Git

### Local 
Setup 1. Clone the repository: 
```bash
git clone https://github.com/st23652/AI\_CodeCommenter.git
cd AI_CodeCommenter

# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

# On Windows use:
venv\\Scripts\\activate

# Install dependencies:
pip install -r requirements.txt

# Create a .env file in the root directory with your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here

# Run the Flask app locally:
python app.py
```

- Open your browser and go to http://localhost:5000.
- Select the comment detail level (Detailed or Brief).
- Choose the AI model (gpt-4o or gpt-3.5-turbo).
- Adjust the creativity (temperature) slider to your liking.
- Click Generate Comments. View, copy, or download the generated explanation.
- Use the dark mode toggle in the top right corner for a comfortable theme.
- Deployment on Render (Optional) Push your code to GitHub.
- Create a new web service on Render.
- Connect your GitHub repo.
- Set the environment variable OPENAI_API_KEY in the Render dashboard under "Environment".
- Set the build command to:
``` bash
pip install -r requirements.txt
```
- Set the start command to:
``` bash
python app.py
```
- Deploy and visit your live app URL.

## Important Notes 
- Never commit your .env file or API keys to the repository.
- The app restricts code input size to 6000 words to avoid overloading the API.
- The OpenAI API key must be set as an environment variable named OPENAI_API_KEY.
- Use the latest OpenAI API version and Python SDK for best results.
- Adjust max tokens and temperature in app.py to fine-tune response length and creativity.
- Future Improvements Add user authentication.
- Support file uploads for code.
- Add history or save feature for past explanations.
- Support more programming languages or frameworks.
- UI/UX improvements with React or Vue frontend.

## License 
MIT 

## License Contact 
- Created by Sneha Tandon
- Email: 5688sneha8865@gmail.com
- LinkedIn: https://linkedin.com/in/sneha21042004

## Feel free to contribute or report issues! 
## If you want me to help with anything else — just let me know! 
