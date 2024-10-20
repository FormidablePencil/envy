import re
from typing import Dict, List

class PromptParser:
    def parse_prompt(self, prompt: str) -> Dict[str, List[str]]:
        """
        Parse a natural language prompt and extract the key requirements and constraints.
        
        Returns:
            A dictionary where the keys are the extracted concepts (e.g. 'functionality', 'data', 'constraints')
            and the values are lists of the corresponding extracted elements.
        """
        # Example implementation (very basic)
        functionality_keywords = ['generate', 'create', 'produce', 'build']
        data_keywords = ['using', 'with', 'from']
        constraint_keywords = ['must', 'should', 'cannot', 'require']
        
        prompt_parts = prompt.lower().split()
        
        functionality = [word for word in prompt_parts if word in functionality_keywords]
        data = [i+1 for i, word in enumerate(prompt_parts) if word in data_keywords]
        constraints = [i+1 for i, word in enumerate(prompt_parts) if word in constraint_keywords]
        
        return {
            'functionality': functionality,
            'data': [' '.join(prompt_parts[i:i+2]) for i in data],
            'constraints': [' '.join(prompt_parts[i:]) for i in constraints]
        }
