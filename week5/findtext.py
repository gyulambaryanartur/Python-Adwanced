import os


class Search:
    def __init__(self, path: str, isnested: bool):
        self.path = path
        self.isnested = isnested
        self.matches=""

    def run(self, string):
        if os.path.isdir(self.path):
            for file in os.listdir(self.path):
                if os.path.isdir(file) and self.isnested == True:
                    self.path += "\\" + file
                    self.run(string)
                    print(os.path.isdir(file))
                if file.endswith(".py"):
                    with open(os.path.join(self.path, file)) as fl:
                        for line in enumerate(fl):
                            if string in line[1]:

                                self.matches += f'File path which matched with string is: {os.path.join(self.path, file)} line is:  {line[0]} content is: {line[1]}\n'
        elif self.path.endswith(".py"):
            with open(os.path.join(self.path, file)) as fl:
                for line in enumerate(fl):
                    if string in line[1]:
                        self.matches += f'File path which matched with string is: {os.path.join(self.path, file)} line is:  {line[0]} content is: {line[1]}\n'
        return self.matches[:-1]


if __name__ == "__main__":
    serches = Search("C:\\Users\\Home\\Desktop\\Adwnaced Python", 1)

    # serches = Search(os.getcwd(), 1)
    print(serches.run('os.path'))
