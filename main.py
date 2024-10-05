import os
from utils import execute_command, log_message
from version_control import create_new_branch, commit_all_changes, push_changes, auto_version_control, add_git_tracked_directories

def main():
    print("Welcome to the AI-powered codebase infrastructure!")
    
    # Initialize Git repository
    execute_command("git init .")
    execute_command("git config core.excludesfile /etc/gitignore")
    execute_command("echo '*' > /etc/gitignore")
    
    # Create a new branch
    branch_name = "feature/auto-versioning"
    create_new_branch(branch_name)
    
    # Automatically add Git-tracked subdirectories
    add_git_tracked_directories()
    
    # Automatically handle version control tasks
    auto_version_control()
    
    print("Initial setup complete. You can now start building your AI-powered codebase infrastructure.")

if __name__ == "__main__":
    main()