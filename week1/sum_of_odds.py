# TODO:
# 1. get a number from user
# 2. sum of the odds


'''num = input('Give me an integer: ')
while not num.isdecimal():
    print('[ERROR] provide vaild integer')
    num = input('Give me an integer: ')'''

while True:
    num = input('Give me an integer: ')
    if num.isdecimal():
        break

    print('[ERROR] provide vaild integer')    

sum_of_odds = 0





for i in range(int(num)):
    if i % 2 != 0:
        sum_of_odds += i

print(sum_of_odds)

sum_of_odds = 0
for i in range(1, int(num), 2):
    sum_of_odds += i

print(sum_of_odds)
