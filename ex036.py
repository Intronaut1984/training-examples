house = int(input('Whats is the your house value?'))
salary = int(input('Whats your salary?'))
years = int(input('For how long do you think to pay the house (in years)?'))

months = years * 12
fee = house / months
cond = salary * 0.3

if cond >= fee:
    print('Congrats, you can buy the house!!!')
else:
    print('Sorry, you can not afford the house.')

