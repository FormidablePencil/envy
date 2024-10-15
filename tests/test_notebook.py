import unittest
import sqlite3
from data_wallet.notebook.main import Notebook

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()
        self.notebook.create_tables()

    def tearDown(self):
        self.notebook.conn.close()

    def test_create_and_retrieve_data(self):
        # Create a new source, reference, and subscription with a specific context
        source = "Test Source"
        relation = "Test Relation"
        permission = "Test Permission"
        subject = "Test Subject"
        keywords = "test, keyword"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Retrieve the data and verify the context-based permissions
        data = self.notebook.get(source, relation, permission, subject, keywords, user_id)
        self.assertIsNotNone(data)
        self.assertEqual(data["source"], source)
        self.assertEqual(data["relation"], relation)
        self.assertEqual(data["permission"], permission)
        self.assertEqual(data["subject"], subject)
        self.assertEqual(data["keywords"], keywords)

    def test_remove_data(self):
        # Create a new source, reference, and subscription with a specific context
        source = "Test Source"
        relation = "Test Relation"
        permission = "Test Permission"
        subject = "Test Subject"
        keywords = "test, keyword"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Get the source_id and context_id
        self.cursor.execute("SELECT id, context_id FROM source WHERE title = ?", (source,))
        source_id, context_id = self.cursor.fetchone()

        # Remove the data and verify it's no longer accessible
        self.assertTrue(self.notebook.remove(source_id, context_id, user_id))
        self.assertIsNone(self.notebook.get(source, relation, permission, subject, keywords, user_id))

    def test_permissions(self):
        # Create a new source, reference, and subscription with a specific context
        source = "Test Source"
        relation = "Test Relation"
        permission = "Test Permission"
        subject = "Test Subject"
        keywords = "test, keyword"
        user_id = 1

        self.assertTrue(self.notebook.add(source, relation, permission, subject, keywords))

        # Verify that a user without the necessary permissions cannot access the data
        unauthorized_user_id = 2
        self.assertIsNone(self.notebook.get(source, relation, permission, subject, keywords, unauthorized_user_id))

        # Grant the necessary permissions and verify the user can now access the data
        self.notebook.cursor.execute("INSERT INTO permissions (user_id, context_id, view_permission, query_permission) VALUES (?, ?, 1, 1)", (unauthorized_user_id, self.notebook.cursor.lastrowid))
        self.notebook.conn.commit()
        data = self.notebook.get(source, relation, permission, subject, keywords, unauthorized_user_id)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
