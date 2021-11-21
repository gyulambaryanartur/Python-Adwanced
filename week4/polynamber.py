pol = input("imput number:")


def polyndrom(polnumber: int):

    steps = 0
    while True:

        if int(polnumber) == int(str(polnumber)[::-1]):
            break

        else:
            polnumber = int(polnumber)+int(str(polnumber)[::-1])
            #polyndrom = str(polyndrom)
            steps += 1
    return steps
 

print(polyndrom(pol))