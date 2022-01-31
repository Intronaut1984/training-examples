dist=int(input('Que distância pretende percorrer?'))

max=(dist * 0.45)
min=(dist * 0.50)

if dist >= 200:
    print('O valor cobrado será de {}€'.format(max))
else:
    print('O valor a pagar será de {}€'.format(min))

print('Obrigado por viajar com a Brisa')