# Task Track CLI

Task tracker is a project used to track and manage your tasks. A simple command line interface (CLI) is built to track what you need to do, what you have done, and what you are currently working on.

## Features

- Add a new task.
- Update a task description.
- Delete a task.
- Mark a task as in progress, done or todo.
- List all tasks.
- List tasks that are done, to done, in progress or todo.

## Required

- python is needed to run this application.
- git is needed to download this application.

## Install

Use git to download this repo.

        git clone https://github.com/wingforth/task-tracker-cli.git

## Usage

1. First start task-cli:  

        python task_cli.py

2. Than you can take following action on tasks.

    - Add a task:

            add <description>

    - Update a task description:

            update <id> <description>

    - Delete a task:

            delete <id>

    - Mark a task on a status (todo, in-progress, done):

            mark <id> <status>

    - List all task:

            list

    - List task that on a status (todo, in-progress, done, not-done):

            list <status>

3. At last exit task-cli:

        exit

    Or input **end-of-file** (EOF) by pressing **Ctrl-D** (Unix or Linux) or **Ctrl-Z** (Windows).

## Project

This is a project from [Roadmap](https://roadmap.sh). For more information, please visit [Task Tracker](https://roadmap.sh/projects/task-tracker).
