""" Test suite for todo package """
import unittest
import tempfile
import todo
import datetime as dt

_TEST_GOOD_STRING = "(A) 2017-03-02 This string is good @better @best @great"
_TEST_BAD_STRING = "This string is bad"

class TestTodo(unittest.TestCase):
    """ Test todo module functionality """
    def setUp(self):
        """ Set up directories, etc. """
        self.temp_dir = tempfile.TemporaryDirectory()
        self.good_item = todo.TodoItem(_TEST_GOOD_STRING)
        self.bad_item = todo.TodoItem(_TEST_BAD_STRING)
    def test_setup(self):
        """ Test setup of package directories, etc. """
        todo.setup_folders(self.temp_dir.name)
    def test_todo_str(self):
        """ Test extraction of features from a todo string """
        self.assertEqual(self.good_item.priority, "A", msg="Checking priority")
        self.assertIsNone(self.bad_item.priority, msg="Checking priority")
        self.assertEqual(self.good_item.due_date, dt.date(2017, 3, 2), msg="Checking due date")
        self.assertIsNone(self.bad_item.priority, msg="Checking due date")
    def tearDown(self):
        self.temp_dir.cleanup()

if __name__ == "__main__":
    unittest.main()