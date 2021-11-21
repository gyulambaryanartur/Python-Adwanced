from collections import Counter
# input validation using set
mask = {'0', '1'}
while True:
    inp = input('Input binary string: ')
    if set(inp).issubset(mask):
        break
    print('[ERROR] Invalid binary number')
# manual input validation
while True:
    inp = input('Input binary string: ')
    ok = True
    for ch in inp:
        if ch != '1' and ch != '0':
            ok = False
            break
    if ok:
        break
    print('[ERROR] Invalid binary number')
# solution for main task
ones = inp.count('1')
zeros = inp.count('0')  # zeros = len(inp) - ones
ones = 0
zeros = 0
for ch in inp:
    if ch == '1':
        ones += 1
    elif ch == '0':
        zeros += 1
print('Ones:', ones)
print('Zeros:', zeros)
counter = {'0': 0, '1': 0}
for ch in inp:
    counter[ch] += 1
print('Ones:', counter['1'], '\n', 'Zeros:', counter['0'])