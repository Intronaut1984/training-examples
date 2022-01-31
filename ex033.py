num1=int(input('Choose 1st number:'))
num2=int(input('Choose 2nd number:'))
num3=int(input('Choose 3th number:'))

if num1 >= num2 and num1 >= num3:
    max=num1

if num2 >= num1 and num2 >= num3:
    max=num2

if num3 >= num2 and num3 >= num1:
    max=num3

print(max)



