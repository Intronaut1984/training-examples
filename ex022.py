name=input('Whats your name?')
#Capital up
print(name.upper())

#Capital down
print(name.lower())

#Counting without spaces(dividir em string numa lista e depois unir sem nada no string
dividido=(name.split())
join=(''.join(dividido))
print(len(join))
#ou
print(len(name)-name.count(' '))

#Quantas letras tem o primeiro nome
nome1=(name.split())
print(len(nome1[0]))
#or
print(name.find(' '))
