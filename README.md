# AI Truth Analyzer

A small Flask web app that analyzes the truth likelihood of a user-provided statement using the Groq AI API.

## What it does

- Presents a simple web interface for entering a statement
- Sends the statement to `AI_truth_analyzer/analyzer.py`
- Uses Groq chat completions to evaluate:
  - Truth likelihood
  - Reasoning
  - Tone
  - Confidence score
- Displays the analysis result and session history per user

## Project structure

- `AI_truth_analyzer/app.py` — Flask application routes and session handling
- `AI_truth_analyzer/analyzer.py` — AI prompt construction and Groq API call
- `AI_truth_analyzer/templates/index.html` — UI for submitting text and viewing results
- `.gitignore` — ignores virtual environment files and other generated artifacts

## Setup

1. Create or activate a Python virtual environment in `truth_analyzer`.
2. Install dependencies (Flask, dotenv, groq):

```powershell
pip install flask python-dotenv groq
```

3. Create a `.env` file in `AI_truth_analyzer` with your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

## Run the app

From the `AI_truth_analyzer` folder:

```powershell
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Notes

- Session history is stored in memory, so it resets when the app restarts.
- The app uses the `llama-3.3-70b-versatile` model via Groq.
- Keep the `.env` file private and do not commit it to git.

## License

This repository contains example code for an AI truth analysis demo.

