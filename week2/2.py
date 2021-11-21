def remrepete(ii):
    lis = [12, 1, 2, 3, 3, 3, 21, 312, 2, 2, 5, 2]
    listnew = []

    for i in lis:
        if listnew.count(i) < ii:
            listnew.append(i)

    return  listnew
print (remrepete(2))
