from pathlib import Path
import json

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Copilot Demo – Sales Booster")

DATA_PATH = Path(__file__).parent / "data.json"


def load_notes():
    with DATA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


@app.get("/api/notes")
def get_notes():
    """Return all sales notes as JSON."""
    return load_notes()


@app.get("/", response_class=HTMLResponse)
def index():
    """Return a nicer HTML page with cards and language toggle."""
    html = """
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Copilot Demo – Sales Booster</title>
        <style>
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: #0d1117;
            color: #c9d1d9;
            margin: 0;
            padding: 0;
          }
          header {
            max-width: 960px;
            margin: 0 auto;
            padding: 24px 16px;
            display: flex;
            flex-direction: column;
            gap: 12px;
          }
          .title {
            font-size: 24px;
            font-weight: 600;
            color: #f0f6fc;
          }
          .subtitle {
            font-size: 14px;
            color: #8b949e;
          }
          .lang-toggle {
            margin-top: 8px;
          }
          .lang-toggle button {
            border: 1px solid #30363d;
            background: #161b22;
            color: #c9d1d9;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 12px;
            cursor: pointer;
            margin-right: 8px;
          }
          .lang-toggle button.active {
            background: #238636;
            border-color: #238636;
            color: #ffffff;
          }
          main {
            max-width: 960px;
            margin: 0 auto 40px;
            padding: 0 16px 24px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
          }
          .card {
            background: #161b22;
            border-radius: 12px;
            border: 1px solid #30363d;
            padding: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
            gap: 8px;
          }
          .card-title {
            font-size: 18px;
            font-weight: 600;
            color: #f0f6fc;
          }
          .card-category {
            font-size: 12px;
            color: #8b949e;
          }
          .pill {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 999px;
            border: 1px solid #30363d;
            font-size: 11px;
            color: #8b949e;
          }
          .details-toggle {
            margin-top: 8px;
            border: 1px solid #30363d;
            background: #21262d;
            color: #c9d1d9;
            border-radius: 999px;
            font-size: 12px;
            padding: 6px 10px;
            cursor: pointer;
            align-self: flex-start;
          }
          .details {
            margin-top: 8px;
            font-size: 13px;
            line-height: 1.5;
          }
          .details-section-title {
            margin: 10px 0 2px;
            font-size: 12px;
            font-weight: 600;
            color: #8b949e;
          }
          .hidden {
            display: none;
          }
        </style>
      </head>
      <body>
        <header>
          <div class="title" id="title-en">GitHub Sales Booster – Demo Notes</div>
          <div class="title hidden" id="title-ja">GitHub セールスブースター – デモ用ノート</div>

          <div class="subtitle" id="subtitle-en">
            A compact view of key GitHub products for pre-sales conversations.
            Click a card to see definition, competitors, strengths, value, and a smart insight.
          </div>
          <div class="subtitle hidden" id="subtitle-ja">
            プリセールスで役立つ GitHub 主力プロダクトの要点です。
            カードをクリックすると、定義・競合・強み・価値・インサイトが表示されます。
          </div>

          <div class="lang-toggle">
            <button id="btn-en" class="active">English</button>
            <button id="btn-ja">日本語</button>
          </div>
        </header>

        <main id="cards"></main>

        <script>
          let currentLang = "en";
          let notesData = [];

          function t(en, ja) {
            return currentLang === "en" ? en : ja;
          }

          function updateHeaderLanguage() {
            document.getElementById("title-en").classList.toggle("hidden", currentLang !== "en");
            document.getElementById("subtitle-en").classList.toggle("hidden", currentLang !== "en");
            document.getElementById("title-ja").classList.toggle("hidden", currentLang !== "ja");
            document.getElementById("subtitle-ja").classList.toggle("hidden", currentLang !== "ja");

            document.getElementById("btn-en").classList.toggle("active", currentLang === "en");
            document.getElementById("btn-ja").classList.toggle("active", currentLang === "ja");
          }

          function renderCards() {
            const container = document.getElementById("cards");
            container.innerHTML = "";

            notesData.forEach(note => {
              const title = note["product_" + currentLang];
              const category = note["category_" + currentLang];
              const definition = note["definition_" + currentLang];
              const competitors = note["competitors_" + currentLang];
              const strengths = note["strengths_" + currentLang];
              const value = note["value_" + currentLang];
              const insight = note["insight_" + currentLang];

              const card = document.createElement("div");
              card.className = "card";
              card.innerHTML = `
                <div class="card-title">${title}</div>
                <div class="card-category"><span class="pill">${category}</span></div>
                <button class="details-toggle">${t("Show details", "詳細を表示")}</button>

                <div class="details hidden">
                  <div class="details-section-title">${t("Definition", "定義")}</div>
                  <div>${definition}</div>

                  <div class="details-section-title">${t("Competitors", "競合")}</div>
                  <div>${competitors}</div>

                  <div class="details-section-title">${t("Strengths", "強み")}</div>
                  <div>${strengths}</div>

                  <div class="details-section-title">${t("Customer value", "価値")}</div>
                  <div>${value}</div>

                  <div class="details-section-title">${t("Insight", "インサイト")}</div>
                  <div>${insight}</div>
                </div>
              `;

              card.querySelector(".details-toggle").addEventListener("click", () => {
                const details = card.querySelector(".details");
                const hidden = details.classList.contains("hidden");
                details.classList.toggle("hidden", !hidden);
                card.querySelector(".details-toggle").textContent = hidden
                  ? t("Hide details", "詳細を隠す")
                  : t("Show details", "詳細を表示");
              });

              container.appendChild(card);
            });
          }

          document.getElementById("btn-en").addEventListener("click", () => {
            currentLang = "en";
            updateHeaderLanguage();
            renderCards();
          });

          document.getElementById("btn-ja").addEventListener("click", () => {
            currentLang = "ja";
            updateHeaderLanguage();
            renderCards();
          });

          fetch("/api/notes")
            .then(r => r.json())
            .then(data => {
              notesData = data;
              updateHeaderLanguage();
              renderCards();
            });
        </script>
      </body>
    </html>
    """
    return HTMLResponse(html)

