import unittest
from smart_ui_framework import SmartUIFramework
from ui_components import SimpleTextInputComponent

class TestSmartUIFramework(unittest.TestCase):
    def setUp(self):
        self.framework = SmartUIFramework('config.json')

        # Register components
        text_analyzer = SimpleTextAnalyzer(
            self.framework.config['components']['text_analyzer']['config']['positive_words'],
            self.framework.config['components']['text_analyzer']['config']['negative_words']
        )
        self.framework.register_component('text_analyzer', text_analyzer)

        text_input_component = SimpleTextInputComponent(text_analyzer)
        self.framework.register_component('text_input', text_input_component)

    def test_framework_flow(self):
        result = self.framework.process_input('text_input', "This is a great day!")
        self.assertIn('You entered: This is a great day!', result)
        self.assertIn('Sentiment: Positive sentiment', result)
