import json
from llm_config import get_llm
from agents.deal_hunter import run_deal_hunter
from agents.critic import run_critic
from agents.final_analyst import run_final_analyst

def shopping_duo(query):
    llm = get_llm()

    # Load product data
    with open("data/products_data.json", "r") as f:
        products = json.load(f)

    # --- Agent A ---
    agent_a = run_deal_hunter(llm, query, products)

    # --- Agent B ---
    agent_b = run_critic(llm, agent_a)

    # --- Agent C ---
    final_text = run_final_analyst(llm, agent_a, agent_b)

    # Display results neatly
    print("\n🧭 Multi-Agent Shopping Recommendation\n")
    print("🛍️ Agent A (Deal Hunter) Picks:")
    for item in agent_a:
        print(f" - {item['name']}: {item['reason']}")

    print("\n🤖 Agent B (Critic) Final Pick:")
    print(f" ✅ {agent_b.get('final_choice', 'N/A')} — {agent_b.get('reason', '')}")

    print("\n🧩 Agent C (Final Analyst) Recommendation:")
    print(final_text)

    return {
        "agent_a": agent_a,
        "agent_b": agent_b,
        "agent_c": final_text
    }


if __name__ == "__main__":
    shopping_duo("best phone or laptop for ML students under 70,000")
