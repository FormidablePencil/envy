# System Instructions

## Running Python Scripts

When running Python scripts, use the `py` command instead of `python`. This ensures that the `PYTHONPATH` environment variable is set correctly which is set to `envy` by default.

To run a Python script, use the following command example:

```
py <file>
```

If you need to set the `PYTHONPATH` to a specific directory, you can use the `-p` option:

```
py -p /path/to/directory <file>
```

This will set the `PYTHONPATH` to the specified directory before running the script.

Always remember to run Python scripts from the appropriate current working directory (cwd). The `PYTHONPATH` is relative to the cwd, so running a script from the wrong directory may result in import errors or other issues.

## Running all types of Tests with the `py` Command

The `py` command can also be used to run unit and integration tests. To run all tests (both unit and integration), use the following command:

```
py -t
```

To run only the unit tests, use:

```
py -ut
```

To run only the integration tests, use:

```
py -it
```

## Running associated Tests against functionality files with the `py` Command

To run against a integration test file use:

```
py -it <target_file>
```

To run against a unit test file use:

```
py -ut <target_file>
```

To treat a test as an executable use:

```
py <target_file>
```

To run all tests associated to a functionality file use:

```
py -t <target_file>
```

To run only integration tests associated to a functionality file use:

```
py -it <target_file>
```

To run only unit tests associated to a functionality file use:

```
py -ut <target_file>
```

## Update task.md before resuming
Before resuming and completing a task, always refer to the `task.md` file and update it accordingly to ensure the instructions are up-to-date and aligned with the current project state.

## Handle task conflicts and syncing
Since we're using version control to manage the codebase, it's important to be aware of potential task conflicts and ensure proper syncing between tasks.

### Pulling new changes
When starting a new task or before resuming work, use the `pull_latest_changes()` function from the `components/version_control.py` file to pull the latest changes from the version control system.

### Diffing changes
After pulling the latest changes, use the `diff_changes()` function from the `components/version_control.py` file to compare the changes to your local files.

### Resolving conflicts
If you encounter any conflicts, use the `resolve_conflicts()` function from the `components/version_control.py` file to resolve the issue. Coordinate with other developers to merge the changes and ensure the codebase remains consistent.

### Committing and pushing changes
When you're ready to commit your changes, use the `commit_changes(message)` function from the `components/version_control.py` file to commit the changes with a descriptive message. Then, use the `push_changes()` function to push the committed changes to the remote repository.

## Auto-versioning of Component Libraries
The centralized codebase management system, implemented in `central_codebase.py`, is integrated with the version control component library to automatically handle the versioning of component libraries.

### Adding new components
When adding a new component using the `add_component()` method, the system will automatically:
1. Pull the latest changes from the remote repository.
2. Diff the local changes with the remote.
3. Resolve any conflicts.
4. Commit the new component with a descriptive message.
5. Push the changes to the remote repository.

This ensures that the component libraries are always up-to-date and synchronized across the team.

### Updating existing components
When modifying or updating an existing component, the same auto-versioning process will be triggered, ensuring the changes are properly versioned and pushed to the remote repository.

By using these version control functions and the auto-versioning capabilities, you can streamline the development process and maintain a consistent, synchronized codebase across the team.

## Codebase Refactoring

The codebase has been refactored into a central component library model, with the following structure:

1. AI Automation Component Library
   - Located in the `ai_components` directory
   - Contains components related to AI automation, such as the `code-framework` and `prompt_programming` modules

2. Feature-Specific Component Lrbrary
   - Located in the `feature_components` directory
   - Contains components specific to various features of the application, such as `component_library1`, `component_library2`, and `component_library3`

The `components.json` file in the `/envy` directory provides a centralized mapping of the available components and their respective paths. This file should be referenced when integrating components into the codebase.

## Using the Component Libraries

To use a component from the AI Automation or Feature-Specific libraries, follow these steps:

1. Ensure you have the latest changes from the remote repository by running the following command:

```
git pull
```

2. Locate the desired component in the `components.json` file and note its path.

3. Import and use the component in your code, referencing the path specified in `components.json`. For example:

```python
from ai_components.code_framework import some_ai_function
from feature_components.components.component_library1 import some_feature_function
```

4. If you need to add or update a component, make the necessary changes, then use the auto-versioning functionality provided in the `data_wallet/version_control/auto_versioning.py` file to commit and push the changes to the remote repository.

By following this structure and using the centralized `components.json` file, you can ensure a consistent and maintainable codebase, with clear separation of concerns between AI-related and feature-specific components.