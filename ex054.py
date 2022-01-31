from datetime import date
date = date.today().year
major = 0
minor = 0
for i in range(1, 5):
    n = int(input('What is your date of birth? '))
    age = date - n

    if age >= 18:
        major += 1
    else:
        minor += 1
print('There are {} persons greater than 18 and {} under 18 years old'.format(major, minor))

