# calualtion formula perfect number num is prime number
def perfect_formula(num):
    return (2 ** (num - 1)) * (2 ** num - 1)


# calualtion formula prime number
def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


while True:
    limit = input("input limit for perfect number search \n or type  "
                  " exit to exit from program:  ")
    if limit == 'exit':
        exit()
    elif limit.isdecimal():
        break
    else:
        print("please enter decimal value!!!!!!!!!!")
        continue

limit = int(limit)

for i in range(1, limit):
    if is_prime(i) and limit > perfect_formula(i):
        perfect_num = perfect_formula(i)
        print(perfect_formula(i))
    elif limit < perfect_formula(i):
        break
