import shelve
s = shelve.open('fruits_shelf.db')
s['1'] = {'itemid': 1, 'name': 'banana', 'price': 1000, 'count': 2}
s['2'] = {'itemid': 2, 'name': 'apple', 'price': 300, 'count': 5}
s['3'] = {'itemid': 3, 'name': 'abricot', 'price': 150, 'count': 10}

commands = {'s': 'sell', 'f': 'search', 'a': 'adding',
            "back": "showmenu", "x": "exitprogram"}


def genericfunc():
    command = showmenu()
    funcname = f'{commands.get(command)}()'
    eval(funcname)


def adding():

    item = input('Enter Item code:')
    itemnm = input('Enter Item Name:')
    price = input('Enter Item price:')
    itcount = int(input('Enter Item count:'))

    if item in s.keys():
        inititemcount = s[item].get('count')
        s[item] = {'itemid': item, 'name': itemnm,
                   'price': price, 'count': inititemcount+itcount}
        print(f'\nItem has been updated \n')
    else:
        s[item] = {'itemid': item, 'name': itemnm,
                   'price': price, 'count': itcount}
        print(f'\nItem has been added \n')

    genericfunc()


def search():

    datatable = None
    searchcriteria = input(
        f'Input name search by item name or input itemid to search by item code: ')
    itemcodename = input(f'\nInput item name or item code:')
    colname = list(dict(list(s.values())[0]).keys())
    for items in s.values():
        if str(items.get(searchcriteria)) == itemcodename:
            datatable = f' -----------------------\n -----------------------\n {colname} \n {list(items.values())} \n'
            print(datatable)
            genericfunc()
    if datatable == None:
        print(f'Item is missing form the storage')
    genericfunc()


def sell():

    item = input('Enter Item code:')
    itcount = int(input('Enter Item count:'))
    if s[item] and itcount <= s[item].get('count'):
        inititemcount = s[item].get('count')
        inititemprice = s[item].get('price')
        inititemname = s[item].get('name')

        s[item] = {'itemid': item, 'name': inititemname,
                   'price': inititemprice, 'count': inititemcount-itcount}
        print("\nYour sale is registered successfully.\n")
    else:
        print("\nThere are no enough items in your store or it is absent\n")
    genericfunc()


def exitprogram():
    exit()


def showmenu():
    show_menu = f'  \n\t Available actions:  \n \t  a - Add or update an item  \n \
         f - Search for an item  \n \t  s - Register a sale   \n  \t  x - Exit\n'
    print(show_menu)
    inpcomm = input('Enter command code:')
    return inpcomm


# print(show_menu)
genericfunc()


# print(list(s.items()))
s.close()
