# 🧾 Tax Compliance & Audit AI Agent

**A forensic auditing tool powered by Google Gemini and LangChain.**



## 📌 Overview
The **Tax Compliance Agent** is an AI-powered application designed to automate the initial stages of a financial audit. It ingests structured financial records (Revenue, COGS, VAT, etc.) and uses **Google Gemini** to act as a "Senior Forensic Tax Analyst."

The agent performs real-time checks for:
* **VAT Reconciliation:** Verifying if collected vs. paid VAT aligns with the net payable.
* **Effective Tax Rate:** Calculating tax paid against net profit to detect underpayment risks.
* **Compliance Red Flags:** Identifying suspicious transactions (e.g., large uncategorized withdrawals or regulatory penalties).

## 🚀 Features
* **Automated Ledger Analysis:** Instantly processes 15+ rows of financial data.
* **Forensic Persona:** The AI is prompted to act with professional skepticism, avoiding generic advice.
* **Interactive Dashboard:** Built with **Streamlit** for a side-by-side view of raw data and the AI audit report.
* **Downloadable Reports:** Users can download the generated audit findings as a Markdown file.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Orchestration:** LangChain (Core & Google GenAI)
* **LLM:** Google Gemini 1.5 Flash (via API)
* **Data Handling:** Pandas
* **Environment:** Python 3.10+

## 📂 Project Structure
```text
tax_compliance_agent/
├── tax_app.py          # Main Streamlit interface (Frontend)
├── tax_agent.py        # Logic to connect Data + Prompt + LLM
├── tax_data.py         # Mock database/financial records generator
├── tax_prompt.py       # Engineered prompt for the "Auditor Persona"
├── requirements.txt    # Python dependencies
└── README.md           # Documentation

⚙️ Setup & Installation
1. Clone the Repository
Bash
git clone [https://github.com/yourusername/tax-compliance-agent.git](https://github.com/yourusername/tax-compliance-agent.git)
cd tax-compliance-agent

2. Install Dependencies
Bash
pip install -r requirements.txt

3. Configure API Keys
Create a file named .env in the root folder and add your Google Gemini API key:

Ini, TOML
GOOGLE_API_KEY=your_actual_api_key_here
(Get your key from Google AI Studio)

4. Run the Application
Launch the dashboard locally:

Bash
python -m streamlit run tax_app.py