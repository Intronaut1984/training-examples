f = int(input('First Number: '))
s = int(input('Second Number: '))

t = int(s - f)
p = t % 2


for t in range(f, s):
    if t % 2 == 0:
        print(t)
