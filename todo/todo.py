""" Organize tasks """
import datetime as dt
import os.path
import os
import re

PRIORITY_RE = re.compile("\(([a-zA-Z])\) *")
DATE_RE = re.compile("([0-9]{4})-([0-9]{2})-([0-9]{2}) *")
CONTEXTS_RE = re.compile("(@.*)")

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
        folder = os.path.join(month, day)
        folder_list.append(folder)
        date = date + one_day
    # Other folders
    for folder in folder_list:
        folder_path = os.path.join(path, folder)
        os.makedirs(name=folder_path, exist_ok=True)

class TodoError(Exception):
    """ Error for Todo class """
    pass

class TodoItem:
    """ A todo item """
    def __init__(self, todo_str=None):
        """ Set up todo item with an optional todo string """
        self.title = None
        self.priority = None
        self.contexts = []
        self.due_date = None
        self.completed = False
        self.contents = None
        self.todo_str = None
        if todo_str:
            self.parse_todo_str(todo_str)
    def __str__(self):
        """ Return the todo string for this item """
        strings = []
        if self.completed:
            strings.append("x")
        if self.priority:
            strings.append("({})".format(self.priority))
        if self.due_date:
            strings.append("{}".format(self.due_date.strftime("%Y-%m-%d")))
        if self.title:
            strings.append(self.title)
        else:
            errstr = "Todo item is missing title!"
            raise TodoError(errstr)
        for context in self.contexts:
            strings.append("@" + context)
        return " ".join(strings)
    def parse_todo_str(self, todo_str):
        """ Parse a todo item formatted as a string """
        self.todo_str = todo_str
        _str = todo_str
        match = PRIORITY_RE.search(_str)
        try:
            self.priority = match.expand("\g<1>").upper()
            span = match.span()
            _str = _str[span[1]:]
        except AttributeError:
            self.priority = None
        try:
            match = DATE_RE.search(_str)
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            self.due_date = dt.date(year, month, day)
            span = match.span()
            _str = _str[span[1]:]
        except AttributeError:
            self.due_date = None
        try:
            match = CONTEXTS_RE.search(_str)
            span = match.span()
            self.title = _str[:span[0]].strip()
            contexts = match.group(1)
            for context in contexts.split("@"):
                context = context.strip()
                if context:
                    self.contexts.append(context)
        except AttributeError:
            self.title = _str.strip()
            _str = ""


if __name__ == "__main__":
    print(TODAY.year)
    print(type(TODAY))
    setup_folders(_DATA_PATH)