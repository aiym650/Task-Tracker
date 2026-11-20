
# AGENTS.md

## 1. Project Purpose

Task Tracker is a simple Python application for managing tasks.
Users can add, view, complete, and delete tasks.

## 2. Project Structure

- main.py - application entry point.
- task_tracker.py - TaskTracker class and business logic.
- test_task_tracker.py - automated unit tests.
- AGENTS.md - instructions for AI coding assistants.
- .gitignore - files excluded from Git.

## 3. Setup

Requirements:
- Python 3.15 or compatible Python 3 version.
- No external dependencies are required.

Run the application:

```bash
python main.py
```

Run tests:

```bash
python -m unittest -v
```

## 4. Coding Conventions

- Use simple and readable Python code.
- Follow PEP 8 style guidelines.
- Use descriptive names for classes, methods, and variables.
- Keep methods small and focused.
- Add tests when new functionality is introduced.

## 5. Architecture

- TaskTracker is the main class.
- Tasks are stored in a Python list.
- Each task contains an ID, title, and completion status.
- Unit tests use Python's built-in unittest framework.

## 6. Safe Commands

Allowed:
- python main.py
- python -m unittest -v
- git status
- git diff
- git log

## 7. Forbidden Actions

AI assistants must not:
- Add passwords, API keys, or other secrets.
- Execute destructive commands without approval.
- Deploy the application to production.
- Install or update dependencies without approval.
- Delete project files without approval.
- Commit or push changes without user approval.

## 8. Testing Expectations

- Run all unit tests after code changes.
- Do not claim tests pass without executing them.
- Review the code changes before accepting them.
- Preserve existing application behavior.

## 9. Acceptance Criteria

AC1: Users can add a task.

AC2: Users can view all tasks.

AC3: Users can mark a task as completed.

AC4: Users can delete a task.

AC5: All automated tests must pass.
