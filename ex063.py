# Fibonacci
n = int(input('Choose number of Fibonacci terms '))
t1 = 0
t2 = 1

print('{} --> {} --> '.format(t1, t2), end='')
count = 3

while count <= n:
    t3 = t1 + t2
    print('{} --> '.format(t3), end='')
    count += 1
    t1 = t2
    t2 = t3
print('END')