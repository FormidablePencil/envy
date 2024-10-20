from smart_ui_framework import AIComponent

class SimpleTextInputComponent(AIComponent):
    def __init__(self, text_analyzer):
        self.text_analyzer = text_analyzer

    def process(self, input_data):
        sentiment = self.text_analyzer.process(input_data)
        return f"You entered: {input_data}\nSentiment: {sentiment}"
