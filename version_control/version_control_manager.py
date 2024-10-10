import os
import uuid
import subprocess
from utils.utils import execute_command, log_message

class VersionControlManager:
    def __init__(self, repo_path='.'):
        self.repo_path = repo_path

    def pull_latest_changes(self):
        """
        Pull the latest changes from the remote repository.
        """
        try:
            execute_command(f"cd {self.repo_path} && git pull")
        except subprocess.CalledProcessError as e:
            log_message("Error pulling latest changes. Attempting to set upstream branch...", logging.ERROR)
            current_branch = execute_command(f"cd {self.repo_path} && git rev-parse --abbrev-ref HEAD").strip()
            try:
                execute_command(f"cd {self.repo_path} && git branch --set-upstream-to=origin/{current_branch} {current_branch}")
                execute_command(f"cd {self.repo_path} && git pull")
            except subprocess.CalledProcessError as e2:
                log_message(f"Error setting upstream branch: {e2}", logging.ERROR)

    def diff_changes(self, directory_to_version):
        """
        Diff the local changes in the specified directory with the remote changes.
        """
        try:
            execute_command(f"cd {self.repo_path} && git diff {directory_to_version}")
        except subprocess.CalledProcessError as e:
            log_message("Error diffing changes. Skipping this step.", logging.WARNING)

    def resolve_conflicts(self):
        """
        Resolve any conflicts between the local and remote changes.
        """
        try:
            execute_command(f"cd {self.repo_path} && git mergetool")
        except subprocess.CalledProcessError as e:
            log_message("No merge tool configured. Skipping conflict resolution.", logging.WARNING)

    def create_new_branch(self, branch_name=None):
        """
        Create a new branch with the specified name.
        """
        if not branch_name:
            branch_name = f"feature/unnamed-{uuid.uuid4().hex[:6]}"
        execute_command(f"cd {self.repo_path} && git checkout -b {branch_name}")
        log_message(f"Checked out new branch: {branch_name}")

    def commit_all_changes(self, directory_to_version, message):
        """
        Commit all changes in the specified directory.
        """
        try:
            execute_command(f"cd {self.repo_path} && git add {directory_to_version}")
            execute_command(f"cd {self.repo_path} && git commit -m '{message}'")
        except subprocess.CalledProcessError as e:
            log_message(f"Error committing changes: {e}", logging.ERROR)

    def push_changes(self, branch_name):
        """
        Push the committed changes to the remote repository.
        """
        try:
            execute_command(f"cd {self.repo_path} && git push origin {branch_name}")
        except subprocess.CalledProcessError as e:
            log_message(f"Error pushing changes: {e}", logging.ERROR)