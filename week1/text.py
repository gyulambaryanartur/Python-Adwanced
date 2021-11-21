a=0
while True:
    length = input('Input length')
    if  length.isdecimal() \
            and int(length) > 0:
        break

    fill = input('Inpt fill')
    if len(fill) > 1:
        continue
    text = input('Input text')
print('a')