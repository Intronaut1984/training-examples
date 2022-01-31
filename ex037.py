num = int(input('Write an integer number: '))

print('''How do you want to translate it?
[1] Binary
[2] Octal
[3] Hexa''')

option = int(input('Your option:'))

if option == 1:
    print('{} in binary is {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('The value {} in Octadecimal is {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} value in Hexadecimal is {}'.format(num, hex(num)[2:]))
else:
    print('Error. Number not recognized. Try an option between 1 and 3')