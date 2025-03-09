
from typing import Any


class dataconnect:
    connected = False
    database = None
    keywords = None

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.connected = True
        self.database = {}
        self.keywords = {}

    def __str__(self):
        return str(self.database) + f"keywords: {self.keywords}"

    def __repr__(self):
        if self.database is not None and self.keywords is not None:
            return f">> repr start --\n database: {self.database},\n keywords: {self.keywords},\n total length: {len(self)}\n>> repr end --"

    def __contains__(self, item) -> bool:
        for i in self.database:
            if item == i:
                return True
        for i in self.keywords:
            if item == i:
                return True
        return False

    def __len__(self) -> int:
        return len(self.database) + len(self.keywords)

    """
        Custom Methods:
    """

    def append(self, kname: str, content) -> Any:
        if self.database is None:
            self.database = {}
        self.database[kname] = content

    def point(self, keywords: str, kname: str):
        self.keywords[keywords] = self.database[kname]

    def catch(self, keyword):
        return self.keywords[keyword]

    def read(self, kname: str):
        return self.database[kname]

    def log(self, kname: str):
        print(self.read(kname))
        return self.read(kname)

    def catchLog(self, keyword: str):
        print(self.catch(keyword))
        return self.catch(keyword)

    def change_content(self, kname, new_content):
        self.database[kname] = new_content
        return "result: " + str(self.database)

    def change_key(self, kname: str, new_name: str):
        self.database[new_name] = self.database[kname]
        del self.database[kname]
        return "result: " + str(self.database)

    def change_pointer(self, old_pointer, new_pointer):
        self.keywords[new_pointer] = self.keywords[old_pointer]
        del self.keywords[old_pointer]
        return "result: " + str(self.keywords)

    def __enter__(self) -> Any:
        if self.connected:
            print("\nprocess << data init-- .force")
            print("Process Connect: Running Data")
            return self
        else:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb) -> Any:
        print("Process Connect: Closing Process")
        print("<< data out-- .close\n")
        self.database = None
        self.keywords = None
        self.connected = False
        return self
