import unittest
import sqlite3
from data_wallet.notebook.main import Notebook

class TestNotebookUseCases(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()
        self.notebook.create_tables()

    def tearDown(self):
        self.notebook.conn.close()

    def test_personal_notes(self):
        # Create a personal note
        source = "My Personal Note"
        relation = "Personal"
        permission = "View"
        subject = "Personal"
        keywords = "personal"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Verify the personal note can be retrieved
        data = self.notebook.get(source, relation, permission, subject, keywords, user_id)
        self.assertIsNotNone(data)
        self.assertEqual(data["source"], source)
        self.assertEqual(data["relation"], relation)
        self.assertEqual(data["permission"], permission)
        self.assertEqual(data["subject"], subject)
        self.assertEqual(data["keywords"], keywords)

        # Verify an unauthorized user cannot access the personal note
        unauthorized_user_id = 2
        self.assertIsNone(self.notebook.get(source, relation, permission, subject, keywords, unauthorized_user_id))

        # Grant the necessary permissions and verify the unauthorized user can now access the note
        self.notebook.cursor.execute("INSERT INTO permissions (user_id, context_id, view_permission, query_permission) VALUES (?, ?, 1, 1)", (unauthorized_user_id, self.notebook.cursor.lastrowid))
        self.notebook.conn.commit()
        data = self.notebook.get(source, relation, permission, subject, keywords, unauthorized_user_id)
        self.assertIsNotNone(data)

    def test_ai_development_notes(self):
        # Create an AI development note
        source = "Philosophy of AI"
        relation = "AI Development"
        permission = "View"
        subject = "AI"
        keywords = "ai, philosophy"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Create an AMV AI note
        source = "AMV AI"
        relation = "AI Development"
        permission = "View"
        subject = "AI"
        keywords = "ai, amv"
        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Verify the AI development notes can be retrieved
        data = self.notebook.get(source, relation, permission, subject, keywords, user_id)
        self.assertIsNotNone(data)
        self.assertEqual(data["source"], source)
        self.assertEqual(data["relation"], relation)
        self.assertEqual(data["permission"], permission)
        self.assertEqual(data["subject"], subject)
        self.assertEqual(data["keywords"], keywords)

    def test_personal_conversation_notes(self):
        # Create a personal conversation note
        source = "Conversations with AI"
        relation = "Personal"
        permission = "View"
        subject = "Personal"
        keywords = "personal, ai"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Verify the personal conversation note can be retrieved by the creator
        data = self.notebook.get(source, relation, permission, subject, keywords, user_id)
        self.assertIsNotNone(data)
        self.assertEqual(data["source"], source)
        self.assertEqual(data["relation"], relation)
        self.assertEqual(data["permission"], permission)
        self.assertEqual(data["subject"], subject)
        self.assertEqual(data["keywords"], keywords)

        # Verify an unauthorized user cannot access the personal conversation note
        unauthorized_user_id = 2
        self.assertIsNone(self.notebook.get(source, relation, permission, subject, keywords, unauthorized_user_id))

    def test_property_subscription_manager(self):
        # Create a property subscription
        source = "My Codebase"
        relation = "Property Subscription"
        permission = "View"
        subject = "Codebase"
        keywords = "codebase, properties"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Verify the property subscription can be retrieved
        data = self.notebook.get(source, relation, permission, subject, keywords, user_id)
        self.assertIsNotNone(data)
        self.assertEqual(data["source"], source)
        self.assertEqual(data["relation"], relation)
        self.assertEqual(data["permission"], permission)
        self.assertEqual(data["subject"], subject)
        self.assertEqual(data["keywords"], keywords)

if __name__ == '__main__':
    unittest.main()
