import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.database import Database

class ChatHistory:
    def __init__(self, database: Database):
        self.database = database

    def get_chat_history(self, user_id: str) -> list:
        """
        Retrieves the chat history for the specified user.
        
        Args:
            user_id (str): The ID of the user to retrieve chat history for.
        
        Returns:
            list: A list of chat messages for the user.
        """
        return self.database.get_chat_history(user_id)

    def add_chat_message(self, user_id: str, message: str):
        """
        Adds a new chat message to the database for the specified user.
        
        Args:
            user_id (str): The ID of the user to add the chat message for.
            message (str): The content of the chat message.
        """
        self.database.add_chat_message(user_id, message)