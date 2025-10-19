Multi-Agent Shopping Recommendation System 🛍️🤖

A Python-based multi-agent AI system designed to help users choose the best electronic products (laptops, phones, tablets, accessories) based on price, performance, and reviews.

This system uses three intelligent AI agents working together in a hierarchical workflow to provide accurate, justified, and human-readable product recommendations, with full traceability using LangSmith.

🚀 Features

🛒 Multi-Agent System: Three agents collaborate for accurate recommendations.

💡 Smart Evaluation: Considers price, performance, user reviews, and ratings.

🤖 Hierarchical AI Reasoning:

Agent A – Deal Hunter: Finds top candidates based on value.

Agent B – Critic: Critically evaluates Agent A’s recommendations.

Agent C – Final Analyst: Analyzes outputs from both agents and produces the final recommendation in human-readable text.

🧭 Tracing & Observability:

Integrated LangSmith to track agent decisions, prompts, and outputs.

Makes debugging, monitoring, and iterative improvements easier.

📊 Supports Diverse Products: Laptops, phones, tablets, headphones, and accessories.

⚡ Modular Architecture: Easily extendable with new agents or LLMs.

🏗️ System Architecture
User Query
   │
   ▼
Agent A – Deal Hunter
   │
   └─> Picks top 3 products (JSON)
   │
   ▼
Agent B – Critic
   │
   └─> Evaluates A's picks and selects the best one (JSON)
   │
   ▼
Agent C – Final Analyst
   │
   └─> Reviews A & B outputs and generates final text recommendation
   │
   ▼
LangSmith Tracing
   │
   ▼
Human-Readable Output


Explanation:

Agent A (Deal Hunter): Scans the product database and selects the top 3 options based on price-performance ratio and ratings.

Agent B (Critic): Reviews Agent A's choices critically, considering user reviews, reliability, and price, then selects the best single product.

Agent C (Final Analyst): Reads both Agent A and B outputs and provides a human-readable final recommendation, optionally adjusting if a better choice is available.

LangSmith: Tracks each agent’s prompt, output, and reasoning flow for debugging, analysis, and performance monitoring.

📂 Project Structure
shopping_duo/
│
├── main.py                 # Entry point
├── llm_config.py           # LLM initialization
├── data/
│   └── products_data.json  # Product database
├── agents/
│   ├── deal_hunter.py      # Agent A logic
│   ├── critic.py           # Agent B logic
│   ├── final_analyst.py    # Agent C logic
│   └── __init__.py
├── utils/
│   └── helpers.py          # Optional utilities
└── tracing/
    └── langsmith_setup.py  # LangSmith integration and tracing setup

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/shopping-duo.git
cd shopping-duo


Create a virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies

pip install langchain langchain-google-genai langsmith


Set Google API key

export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"  # macOS/Linux
set GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY       # Windows


Set LangSmith API key

export LANGSMITH_API_KEY="YOUR_LANGSMITH_API_KEY"

🏃‍♂️ Usage

Run the system:

python main.py


Example Input:

best laptop or phone for AI/ML work under 70,000


Example Output:

🛍️ Agent A (Deal Hunter) Picks:
 - Lenovo IdeaPad Slim 3: Excellent specs and value
 - HP 15s Ryzen 5 Laptop: Strong ML performance
 - OnePlus 12R: Great mobile ML performance

🤖 Agent B (Critic) Final Pick:
 ✅ Lenovo IdeaPad Slim 3 — Balanced performance and battery life

🧩 Agent C (Final Analyst) Recommendation:
After reviewing both agents, I recommend the Lenovo IdeaPad Slim 3.
It provides the best performance-to-cost ratio for ML students.
Its Ryzen 7 and 16GB RAM ensure smooth training on smaller datasets while maintaining good battery life.
Unless portability is your main concern (consider OnePlus 12R), the IdeaPad Slim 3 is the most versatile choice.


LangSmith Tracing:
All agent outputs, prompts, and final reasoning are logged automatically in LangSmith, enabling detailed trace visualization.

💡 How It Works

User query: User specifies the desired product type and budget.

Agent A: Filters and picks top 3 products based on price, ratings, and reviews.

Agent B: Critically evaluates Agent A’s picks, considering performance and reliability, then selects the best option.

Agent C: Reviews both A and B’s outputs and delivers a final human-readable recommendation, optionally overriding if a better choice exists.

LangSmith: Tracks the entire agent interaction flow, making the system transparent and traceable.

🔧 Technologies Used

Python 3.10+

LangChain: Orchestrates multi-agent interactions

Google Gemini AI: LLM backend

LangSmith: Tracing and observability

JSON: Data format for agent communication
