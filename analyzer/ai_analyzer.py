import ollama

def ai_analysis(text):

    prompt = f"""
    You are a senior QA engineer.

    Analyze this structured test plan:
    - Check scenario clarity
    - Validate preconditions
    - Review test steps
    - Evaluate expected results
    - Identify missing edge cases
    - Suggest QA improvements

    Test Plan:
    {text}
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
