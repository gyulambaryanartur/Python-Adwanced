inp = input('Hit me: ')
msg = 'You hitted me with'

if inp.isdecimal():
    print(msg, '<integer>')
elif inp[0] != '.' and inp[-1] != '.' and \
     inp.replace('.', '', 1).isdecimal():
    print(msg, '<float>')
else:
    print(msg, '<string>')
