import json

def run_deal_hunter(llm, query, products):
    """
    Agent A: Selects top 3 value-for-money products.
    """
    a_prompt = f"""
    You are Agent A, a deal hunter.
    The user wants: {query}.
    Available products: {products}.
    Choose the 3 best products based on value, performance, and rating.

    Return your answer strictly in JSON format:
    [
      {{ "name": "Product Name", "reason": "why you chose it" }},
      {{ "name": "Product Name", "reason": "why you chose it" }},
      {{ "name": "Product Name", "reason": "why you chose it" }}
    ]
    """

    a_response = llm.invoke(a_prompt).strip()
    try:
        return json.loads(a_response)
    except json.JSONDecodeError:
        return [{"name": "Parsing Error", "reason": a_response}]
