import openai

class AICodeGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_code(self, prompt, model="code-davinci-002", max_tokens=1024, temperature=0.7):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )

        return response.choices[0].text.strip()