while True:
    guesser = input('input string:')
    if guesser.isdecimal():
        print('string type is decimal')
    elif guesser.isdigit():
        print('string type is digit')

    elif guesser[0] != 0 and guesser[-1] != '.' \
            and guesser.replace('.', '', 1).isdecimal():
        print('Type is float')
    else:
        print('Type is string')
