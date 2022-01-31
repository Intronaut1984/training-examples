# ex(2) Ame o Poema

# coloca em maiuscula e depois divide as palavras
frase = str(input('Escreva um Palímero: ')).upper().split()
# print(frase)
# Retirar espaços: Depois de dividir com split(), é só unir novamente
join = "".join(frase)
# print(join)
# Pode também ser feito assim:
# space = frase.replace(' ', '')
inverso = ''
for letra in range(len(join) -1, -1, -1):
    inverso = inverso + join[letra]
print(inverso)

if inverso == join:
    print('É Palímero')
else:
    print('Não É Palimero')





