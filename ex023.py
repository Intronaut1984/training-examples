number=(input('Write a number between 0 and 9999'))

split=(number.split())
count=(len(split[0]))

print('number of caracters is:',count)

thousand=(number[0:1])
print('thousand',thousand)

hundred=(number[1:2])
print('hundred', hundred)

tenth=(number[2:3])
print('ten', tenth)

unity=(number[3:4])
print('unit', unity)

print(int(number)//1000%10)
print(int(number)//100%10)
print(int(number)//10%10)
print(int(number)//1%10)