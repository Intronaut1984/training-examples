sal=int(input('Whats your salary?'))

inc1= (sal + (sal * 0.1))
inc2= (sal + (sal * 0.15))

if sal >= 1250:
    print('Teve um aumento de 10%. Seu novo salário é de: {}€'.format(inc1))
else:
    print('Teve um aumento de 15%. Seu novo salário é de: {}€'.format(inc2))