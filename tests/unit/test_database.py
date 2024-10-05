import unittest
import sqlite3
from database.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.execute("DELETE FROM tasks")
        self.cursor.execute("DELETE FROM implementation_details")
        self.cursor.execute("DELETE FROM completion_records")
        self.cursor.execute("DELETE FROM coordination_capabilities")
        self.conn.commit()
        self.conn.close()

    def test_commit_task(self):
        task = {"title": "Task 1", "description": "Do something"}
        task_id = self.db.commit_task(task, "2023-04-01", "2,3", "Impacts feature X")
        tasks = self.db.get_tasks()
        records = self.db.get_completion_records()
        self.assertEqual(len(tasks), 1)
        self.assertDictEqual(tasks[0], {'id': task_id, **task})
        self.assertEqual(len(records), 1)
        self.assertDictEqual(records[0], {'id': 1, 'task_id': task_id, 'completed_at': "2023-04-01", 'related_tasks': "2,3", 'impact_notes': "Impacts feature X"})

    def test_create_and_retrieve_implementation_details(self):
        detail1 = {"component": "UI", "description": "Implement button functionality"}
        detail2 = {"component": "Backend", "description": "Implement API endpoint"}
        self.db.create_implementation_detail(detail1)
        self.db.create_implementation_detail(detail2)
        details = self.db.get_implementation_details()
        self.assertEqual(len(details), 2)
        self.assertDictEqual(details[0], detail1)
        self.assertDictEqual(details[1], detail2)

    def test_create_and_retrieve_coordination_capabilities(self):
        capability1 = {"name": "Scheduling", "description": "Coordinate task scheduling"}
        capability2 = {"name": "Notifications", "description": "Coordinate task notifications"}
        self.db.create_coordination_capability(capability1)
        self.db.create_coordination_capability(capability2)
        capabilities = self.db.get_coordination_capabilities()
        self.assertEqual(len(capabilities), 2)
        self.assertDictEqual(capabilities[0], capability1)
        self.assertDictEqual(capabilities[1], capability2)