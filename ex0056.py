# Name, Age, Genre

n = 0
w = 0
nomevelho = ''
maioridade = 0
for i in range(1, 5):
    print('Person {}'.format(i))
    name = input('Whats your name?')
    age = int(input('Whats your age?'))
    g = input('Genre (M/F)')
    print('=/' * 10)
    n = n + age
    if g in 'Ff' and age < 20:
        w += 1
    if i == 1:
        maioridade = age
        nomevelho = name
    if age > maioridade:
        maioridade = age
        nomevelho = name
print('A média de idades é de: ', (n / i), 'anos')
print('{} é a pessoa mais velha e tem {} anos'.format(nomevelho, maioridade))
print('Há {} mulhere(s) com menos de 20 anos'.format(w))
