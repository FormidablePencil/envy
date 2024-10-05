import unittest
from unittest.mock import patch
from version_control.version_control_manager import VersionControlManager

class TestVersionControlManager(unittest.TestCase):
    def setUp(self):
        self.version_control_manager = VersionControlManager(repo_path='.')

    @patch('version_control.version_control_manager.execute_command')
    def test_pull_latest_changes(self, mock_execute_command):
        self.version_control_manager.pull_latest_changes()
        mock_execute_command.assert_called_with('cd . && git pull')

    @patch('version_control.version_control_manager.execute_command')
    def test_diff_changes(self, mock_execute_command):
        self.version_control_manager.diff_changes('some/directory')
        mock_execute_command.assert_called_with('cd . && git diff some/directory')

    @patch('version_control.version_control_manager.execute_command')
    def test_resolve_conflicts(self, mock_execute_command):
        self.version_control_manager.resolve_conflicts()
        mock_execute_command.assert_called_with('cd . && git mergetool')

    @patch('version_control.version_control_manager.execute_command')
    def test_create_new_branch(self, mock_execute_command):
        self.version_control_manager.create_new_branch('my-new-branch')
        mock_execute_command.assert_called_with('cd . && git checkout -b my-new-branch')

    @patch('version_control.version_control_manager.execute_command')
    def test_commit_all_changes(self, mock_execute_command):
        self.version_control_manager.commit_all_changes('some/directory', 'Commit message')
        mock_execute_command.assert_any_call('cd . && git add some/directory')
        mock_execute_command.assert_any_call("cd . && git commit -m 'Commit message'")

    @patch('version_control.version_control_manager.execute_command')
    def test_push_changes(self, mock_execute_command):
        self.version_control_manager.push_changes('my-new-branch')
        mock_execute_command.assert_called_with('cd . && git push origin my-new-branch')