import os
import anthropic

class CodeGenerator:
    def __init__(self):
        self.ai_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    def generate_code(self, prompt):
        response = self.ai_client.create_completion(
            prompt=f"Generate a simple Flask web application:\n\n{prompt}",
            max_tokens=1024,
            temperature=0.5,
            stop_sequences=["\n\n"]
        )
        generated_code = response.choices[0].text
        return generated_code