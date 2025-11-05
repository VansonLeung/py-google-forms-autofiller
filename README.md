# py-google-forms-autofiller

A Python script to automatically fill Google Forms with generated responses that match statistical trends from survey data.

## Features

- Analyzes survey trends from a markdown file
- Generates probabilistic responses based on the trends
- Automates form filling using Playwright
- Supports multi-page Google Forms with various question types (radio buttons, text inputs, Likert scales)

## Installation

1. Clone or download the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Usage

1. Prepare your trends data in `trends.md` format
2. Run the response generator:
   ```bash
   python generate_responses.py
   ```
3. Update the form URL in `fill_form.py`
4. Run the form filler:
   ```bash
   python fill_form.py
   ```

## Files

- `trends.md`: Survey data counters
- `generate_responses.py`: Script to generate responses matching trends
- `responses.json`: Generated responses
- `fill_form.py`: Script to fill the Google Form
- `requirements.txt`: Python dependencies

## Requirements

- Python 3.7+
- Playwright
- JSON data format for responses

## Disclaimer

Use responsibly and in accordance with Google Forms terms of service. This tool is for educational purposes only.

---

100% made with Grok Code Fast 1, Visual Studio Code and Github Copilot.