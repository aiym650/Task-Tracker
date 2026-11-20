class TaskTracker:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {"id": self.next_id, "title": title, "completed": False}

        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True

        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True

        return False


if __name__ == "__main__":
    tracker = TaskTracker()

    tracker.add_task("Learn Python")
    tracker.add_task("Complete assignment")

    print("My tasks:")

    for task in tracker.get_tasks():
        status = "Done" if task["completed"] else "Not completed"
        print(f'{task["id"]}. {task["title"]} - {status}')
