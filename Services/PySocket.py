class createSocket:
    def __init__(self, socket):
        self.socket = socket
class listen(createSocket):
    listening = {}
    def __init__(self, socket):
        super().__init__(socket)
        self.listening[socket] = True

    def __enter__(self):
        print("Entering listen process")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting listening")
        self.close()

    def __getitem__(self, item):
        return self.listening[item]

    def __delitem__(self, key):
        del self.listening[key]
        return self.listening

    def close(self):
        listening = {}
        del self

class send(createSocket):
    listening = False
    def __init__(self, socket, content = None):
        super().__init__(socket)
        self.listenService = listen(self.socket)
        if self.listenService.listening[socket] is True:
            self.listening = True
        self.content = content

    def __call__(self, content):
        if self.listening:
            self.content = content
            return self.content
    def __get__(self, socket):
        if self.listenService[socket] is None:
            return False
        return self.listenService[socket]

    def __enter__(self):
        print("Sending Process starting")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing Process")
        self.listening = False
        self.content = None
        self.close()

    def __str__(self):
        return self.content

    def encode(self, method):
        if self.listening:
            content = self.content
            self.content = content.encode(method)
            return self.content

    def force(self, to):
        if self.listening:
            if to == "int":
                self.content = int(self.content)
                return int(self.content)

            elif to == "str":
                self.content = str(self.content)
                return str(self.content)

            elif to == "float":
                self.content = float(self.content)
                return float(self.content)

    def also_do(self, method, cause = None):
        if self.listening:
            if method == "stop":
                self.content = None
                del self

            elif method == "force":
                return self.force(cause)

    def log(self):
        if self.listening:
            print(self.content)
            return self.content

    def file_log(self, filename):
        try:
            with open(filename, "a") as f:
                f.write(self.content)
            with open(filename, "r") as f:
                print(f.read())
            return True
        except Exception:
            raise Exception("Failed: service file_handler -> error in file_log")
        finally:
            return self.content

    def close(self):
        self.listenService.close()
        del self
