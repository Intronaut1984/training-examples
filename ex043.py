# IMC

weight = float(input('How much do you weigh?'))
height = float(input('Houw much do you measure?'))

imc = weight / (height ** 2)

if 18.6 <= imc <= 24.9:
    print('Your imc is: {:.2f}! You are in good shape!!'.format(imc))
elif imc < 18.6:
    print('Your imc is: {:.2f}! You are above the recommendation wight level!')
else:
    print('Your imc is: {:.2f}! You need to lose weight!'.format(imc))
