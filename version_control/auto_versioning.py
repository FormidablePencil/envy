import json
from datetime import datetime
import subprocess
import sys
import os
from envy.utils import log_message
from envy.version_control_manager import VersionControlManager

def auto_version_directory(directory_to_version):
    """
    Automatically handle version control tasks for the specified directory.
    """
    version_control_manager = VersionControlManager(directory_to_version)

    try:
        version_control_manager.pull_latest_changes()
    except subprocess.CalledProcessError as e:
        log_message("Error pulling latest changes. Skipping this step.", logging.ERROR)
    
    version_control_manager.diff_changes(directory_to_version)
    version_control_manager.resolve_conflicts()

    # Create a new branch for the changes
    branch_name = f"auto-versioned-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    version_control_manager.create_new_branch(branch_name)

    version_control_manager.commit_all_changes(directory_to_version, f"Auto-versioned changes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        version_control_manager.push_changes(branch_name)
        log_message(f"Successfully pushed changes to branch: {branch_name}", logging.INFO)
    except subprocess.CalledProcessError as e:
        log_message(f"Error pushing changes to branch: {branch_name}", logging.ERROR)


def main():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            for project in config['projects']:
                auto_version_directory(project)
    except FileNotFoundError:
        log_message("config.json not found.", logging.ERROR)
    except json.JSONDecodeError:
        log_message("Invalid JSON in config.json", logging.ERROR)
    except Exception as e:
        log_message(f"An error occurred: {e}", logging.ERROR)

if __name__ == "__main__":
    main()