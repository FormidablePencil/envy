import json
from abc import ABC, abstractmethod
from ui_components import SimpleTextInputComponent

class AIComponent(ABC):
    @abstractmethod
    def process(self, input_data):
        pass

class SmartUIFramework:
    def __init__(self, config_path):
        self.components = {}
        self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)

    def register_component(self, name, component):
        if isinstance(component, AIComponent):
            self.components[name] = component
        else:
            raise ValueError("Component must be an instance of AIComponent")

    def process_input(self, component_name, input_data):
        if component_name in self.components:
            return self.components[component_name].process(input_data)
        else:
            raise ValueError(f"Component '{component_name}' not found")

# Example AI Component
class SimpleTextAnalyzer(AIComponent):
    def __init__(self, positive_words, negative_words):
        self.positive_words = positive_words
        self.negative_words = negative_words

    def process(self, input_data):
        # Simple sentiment analysis (very basic example)
        words = input_data.lower().split()
        sentiment_score = sum([1 for word in words if word in self.positive_words]) - \
                          sum([1 for word in words if word in self.negative_words])
        
        if sentiment_score > 0:
            return "Positive sentiment"
        elif sentiment_score < 0:
            return "Negative sentiment"
        else:
            return "Neutral sentiment"

# Demo usage
if __name__ == "__main__":
    # Create and initialize the framework
    framework = SmartUIFramework('config.json')
    
    # Register components
    text_analyzer = SimpleTextAnalyzer(
        framework.config['components']['text_analyzer']['config']['positive_words'],
        framework.config['components']['text_analyzer']['config']['negative_words']
    )
    framework.register_component('text_analyzer', text_analyzer)

    text_input_component = SimpleTextInputComponent(text_analyzer)
    framework.register_component('text_input', text_input_component)
    
    # Process some input
    result = framework.process_input('text_input', "This is a great day!")
    print(result)
