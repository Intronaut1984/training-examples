from random import randint
pc = randint(1, 10)
count = -1
hit = False

while not hit:
    number = int(input('Choose a number between 0 and 10: '))
    count += 1
    if number == pc:
        hit = True
    else:
        if number < pc:
            print('Its higher. Please try again')
        if number > pc:
            print('Its lower. Please try again')
print('You won!! Congratulations. Computer choose {} also. You lost {} lifes'.format(pc, count))



# OR:
# from random import randint
#
# count = 0
# number = ''
# pc = 0
# while number != pc:
#     pc = randint(1, 10)
#     number = int(input('Choose a number between 0 and 10: '))
#     print('Computer choose {}, please try again'.format(pc))
#     count += 1
# print('You won!! Congratulations. Computer choose {} also. You lost {} lifes'.format(pc, count))