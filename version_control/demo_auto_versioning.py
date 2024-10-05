import os
from datetime import datetime
from git_operations import (
    pull_latest_changes,
    diff_changes,
    resolve_conflicts,
    create_new_branch,
    commit_all_changes,
    push_changes
)

def demo_auto_version_hello_world():
    """
    Demonstrate the automatic versioning process for the envy/hello_world directory.
    """
    try:
        pull_latest_changes()
    except subprocess.CalledProcessError as e:
        print("Error pulling latest changes. Skipping this step.")
    
    diff_changes()
    resolve_conflicts()

    # Create a new branch for the changes
    branch_name = f"auto-versioned-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    create_new_branch(branch_name)

    # Simulate some changes to the envy/hello_world directory
    os.makedirs("envy/hello_world/new_feature", exist_ok=True)
    with open("envy/hello_world/new_feature/test.py", "w") as f:
        f.write("# New feature code")

    commit_all_changes(f"Auto-versioned changes at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        push_changes(branch_name)
        print(f"Successfully pushed changes to branch: {branch_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes to branch: {branch_name}")

if __name__ == "__main__":
    demo_auto_version_hello_world()