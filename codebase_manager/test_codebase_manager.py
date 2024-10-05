import unittest
from unittest.mock import patch, mock_open
from codebase_manager import CodebaseManager

class TestCodebaseManager(unittest.TestCase):
    def setUp(self):
        self.test_repo_dir = 'test_repo'
        os.makedirs(self.test_repo_dir, exist_ok=True)
        os.chdir(self.test_repo_dir)
        subprocess.run(['git', 'init'], check=True)

    def tearDown(self):
        os.chdir('..')
        shutil.rmtree(self.test_repo_dir)

    @patch('codebase_manager.execute_command')
    def test_checkout_new_branch(self, mock_execute_command):
        codebase_manager = CodebaseManager()
        codebase_manager.checkout_new_branch()
        mock_execute_command.assert_called_with(['git', 'checkout', '-b', codebase_manager.branch_name])
        self.assertIsNotNone(codebase_manager.branch_name)

    @patch('codebase_manager.execute_command')
    def test_pull_latest_changes(self, mock_execute_command):
        codebase_manager = CodebaseManager()
        codebase_manager.pull_latest_changes()
        mock_execute_command.assert_called_with(['git', 'pull'])

    @patch('codebase_manager.execute_command')
    @patch('builtins.input', return_value='Test Commit')
    def test_commit_and_push_changes(self, mock_input, mock_execute_command):
        codebase_manager = CodebaseManager()
        codebase_manager.commit_and_push_changes()
        mock_execute_command.assert_any_call(['git', 'add', '.'])
        mock_execute_command.assert_any_call(['git', 'commit', '-m', 'Test Commit'])
        mock_execute_command.assert_called_with(['git', 'push'])

    @patch('codebase_manager.execute_command')
    def test_merge_changes(self, mock_execute_command):
        codebase_manager = CodebaseManager()
        codebase_manager.branch_name = 'test-branch'
        codebase_manager.merge_changes()
        mock_execute_command.assert_any_call(['git', 'checkout', 'main'])
        mock_execute_command.assert_called_with(['git', 'merge', 'test-branch'])

    @patch('builtins.open', mock_open())
    @patch('codebase_manager.datetime')
    def test_record_progress_reflection(self, mock_datetime):
        mock_datetime.now.return_value = datetime.datetime(2023, 4, 20, 12, 0, 0)
        codebase_manager = CodebaseManager()
        codebase_manager.record_progress_reflection()
        mock_open.assert_called_with('progress_reflection.md', 'a')
        mock_open().write.assert_called_with('# Progress Reflection - 2023-04-20 12:00:00\n\n\n\n')

    @patch('codebase_manager.openai.Completion.create')
    def test_generate_code(self, mock_openai_create):
        mock_openai_create.return_value.choices = [{'text': 'Generated code'}]
        codebase_manager = CodebaseManager()
        generated_code = codebase_manager.generate_code('test prompt')
        self.assertEqual(generated_code, 'Generated code')

    def test_codebase_management_workflow(self):
        codebase_manager = CodebaseManager()
        codebase_manager.checkout_new_branch()
        codebase_manager.pull_latest_changes()
        codebase_manager.commit_and_push_changes()
        codebase_manager.merge_changes()
        codebase_manager.record_progress_reflection()

        # Verify the state of the Git repository
        self.assertEqual(subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True).stdout.strip(), 'main')
        self.assertTrue(os.path.exists('progress_reflection.md'))

if __name__ == '__main__':
    unittest.main()