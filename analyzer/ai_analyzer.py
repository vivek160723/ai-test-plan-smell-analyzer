import ollama

def ai_analysis(text):

    prompt = f"""
    You are a QA expert.

    Analyze this manual test plan:
    - Identify unclear steps
    - Missing edge cases
    - Duplicate scenarios
    - Suggest improvements

    Test Plan:
    {text}
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
