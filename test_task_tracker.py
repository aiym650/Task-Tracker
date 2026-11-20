import unittest
from task_tracker import TaskTracker


class TestTaskTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = TaskTracker()

    def test_add_task(self):
        task = self.tracker.add_task("Learn Python")

        self.assertEqual(task["title"], "Learn Python")
        self.assertFalse(task["completed"])

    def test_get_tasks(self):
        self.tracker.add_task("Task 1")

        self.assertEqual(len(self.tracker.get_tasks()), 1)

    def test_complete_task(self):
        task = self.tracker.add_task("Task 1")

        result = self.tracker.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        task = self.tracker.add_task("Task 1")

        result = self.tracker.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.tracker.get_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
