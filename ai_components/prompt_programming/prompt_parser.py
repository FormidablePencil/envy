import re
import ast

class PromptParser:
    def parse_prompt(self, prompt):
        # Parse the natural language prompt and extract relevant information
        parsed_prompt = {}

        # Extract the desired functionality
        functionality_pattern = r'create\s+(\w+)'
        match = re.search(functionality_pattern, prompt, re.IGNORECASE)
        if match:
            parsed_prompt['functionality'] = match.group(1)
        else:
            parsed_prompt['functionality'] = 'unknown'

        # Extract the title (if provided)
        title_pattern = r'with\s+the\s+title\s+"([^"]+)"'
        match = re.search(title_pattern, prompt, re.IGNORECASE)
        if match:
            parsed_prompt['title'] = match.group(1)
        else:
            parsed_prompt['title'] = 'Untitled'

        # Extract the list of items (if provided)
        items_pattern = r'the\s+following\s+items:\s*"([^"]+)"'
        match = re.search(items_pattern, prompt, re.IGNORECASE)
        if match:
            parsed_prompt['items'] = [item.strip() for item in match.group(1).split(',')]
        else:
            parsed_prompt['items'] = []

        return parsed_prompt