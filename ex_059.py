# Menu
number_1 = int(input('Give me a number '))
number_2 = int(input('Give me another number '))

m = 0
while m != 5:
    sum = (number_1 + number_2)
    multi = (number_1 * number_2)
    print('''Choose a number from the Menu above:\n
    [1] - Sum Numbers\n 
    [2] - Multiply Numbers\n
    [3] - Show me the biggest number\n
    [4] - Add new numbers\n
    [5] - Exit program''')
    m = int(input('Wich option do you prefer?'))
    if m == 1:
        print(sum)
    elif m == 2:
        print(multi)
    elif m == 3:
        if number_1 > number_2:
            print(number_1)
        else:
            print(number_2)
    elif m == 4:
        print('Write new numbers: ')
        number_1 = int(input('Give me a number '))
        number_2 = int(input('Give me another number '))
    elif m == 5:
        print('Finishing program')
    else:
        print('Invalid option')
print('Finish')




