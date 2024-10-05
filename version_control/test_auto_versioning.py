from .git_operations import (
    pull_latest_changes,
    diff_changes,
    resolve_conflicts,
    create_new_branch,
    commit_all_changes,
    push_changes
)
from .auto_versioning import auto_version_hello_world

def test_auto_versioning():
    try:
        pull_latest_changes()
    except subprocess.CalledProcessError as e:
        print("Error pulling latest changes. Skipping this step.")
    
    diff_changes()
    resolve_conflicts()

    # Create a new branch for the changes
    branch_name = "test-auto-versioned"
    create_new_branch(branch_name)

    commit_all_changes("Testing auto-versioned changes")
    try:
        push_changes(branch_name)
        print(f"Successfully pushed changes to branch: {branch_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes to branch: {branch_name}")

    auto_version_hello_world()

if __name__ == "__main__":
    test_auto_versioning()