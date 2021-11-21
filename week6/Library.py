import shelve
import datetime
from types import FunctionType
class Rental:
    rentals = shelve.open('rentals.db')
    rentals['1'] = {'isbn': '1', 'client_name': 'Gevorg',
              'start_date': '1900-01-01', 'end_date': '1900-01-01'}
    rentals['2'] = {'isbn': '2', 'client_name': 'Vardges',
              'start_date': '1900-01-01', 'end_date': '1900-01-01'}
    rentals['3'] = {'isbn': '3', 'client_name': 'Artur',
              'start_date': '1900-01-01', 'end_date': '1900-01-01'}
    def __init__(self):
        pass
    def __repr__(self):
        my_values = list(self.rentals.values())
        dataset="  |  ".join(my_values[0].keys())

        for i in my_values:
            dataset += f"\n{'  | '.join(i.values())}"
        return dataset              
    
class Book(Rental):
    books = shelve.open('self.books.db')
    books['1'] = {'isbn': '1', 'title': 'G Marzpetuni',
              'author': 'Muratsan', 'year': '1800', 'is_available': '1'}
    books['2'] = {'isbn': '2', 'title': 'Mirhav',
              'author': 'Aksel Bakunts', 'year': '1956', 'is_available': '1'}
    books['3'] = {'isbn': '3', 'title': 'Samvel',
              'author': 'Raffi', 'year': '1998', 'is_available': '0'}
    def __repr__(self):
        my_values = list(self.books.values())
        dataset="  |  ".join(my_values[0].keys())

        for i in my_values:
            dataset += f"\n{'  | '.join(i.values())}"
        return dataset    
        #for lctno in my_keys:
          #pass
          #return  ' '.join(self.books[lctno].keys())
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        colname = list(dict(list(self.rentals.values())[0]).keys())
         
        if self.n<len(list(self.rentals.values())):
            datatable = f' -----------------------\n -----------------------\n {"  ".join(colname)} \n {"  ".join(list(dict(list(self.rentals.values())[self.n]).values()))} \n'
            self.n+=1
            return datatable
        #self.genericfunc()
        else:
            raise StopIteration
    
        #self.books.close()              


class Library(Book,Rental):
    def methods(self):
     return [x for x, y in Library.__dict__.items() if type(y) == FunctionType]
    def genericfunc(self):

        while True:
            commands = self.methods()          
            command = self.showmenu()

            if command.lower() not in commands:
                print('Unsupported command format. Please use one of the')
                continue
            funcname=f'self.{command}()'
            eval(funcname)
       
    
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        colname = list(dict(list(self.books.values())[0]).keys())
         
        if self.n<len(list(self.books.values())):
            datatable = f' -----------------------\n -----------------------\n {"  ".join(colname)} \n {"  ".join(list(dict(list(self.books.values())[self.n]).values()))} \n'
            self.n+=1
            return datatable
        #self.genericfunc()
        else:
            raise StopIteration

    #delete book from db
    def d(self):

        isbn = input('Enter isbn code:')
        print("".join(self.books.keys()))
        
        if isbn in self.books.keys():
            del self.books[isbn]
            print(f'Data from books.db was deleted for isbn:{isbn}')
              
        else:
          
            print(f'\nIsbn was not found \n')

        self.genericfunc()
    #delete rental from db
    def dr(self):

        isbn = input('Enter isbn code:')
        print("".join(self.rentals.keys()))
        
        if isbn in self.rentals.keys():
            del self.rentals[isbn]
            print(f'Data from books.db was deleted for isbn:{isbn}')
              
        else:
          
            print(f'\nIsbn was not found \n')

        self.genericfunc()
    # Add or update a book
    def a(self):

        isbn = input('Enter isbn code:')
        titlenm = input('Enter title Name:')
        author = input('Enter author name :')
        ityear = input('Enter Item year:')
        is_available = input('Enter if book is available or not:')

        if isbn in self.books.keys():
            inititemcount = self.books[isbn].get('year')
            self.books[isbn] = {'isbn': isbn, 'title': titlenm,
                           'author': author, 'year': ityear,'is_available':is_available}
            print(f'\nItem has been updated \n')
        else:
            self.books[isbn] = {'isbn': isbn, 'title': titlenm,
                           'author': author, 'year': ityear,'is_available':is_available}
            print(f'\nItem has been added \n')

        self.genericfunc()
    # Add or update a rental
    def ar(self):

        isbn = input('Enter isbn code:')
        client_name = input('Enter client name :')
        

        if isbn in self.rentals.keys():
            inititemcount = self.rentals[isbn].get('year')
            self.rentals[isbn] = {'isbn': isbn, 'client_name': client_name}
            print(f'\nItem has been updated \n')
        else:
            self.rentals[isbn] = {'isbn': isbn, 'client_name': client_name}
            print(f'\nItem has been added \n')

        self.genericfunc()    
    def show(self):
        book=Book()
        print(book)
    #show all rentals
    def showr(self):
        rentals=Rental()
        print(rentals)    
    # Search for a book
    def s(self):

        datatable = None
        itemcodename = input(f'\nInput  isbn:')
        colname = list(dict(list(self.books.values())[0]).keys())
        for items in self.books.values():
            if str(items.get('isbn')) == itemcodename:
                datatable = f' -----------------------\n -----------------------\n {"  ".join(colname)} \n {"  ".join(list(items.values()))} \n'
                print(datatable)
                self.genericfunc()
        if datatable == None:
            print(f'Item is missing form the storage')
        self.genericfunc()

    # Search for a rentals
    def sr(self):

        datatable = None
        itemcodename = input(f'\nInput  isbn:')
        colname = list(dict(list(self.rentals.values())[0]).keys())
        for items in self.rentals.values():
            if str(items.get('isbn')) == itemcodename:
                datatable = f' -----------------------\n -----------------------\n {"  ".join(colname)} \n {"  ".join(list(items.values()))} \n'
                print(datatable)
                self.genericfunc()
        if datatable == None:
            print(f'Item is missing form the storage')
        self.genericfunc()

    
    # Register rental information
    def r(self):

        item = input('Enter Item code:')

        if self.books[item] and self.books[item].get('is_available')=="1":
            inititemcount = self.books[item].get('year')
            inititemauthor = self.books[item].get('author')
            inititemname = self.books[item].get('title')
            Client_Name = input('Enter Client Name:')

            self.books[item] = {'isbn': item, 'title': inititemname,
                           'author': inititemauthor, 'year': inititemcount,'is_available':'0'}
            self.rentals[item] = {'isbn': item, 'client_name': Client_Name,
                           'start_date': str(datetime.datetime.now()), 'end_date': str(datetime.datetime(3000,1,1))}
            print("\nYour rent is registered successfully.\n")
        else:
            print("\nThere are no enough items in your store or it is absent\n")
        self.genericfunc()

    def x(self):
        exit()

    def showmenu(self):
        show_menu = f'  \n\t Available actions:  \n \t  a - Add or update a book  \
            \n \t  ar - Add or update a Rentals \
            \n \t  s - Search for a book  \n \t  sr - Search for a rentals  \n \t  r - Register rental information \
            \n \t  d - Delete a book \n \t  dr - Delete a rentals \n \t  show - Show all  books \n \t  showr - Show all  rents  \n  \t  x - Exit\n'
        print(show_menu)
        inpcomm = input('Enter command code:')
        return inpcomm




# print(show_menu)
if __name__ == "__main__":
    
    book = Library()
    rental = Book()
    i=iter(book)
    j=iter(rental)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(j))
    print(next(j))
    #print(next(i))
  

    book.genericfunc()

Book.books.close()
# print(list(s.items()))
