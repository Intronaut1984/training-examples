# tabuada

c = n = m = r = 0
while True:
    n = int(input('Choose a number to see 10th multiplication: '))
    for c in range(1, 11):
        m = c
        r = c * n
        print(f'{n} x {c} = {r}')
    if n < 0:
        break
print('END')
