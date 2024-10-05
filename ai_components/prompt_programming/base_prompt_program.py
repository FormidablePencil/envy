from .prompt_parser import PromptParser
from .code_generator import CodeGenerator
from .integrator import Integrator
from envy.data_wallet.version_control.auto_versioning import create_new_branch, commit_all_changes, push_changes

class BasePromptProgram:
    def __init__(self):
        self.prompt_parser = PromptParser()
        self.code_generator = CodeGenerator()
        self.integrator = Integrator(self)

    def parse_prompt(self, prompt):
        # Extract relevant information from the natural language prompt
        # This could include identifying the desired functionality, input parameters, etc.
        parsed_prompt = self.prompt_parser.parse_prompt(prompt)
        return parsed_prompt

    def generate_code(self, parsed_prompt):
        # Generate the corresponding code based on the parsed prompt information
        generated_code = self.code_generator.generate_code(parsed_prompt)
        return generated_code

    def integrate_code(self, generated_code):
        # Integrate the generated code with the existing AI-powered codebase infrastructure
        branch_name = f"prompt-programming-changes-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        create_new_branch(branch_name)
        commit_all_changes("envy/prompt_programming", f"Auto-versioned prompt programming changes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        push_changes(branch_name)

    def run_prompt(self, prompt):
        parsed_prompt = self.parse_prompt(prompt)
        generated_code = self.generate_code(parsed_prompt)
        self.integrate_code(generated_code)