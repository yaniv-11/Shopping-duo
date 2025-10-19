import json

def run_final_analyst(llm, agent_a_output, agent_b_output):
    """
    Agent C: Reads both Agent A and Agent B data, and gives the final recommendation.
    """

    c_prompt = f"""
    You are Agent C, the Final Analyst.
    You receive:
    - Agent A’s picks: {agent_a_output}
    - Agent B’s evaluation: {agent_b_output}

    Your job:
    1. Review Agent A’s reasoning and Agent B’s criticism.
    2. Validate if Agent B’s choice makes sense.
    3. If you agree, justify it with extra insights.
       If you disagree, pick a better product and justify your decision.
    4. Explain your reasoning clearly in text (not JSON).

    Output a human-readable recommendation with:
    - Final product name
    - Why it’s the best fit
    - Optional advice or comparison insight
    """

    response = llm.invoke(c_prompt).strip()
    return response
