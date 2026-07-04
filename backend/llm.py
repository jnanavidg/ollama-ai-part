import ollama

client = ollama.Client()

def generate(prompt):
    response = client.generate(
        model="gpt-oss:120b-cloud",
        prompt=prompt
    )

    return response["response"]