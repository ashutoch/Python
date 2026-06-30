# Python Projects

A collection of Python scripts and projects, including learning exercises and applied tools.

## Projects

### Jarvis (VA.py)
A Python-based voice assistant with:
- Gemini AI integration for conversational queries
- Weather lookups
- Reminders
- Web search
- Email sending

### Birthday Mail Automation
Scripts to automatically send formatted birthday emails via Gmail.

### Learning Exercises
Various scripts covering Python fundamentals: variables, data types, operators, conditionals, strings, loops, lists, tuples, dictionaries.

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.venv\Scripts\Activate.ps1` (Windows PowerShell)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file in the root directory with the following keys:
GEMINI_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
GMAIL_ADDRESS=your_email_here
GMAIL_APP_PASSWORD=your_app_password_here
6. Run any script, e.g. `python VA.py`

## Note
This repo does not include `.env` or `.venv` — both are excluded via `.gitignore`. You must provide your own API keys and virtual environment.