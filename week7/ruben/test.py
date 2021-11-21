class Library:
    max_book_count = 100

    def __init__(self):  #, x):
        # self.x = x
        self.attr = 145

    def add_attr(self, attr):
        self.attr = attr

    def show_attr(self):
        print(self.attr)


class Book(Library):
    def __init__(self, z):
        super().__init__()

    def render_library(self, x):
        print(Library.max_book_count)
        print(x)
        print(self.attr)

my_lib = Library()
my_lib.add_attr(45)

# print(my_lib.x)

book = Book()
book.render_library(my_lib)
