# pedra papel tesoura
import random
from time import sleep

print('''[1] Pedra 
[2] Papel 
[3] Tesoura?''')
val = int(input('Qual a sua opção?: '))

hip = 'Pedra', 'Papel', 'Tesoura'
val_pc = random.choice(hip)

print('My turn...')
sleep(1)

if val == 1 and val_pc == 'Papel':
    print('Voce é burra Tatiana??!! Eu escolhi Papel. Ganhei!!')
elif val == 1 and val_pc == 'Tesoura':
    print('Escolhi Tesoura. Você Ganhou e é muito inteligente')
elif val == 1 and val_pc == 'Pedra':
    print('Escolhi Pedra também. É um empate!!')

if val == 2 and val_pc == 'Papel':
    print('Escolhi Papel também. É um empate!!')
elif val == 2 and val_pc == 'Tesoura':
    print('Tatiana você é mesmo burra!! Eu escolhi tesoura. Ganhei!!!')
elif val == 2 and val_pc == 'Pedra':
    print(' Escolhi Pedra. Você ganhou!!! ')

if val == 3 and val_pc == 'Tesoura':
    print('Escolhi Tesoura também. É um empate!')
elif val == 3 and val_pc == 'Papel':
    print('Eu escolhi Papel. Você ganhou!!!')
elif val == 3 and val_pc == 'Pedra':
    print('Tatiana você é mesmo burra!! Eu escolhi Pedra. Ganhei!!!')




