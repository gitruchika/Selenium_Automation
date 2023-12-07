class ReadWriteFiles:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, "r") as file:
            data = file.read()
        return data