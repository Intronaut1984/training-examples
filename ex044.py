price = float(input('Confirm your 50$ basket to see payment methods.'))

cashp = float(input('Cash Payment: Press 1. Another mothod: Press 2'))
cardp = float(input('For Card Payment: Press 1. Another mothod: Press 2'))
x_2 = float(input('To pay in two times: Press 1. Another method: Press 2'))
x_3 = float(input('To pay in 3 times press 1: Another method: Press 2'))

price_1 = price - (price * 0.1)
price_2 = price - (price * 0.05)
price_3 = price * 1
price_4 = price + (price * 0.2)

if cashp == 1:
    print('Your final price for instant payment with cash is: {}'.format(price_1))
elif cardp == 1:
    print('Your final price for instant payment with card is: {}'.format(price_2))
elif x_2 == 1:
    print('Your final price for 2x payment is: {}'.format(price_3))
elif x_3 == 1:
    print('Your final price for 3x payment is: {}'.format(price_4))
