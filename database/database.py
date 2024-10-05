import sqlite3
from typing import List, Dict

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS implementation_details
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, component TEXT, description TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS completion_records
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER, completed_at TEXT, related_tasks TEXT, impact_notes TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS coordination_capabilities
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)''')
        self.conn.commit()

    def create_task(self, task: Dict) -> int:
        self.cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (task['title'], task['description']))
        task_id = self.cursor.lastrowid
        self.conn.commit()
        return task_id

    def get_tasks(self) -> List[Dict]:
        self.cursor.execute("SELECT * FROM tasks")
        tasks = [{'id': row[0], 'title': row[1], 'description': row[2]} for row in self.cursor.fetchall()]
        return tasks

    def create_implementation_detail(self, detail: Dict) -> None:
        self.cursor.execute("INSERT INTO implementation_details (component, description) VALUES (?, ?)", (detail['component'], detail['description']))
        self.conn.commit()

    def get_implementation_details(self) -> List[Dict]:
        self.cursor.execute("SELECT * FROM implementation_details")
        details = [{'id': row[0], 'component': row[1], 'description': row[2]} for row in self.cursor.fetchall()]
        return details

    def create_completion_record(self, task_id: int, completed_at: str, related_tasks: str, impact_notes: str) -> None:
        self.cursor.execute("INSERT INTO completion_records (task_id, completed_at, related_tasks, impact_notes) VALUES (?, ?, ?, ?)", (task_id, completed_at, related_tasks, impact_notes))
        self.conn.commit()

    def get_completion_records(self) -> List[Dict]:
        self.cursor.execute("SELECT * FROM completion_records")
        records = [{'id': row[0], 'task_id': row[1], 'completed_at': row[2], 'related_tasks': row[3], 'impact_notes': row[4]} for row in self.cursor.fetchall()]
        return records

    def create_coordination_capability(self, capability: Dict) -> None:
        self.cursor.execute("INSERT INTO coordination_capabilities (name, description) VALUES (?, ?)", (capability['name'], capability['description']))
        self.conn.commit()

    def get_coordination_capabilities(self) -> List[Dict]:
        self.cursor.execute("SELECT * FROM coordination_capabilities")
        capabilities = [{'id': row[0], 'name': row[1], 'description': row[2]} for row in self.cursor.fetchall()]
        return capabilities

    def commit_task(self, task: Dict, completed_at: str, related_tasks: str, impact_notes: str) -> int:
        self.conn.execute("BEGIN TRANSACTION")
        try:
            task_id = self.create_task(task)
            self.create_completion_record(task_id, completed_at, related_tasks, impact_notes)
            self.conn.commit()
            return task_id
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e