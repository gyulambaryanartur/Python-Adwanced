inpbit = input('Git bit string:')
counzero = 0
countone = 0
while True:
    if not inpbit.isdecimal():
        print('Acurate value')
        break
    else:
        for i in inpbit:
            if int(i) > 1:
                break
            else:
                print(inpbit.count('1'), '/n', 'count of zero:',
                inpbit.count('0'))
