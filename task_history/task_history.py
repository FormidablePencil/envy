import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.database import Database

class TaskHistory:
    def __init__(self, database: Database):
        self.database = database

    def get_task_history(self, user_id: str) -> list:
        """
        Retrieves the task history for the specified user.
        
        Args:
            user_id (str): The ID of the user to retrieve task history for.
        
        Returns:
            list: A list of tasks for the user.
        """
        return self.database.get_task_history(user_id)

    def add_task(self, user_id: str, task_description: str):
        """
        Adds a new task to the database for the specified user.
        
        Args:
            user_id (str): The ID of the user to add the task for.
            task_description (str): The description of the task.
        """
        self.database.add_task(user_id, task_description)