# Copilot Demo – Sales Booster

A small FastAPI web app used to demo **GitHub Copilot** (and optionally **GitHub Actions**) in a sales/pre-sales context.

The app stores key sales messages about several GitHub products in **English** and **Japanese**, and displays them as cards with details (definition, competitors, strengths, value, and a “smart insight”).

## GitHub concepts covered

- GitHub Copilot
- GitHub Copilot Agents / Agent HQ
- GitHub Actions
- GitHub Advanced Security
- GitHub Enterprise Cloud

Each concept has:
- **Category** (what kind of product it is)
- **Definition** (clear, neutral description)
- **Competitors** (who else is in this space)
- **Strengths** (why GitHub’s approach is strong)
- **Value** (business outcome, not just features)
- **Insight** (a higher-level observation you can use in conversation)

## Tech stack

- **Python 3.9**
- **FastAPI** + **Uvicorn**
- Simple JSON file (`app/data.json`) as the data store
- Plain HTML + a bit of JavaScript for the front-end

This stack is intentionally lightweight so the focus of the demo is on **GitHub Copilot** assisting with:
- Implementing endpoints and UI
- Refactoring code
- Adding tests
- Explaining unfamiliar code during the conversation

## Running the app locally

```bash
git clone https://github.com/<your-username>/copilot-demo-app.git
cd copilot-demo-app

python3 -m venv .venv
source .venv/bin/activate  # On macOS / Linux

pip install -r requirements.txt

uvicorn app.main:app --reload
# test
