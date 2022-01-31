import random
nome1= str(input('Qual o seu nome?'))
nome2= str(input('Qual o seu nome?'))
nome3= str(input('Qual o seu nome?'))
nome4= str(input('Qual o seu nome?'))
nome5= str(input('Qual o seu nome?'))
lista= [nome2, nome1, nome3, nome4,nome5]
escolido= random.shuffle(lista)
print('o escolhido é:')
print(lista)
