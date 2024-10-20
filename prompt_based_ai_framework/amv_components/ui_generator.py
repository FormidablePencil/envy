from prompt_based_ai_framework.prompt_parser import PromptParser
from prompt_based_ai_framework.constraint_analyzer import ConstraintAnalyzer
from prompt_based_ai_framework.code_generator import CodeGenerator
from prompt_based_ai_framework.ai_components import *
from prompt_based_ai_framework.amv_components.animation_engine import AnimationEngine
from prompt_based_ai_framework.amv_components.audio_player import AudioPlayer
from prompt_based_ai_framework.amv_components.interaction_manager import InteractionManager

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
        return "AMV app generated successfully"

if __name__ == "__main__":
    framework = PromptBasedAIFramework()
    prompt = "Generate an AMV app with a black background, a 800x600 canvas, and a music file that cannot contain any offensive content"
    output = framework.process_prompt(prompt)
    print(output)
