# AI-Powered Codebase Infrastructure

This project provides an AI-powered codebase infrastructure with a database for storing and managing tasks, implementation details, completion records, and coordination capabilities.

## Database CLI

The database functionality is accessible through a command-line interface (CLI) implemented in the `database_cli.py` file.

### Usage

To use the database CLI, run the following command:

```
py database/database_cli.py [COMMAND] [OPTIONS]
```

Available commands:

- `tasks`
  - `--create TITLE DESCRIPTION`: Create a new task
  - `--list`: List all tasks
- `details`
  - `--create COMPONENT DESCRIPTION`: Create a new implementation detail
  - `--list`: List all implementation details
- `records`
  - `--create TASK_ID COMPLETED_AT`: Create a new completion record
  - `--list`: List all completion records
- `capabilities`
  - `--create NAME DESCRIPTION`: Create a new coordination capability
  - `--list`: List all coordination capabilities

Examples:

```
# Create a new task
py database/database_cli.py tasks --create "Implement login feature" "Add login functionality to the app"

# List all tasks
py database/database_cli.py tasks --list

# Create a new implementation detail
py database/database_cli.py details --create "UI" "Implement button styling"

# List all implementation details
py database/database_cli.py details --list

# Create a new completion record
py database/database_cli.py records --create 1 "2023-04-15"

# List all completion records
py database/database_cli.py records --list

# Create a new coordination capability
py database/database_cli.py capabilities --create "Scheduling" "Coordinate task scheduling"

# List all coordination capabilities
py database/database_cli.py capabilities --list
```

## Testing

The project includes both unit and integration tests for the `Database` class. You can run the tests using the following commands:

```
# Run all tests
py -t

# Run only unit tests
py -ut

# Run only integration tests
py -it
```

Feel free to explore and extend the database functionality as needed for your AI-powered codebase infrastructure project.
