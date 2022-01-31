import math
cat1= float(input('Qual o cateto adjacente?'))
cat2= float(input('Qual o Cateto oposto?'))
h= math.hypot(cat1, cat2)
print('A hipotenusa é {:.2f}'.format(h))