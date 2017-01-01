""" Organize tasks """
import datetime as dt
import os.path
import os
import re

PRIORITY_RE = re.compile("\(([a-zA-Z])\)")
DATE_RE = re.compile("([0-9]{4})-([0-9]{2})-([0-9]{2})")

TODAY = dt.date.today()
_DATA_PATH = "data"
_OTHER_FOLDERS = ["completed", "inbox"]

def setup_folders(path):
    """ Set up folders for tasks in directory specified by path """
    folder_list = [folder for folder in _OTHER_FOLDERS]
    # Date folders
    one_day = dt.timedelta(days=1)
    date = TODAY
    for _ in range(366):
        month = date.strftime("%m")
        day = date.strftime("%d")
        folder = os.path.join(path, month, day)
        folder_list.append(folder)
        date = date + one_day
    # Other folders
    for folder in folder_list:
        os.makedirs(name=folder, exist_ok=True)

class TodoItem:
    """ A todo item """
    def __init__(self, todo_str=None):
        """ Set up todo item with an optional todo string """
        self.priority = None
        self.contexts = []
        self.due_date = None
        self.completed = False
        self.contents = None
        self.todo_str = None
        if todo_str:
            self.parse_todo_str(todo_str)
    def parse_todo_str(self, todo_str):
        """ Parse a todo item formatted as a string """
        match = PRIORITY_RE.search(todo_str)
        try:
            self.priority = match.expand("\g<1>").upper()
        except AttributeError:
            self.priority = None
        try:
            match = DATE_RE.search(todo_str)
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            self.due_date = dt.date(year, month, day)
        except AttributeError:
            self.due_date = None




if __name__ == "__main__":
    print(TODAY.year)
    print(type(TODAY))
    setup_folders(_DATA_PATH)