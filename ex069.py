# age and genre
genre = loop = ''
age = 0
cgenref = cgenrem = cage = under = 0
while True:
    while True:
        while True:
            genre = str((input('Whats you genre? [M/F] ').upper()))
            if genre == 'M':
                cgenrem += 1
            if genre == 'F':
                cgenref += 1
            if genre != 'F' and genre != 'M':
                print('Insert valid genre')
            else:
                break
        age = int(input('Whats your age?'))
        if age >= 18:
            cage += 1
        if age > 150:
            print('Invalid age')
        if age < 18:
            under = cgenref
            break

        else:
            break
    q = str((input('Do you want to proceed? [Y/N]').upper()))
    if q == 'Y':
        print('Answer again!')
    if q == 'N':
        break

print(f'Há {cage} pessoas com mais de 18 anos. Há {cgenrem} homens registados e {under} mulheres com menos de 18 anos')
