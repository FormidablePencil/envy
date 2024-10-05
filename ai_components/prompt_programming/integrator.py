import os

from .prompt_parser import PromptParser
from .code_generator import CodeGenerator

class Integrator:
    def __init__(self):
        self.prompt_parser = PromptParser()
        self.code_generator = CodeGenerator()

    def integrate_code(self, generated_code, output_dir='.'):
        # Parse the prompt to get the functionality
        parsed_prompt = self.prompt_parser.parse_prompt('') # Pass an empty string since we already have the parsed prompt
        file_name = f"{parsed_prompt['functionality']}.py"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w') as f:
            f.write(generated_code)

        print(f"Generated code saved to: {file_path}")

        # Optionally, execute the generated code
        # This would depend on the specific requirements of the AI-powered codebase infrastructure
        # For example, you could use the execute_command tool to run the generated script
        # execute_command(f"python {file_path}")

    def process_prompt(self, prompt, output_dir='.'):
        parsed_prompt = self.prompt_parser.parse_prompt(prompt)
        generated_code = self.code_generator.generate_code(parsed_prompt)
        self.integrate_code(generated_code, output_dir)