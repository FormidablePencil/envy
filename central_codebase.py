"""Central codebase for reusable components with Git integration."""

import os
import json
import subprocess
from components.version_control import auto_version_directory, pull_latest_changes, diff_changes, resolve_conflicts, commit_changes, push_changes

class ReusableComponentManager:
    """Manages reusable code components with Git integration."""

    def __init__(self, base_dir):
        """Initializes ReusableComponentManager with the base directory."""
        self.base_dir = base_dir
        self.components = {}
        self.load_components()

    def load_components(self):
        """Loads components from JSON configuration."""
        config_path = os.path.join(self.base_dir, "components.json")
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                self.components = json.load(f)

    def add_component(self, name, path):
        """Adds a new component to the manager and commits it to Git."""
        self.components[name] = path
        self.save_components()
        auto_version_directory(self.base_dir)

    def get_component(self, name):
        """Retrieves a component by name."""
        return self.components.get(name)

    def save_components(self):
        """Saves components to JSON configuration and commits it to Git."""
        config_path = os.path.join(self.base_dir, "components.json")
        with open(config_path, "w") as f:
            json.dump(self.components, f, indent=4)
        auto_version_directory(self.base_dir)

    def list_components(self):
        """Lists all available components."""
        return list(self.components.keys())


# Example usage:
base_dir = "./components"

if not os.path.exists(base_dir):
    os.makedirs(base_dir)
    subprocess.run(["git", "init"], check=True, cwd=base_dir)

manager = ReusableComponentManager(base_dir)

# Pull the latest changes before adding a new component
pull_latest_changes(base_dir)
diff_changes(base_dir)
resolve_conflicts()

manager.add_component("my_component", "./components/my_component.py")

# Commit and push the changes
commit_changes(base_dir, "Add new component")
push_changes(base_dir)

print(manager.list_components())

print(manager.get_component("my_component"))

# Add more components as needed
