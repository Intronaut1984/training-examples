birth = int(input('Enter your year of birth'))

age = 2021 - birth

if 10 <= age <= 12:
    print('You are Infant!!')
elif 12 < age <= 14:
    print('You are Init!!')
elif 14 < age <= 16:
    print('You are Junior!!')
elif age > 16:
    print('You are Senior!!')
