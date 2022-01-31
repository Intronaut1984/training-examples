from time import sleep

test_1 = float(input('Enter your 1st test value:'))
test_2 = float(input('Enter your 2nd test value:'))

print('We are generating your score. PLease wait...')
sleep(3)

score = (test_1 + test_2) / 2

if 9.5 <= score <= 12:
    print('Aproved with {} but you got to get better next time!'.format(score))
elif score > 12:
    print('Excelent you got a {}!! Continue like this!'.format(score))
elif score < 9.5:
    print('Sorry, your score is just {} and is not enough to pass!! Try next year'.format(score))
