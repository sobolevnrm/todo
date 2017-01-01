""" Test suite for todo package """
import unittest
import tempfile
import todo
import datetime as dt

_STRING_VARIABLES = {
    "priority" : ["A", "Q", None],
    "date" : [dt.date(2016, 1, 2), dt.date(2017, 3, 2), None],
    "context" : [["bar", "foo"], ["pi", "31451"], ["fnord"], []],
    "title" : ["This is a test todo item"]
}

class TestTodo(unittest.TestCase):
    """ Test todo module functionality """
    def setUp(self):
        """ Set up directories, etc. """
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_objects = []
        for priority in _STRING_VARIABLES["priority"]:
            for date in _STRING_VARIABLES["date"]:
                for contexts in _STRING_VARIABLES["context"]:
                    for title in _STRING_VARIABLES["title"]:
                        item = todo.TodoItem()
                        item.priority = priority
                        item.due_date = date
                        item.contexts = contexts
                        item.title = title
                        self.test_objects.append(item)
    def test_setup(self):
        """ Test setup of package directories, etc. """
        todo.setup_folders(self.temp_dir.name)
    def test_null_title(self):
        """ Test title = None """
        test_item = self.test_objects[0]
        test_item = todo.TodoItem(str(test_item))
        test_item.title = None
        with self.assertRaises(todo.TodoError):
            todo_str = str(test_item)
    def do_test(self, attr):
        """" Test attribute loading from string """
        for item in self.test_objects:
            todo_str = str(item)
            test_item = todo.TodoItem(todo_str)
            item_attr = getattr(item, attr)
            test_attr = getattr(test_item, attr)
            test_message = "Testing %s (%s, %s)" % (attr, item_attr, test_attr)
            self.assertEqual(item_attr, test_attr)
    def test_priority(self):
        """ Test priorities """
        self.do_test("priority")
    def test_dates(self):
        """ Test due dates """
        self.do_test("due_date")
    def test_contexts(self):
        """ Test contexts """
        self.do_test("contexts")
    def test_title(self):
        """ Test title """
        self.do_test("title")
    def tearDown(self):
        self.temp_dir.cleanup()

if __name__ == "__main__":
    unittest.main()