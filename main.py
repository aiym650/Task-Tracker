from task_tracker import TaskTracker


def main():
    tracker = TaskTracker()

    tracker.add_task("Learn Python")
    tracker.add_task("Complete assignment")

    print("My tasks:")

    for task in tracker.get_tasks():
        status = "Done" if task["completed"] else "Not completed"
        print(f'{task["id"]}. {task["title"]} - {status}')


if __name__ == "__main__":
    main()
