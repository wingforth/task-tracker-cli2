# -*- coding: utf-8 -*-
"""
A simple CLI application used to track and manage your tasks.
    Example:
    python task_cli.py
    task_cli> add "A new task"
    task_cli> update 1 "New description"
    task_cli> mark 1 in-progress
    task_cli> mark 1 done
    task_cli> mark 1 todo
    task_cli> list
    task_cli> list todo
    task_cli> list in-progress
    task_cli> list done
    task_cli> list not-done
    task_cli> delete 1
"""

from cmd import Cmd
from pathlib import Path
from task_tracker.task_tracker import TaskTracker


class TackCLI(Cmd):
    """A simple CLI for task tracker."""

    intro = 'Task tracker is a simple CLI application used to track and manage your tasks.\nType "help" for more information.'
    prompt = "task-cli> "

    def __init__(self) -> None:
        super().__init__()
        self.task_tracker = TaskTracker(Path(__file__).parent.joinpath("tasks.json"))
        self.task_tracker.load()

    @staticmethod
    def remove_quote(s: str) -> str:
        """
        If the string is enclosed with a pair of quotes (" or '),
        delete the quotes first, and then remove the leading and trailing whitespaces.
        For example, if s is "'       hello  world   '", than return "helo world".
        """
        if len(s) >= 2 and s[0] in ('"', "'") and s[0] == s[-1]:
            return s[1:-1].strip()
        return s

    def do_add(self, line: str) -> None:
        """
        Usage: add <description>

        Add a new task.
        """
        if not line:
            print("task-cli: 'description' is required.")
            return
        if line in ("-h", "--help"):
            self.do_help("add")
            return
        if id := self.task_tracker.add(self.remove_quote(line)):
            print(f"Task added successfully (ID: {id})")

    def do_update(self, line: str) -> None:
        """
        Usage: update <id> <description>

        Update the task description by ID.
        """
        if not line:
            print("task-cli: 'id' and 'description' are required.")
            return
        if line in ("-h", "--help"):
            self.do_help("update")
            return
        id, *description = line.split(maxsplit=1)
        if not description:
            print("task-cli: 'description' is required.")
            return
        self.task_tracker.update(id, self.remove_quote(description[0]))

    def do_delete(self, line: str) -> None:
        """
        Usage: delete <id>

        Delete a task by ID.
        """
        if not line:
            print("task-cli: 'id' is required.")
            return
        if line in ("-h", "--help"):
            self.do_help("delete")
            return
        self.task_tracker.delete(line)

    def do_mark(self, line: str) -> None:
        """
        Usage: mark <id> {"todo" | "in-progress" | "done"}

        Mark a task as todo, in progress or done by ID.
        """
        if not line:
            print("task-cli: 'id' and 'status' are required.")
            return
        if line in ("-h", "--help"):
            self.do_help("mark")
            return
        id, *status = line.split(maxsplit=1)
        if not status:
            print("task-cli: 'status' is required.")
            return
        self.task_tracker.mark_status(id, str.lower(status[0]))

    def do_list(self, line: str) -> None:
        """
        Usage: list [{"todo" | "in-progress" | "done" | "not-done"}]

        List all tasks or list tasks by status.
        """
        if line in ("-h", "--help"):
            self.do_help("list")
            return
        tasks = self.task_tracker.list_by_status(str.lower(line))
        if tasks is None:
            return
        if line == "":
            print("All tasks\n")
        else:
            print("All tasks that are", *line.split("-"), "\n")

        task_format = r"{:5}{:21}{:21}{:13}{}"
        # print head of task list.
        print(task_format.format(*TaskTracker.task_properties))
        print(
            task_format.format(
                *("-" * n for n in map(len, TaskTracker.task_properties))
            ),
        )
        for task in tasks:
            print(task_format.format(*task))
        print()

    def do_exit(self, line: str) -> bool:
        """
        Usage: exit

        Exit task tracker cli.
        """
        self.task_tracker.save()
        return True

    def do_EOF(self, line: str) -> bool:
        """Exit task tracker cli by pressing Ctrl-D (Unix or Linux) or Ctrl-Z (Windows)."""
        self.task_tracker.save()
        return True

    def default(self, line: str) -> None:
        cmd, *_ = line.partition(" ")
        print(f"task-cli: '{cmd}' is not a task-cli command. See 'help'.")

    def emptyline(self) -> None:
        pass


if __name__ == "__main__":
    TackCLI().cmdloop()
