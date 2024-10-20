import random

class GeneratorComponent:
    def process(self, data):
        return "hello"

class CreatorComponent:
    def process(self, data):
        return "created"

class ProducerComponent:
    def process(self, data):
        return "produced"

class BuilderComponent:
    def process(self, data):
        return "built"

class OffensiveWordFilter:
    def __init__(self, prohibited_words):
        self.prohibited_words = prohibited_words

    def filter(self, text):
        filtered_text = text
        for word in self.prohibited_words:
            filtered_text = filtered_text.replace(word, "*" * len(word))
        return filtered_text
