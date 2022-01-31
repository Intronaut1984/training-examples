# Tuplas
n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')
i = 0

while True:
    i = int(input('Escreva um número entre 0 e 20: '))
    if i <= 20 and i >= 0:
        print(f'O número escolhido foi {n[i]}')
    if i > 20 or i < 0:
        print('Tenta de novo')
    else:
        break
print('END')
