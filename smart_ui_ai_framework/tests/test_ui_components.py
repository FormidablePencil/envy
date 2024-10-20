import unittest
from smart_ui_framework import SimpleTextAnalyzer
from ui_components import SimpleTextInputComponent

class TestSimpleTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SimpleTextAnalyzer(['good', 'great'], ['bad', 'terrible'])

    def test_positive_sentiment(self):
        self.assertEqual(self.analyzer.process('This is a great day!'), 'Positive sentiment')

    def test_negative_sentiment(self):
        self.assertEqual(self.analyzer.process('This is a terrible day.'), 'Negative sentiment')

    def test_neutral_sentiment(self):
        self.assertEqual(self.analyzer.process('This is an okay day.'), 'Neutral sentiment')

class TestSimpleTextInputComponent(unittest.TestCase):
    def setUp(self):
        self.analyzer = SimpleTextAnalyzer(['good', 'great'], ['bad', 'terrible'])
        self.component = SimpleTextInputComponent(self.analyzer)

    def test_component_process(self):
        result = self.component.process('This is a great day!')
        self.assertIn('You entered: This is a great day!', result)
        self.assertIn('Sentiment: Positive sentiment', result)
