from central_ai_manager.core import CentralAIManager

def generate_code_from_anywhere(task: dict):
    """Generates code from anywhere using the CentralAIManager."""
    central_ai_manager = CentralAIManager()
    file_path = central_ai_manager.generate_from_anywhere(task)
    return file_path

def apply_changes_from_anywhere(file_path: str):
    """Applies changes from anywhere using the CentralAIManager."""
    central_ai_manager = CentralAIManager()
    central_ai_manager.apply_changes_from_anywhere(file_path)