from .prompt_parser import PromptParser
from .constraint_analyzer import ConstraintAnalyzer
from .code_generator import CodeGenerator
from .ai_components import *

class PromptBasedAIFramework:
    def __init__(self):
        self.prompt_parser = PromptParser()
        self.constraint_analyzer = ConstraintAnalyzer()
        self.code_generator = CodeGenerator({
            'require_strict_compliance': {'module': 'prompt_based_ai_framework.constraint_analyzer', 'class': 'StrictComplianceConstraint'},
            'prefer_compliance': {'module': 'prompt_based_ai_framework.constraint_analyzer', 'class': 'PreferredComplianceConstraint'},
            'prohibit': {'module': 'prompt_based_ai_framework.ai_components', 'class': 'OffensiveWordFilter'},
            'require_specific_conditions': {'module': 'prompt_based_ai_framework.constraint_analyzer', 'class': 'SpecificConditionsConstraint'},
            'generate': {'module': 'prompt_based_ai_framework.ai_components', 'class': 'GeneratorComponent'},
            'create': {'module': 'prompt_based_ai_framework.ai_components', 'class': 'CreatorComponent'},
            'produce': {'module': 'prompt_based_ai_framework.ai_components', 'class': 'ProducerComponent'},
            'build': {'module': 'prompt_based_ai_framework.ai_components', 'class': 'BuilderComponent'}
        })

    def process_prompt(self, prompt: str) -> str:
        """
        Process a natural language prompt and generate the necessary AI-powered functionality.
        
        Args:
            prompt: The natural language prompt.
        
        Returns:
            The generated code or output.
        """
        parsed_prompt = self.prompt_parser.parse_prompt(prompt)
        analyzed_constraints = self.constraint_analyzer.analyze_constraints(parsed_prompt['constraints'])
        generated_code = self.code_generator.generate_code(parsed_prompt['functionality'], parsed_prompt['data'], analyzed_constraints)
        
        # Execute the generated code and return the output
        exec(generated_code)
        return "Output generated successfully"

if __name__ == "__main__":
    framework = PromptBasedAIFramework()
    prompt = "Generate a simple text generator using the word 'hello' and ensure it cannot produce any offensive content"
    output = framework.process_prompt(prompt)
    print(output)
