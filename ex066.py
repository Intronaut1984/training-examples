# while break

c = n = s = 0

while True:
    n = int(input('Choose any number. Press 999 to exit program: '))
    if n == 999:
        break
    c += 1
    s += n

print(f'Total sum is {s} and you wrote {c} numbers!')

