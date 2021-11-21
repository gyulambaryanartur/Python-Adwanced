mathsigns = {"+": "add", "-": "subtract", \
             "/": "divide", "*": "multply"}  # sign pattern
functpattern = '(num1,num2)'


# functions  for operations  calcualtor
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2 if num2 else 0


def multply(num1, num2):
    return num1 * num2


# Implement validation
while True:
    inp = input("input Statements of calculator:")
    sign = inp.lstrip()[0]
    numbers = inp.lstrip()[1:].split(' ')
    numbers = list(filter(None, numbers))

    if sign in mathsigns.keys() and len(numbers) == 2 and \
            numbers[0].isdecimal() and numbers[1].isdecimal():
        funcname = mathsigns.get(sign)
        num1 = int(numbers[0])
        num2 = int(numbers[1])

        break
    print("Enter valid expression")
funcname = "%s %s" % (funcname, functpattern)  # get full name of function
result = eval(funcname)  # run string as command
print("Operation  of %d %s %d = %s" % (num1, sign, num2, result))
