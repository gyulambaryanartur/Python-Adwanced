import os


class Search:
    def __init__(self, path: str, isnested: bool):
        self.path = path
        self.isnested = isnested
        self.matches = ""

    def __readfile(self, file: str,string :str):
        with open(os.path.join(self.path, file)) as fl:
            for line in enumerate(fl):
                if string in line[1]:

                    self.matches += f'File path which matched with string is: {os.path.join(self.path, file)} line is:  {line[0]} content is: {line[1]}\n'

    def run(self, string):
        if os.path.isdir(self.path):
            for file in os.listdir(self.path):
                if not os.path.isdir(os.path.join(self.path, file)) and file.endswith(".py"):
                    self.__readfile(file,string)

            for file in os.listdir(self.path):
                if os.path.isdir(os.path.join(self.path, file)) and self.isnested == True:
                    self.path += f"\\{file}"
                    self.run(string)

        elif self.path.endswith(".py"):
            self.__readfile(file,string)

        return self.matches[:-1]


if __name__ == "__main__":
    serches = Search("C:\\Users\\Home\\Desktop\\Intro-to-Python\\Exam", 0)

    # serches = Search(os.getcwd(), 1)
    print(serches.run('usinput'))
