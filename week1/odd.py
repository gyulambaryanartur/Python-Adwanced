check = True
while check:
    oddnumber = input('Input number:')
    sumodd = 0

    if oddnumber.isnumeric():
        for i in range(int(oddnumber)):
            if i % 2 == 1:
                sumodd += i
        print('Summ of odd nume is:', sumodd)
        check = False
    else:
        print('Give Correct Value')
