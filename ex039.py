born = int(input('Ano de nascimento:'))

ad = 2021
age = 2021 - born
wait = 18 - age
pas = age - 18

if age < 18:
    print('You have to wait more {} year(s) to get listed'.format(wait))
elif age > 18:
    print('Your time is up!! You should get listed {} year(s) ago.'.format(pas))
elif age == 18:
    print('You have to get listed right now!')
