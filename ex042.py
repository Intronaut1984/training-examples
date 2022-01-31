from time import sleep

ab = int(input('Choose your first side'))
cd = int(input('Choose your second side'))
ef = int(input('Choose your third side'))
ok = str('It is possible to design a triangule')

if (ab + cd) >= ef and (cd + ef) >= ab and (ef + ab) >= cd:
    print(ok)

print('=//' * 15)
print('Please Wait... Calculating your triangule type.')
print('=//' * 15)
sleep(3)

if ok == True:
    print('It is posible to design a triangule')
elif ab == cd and ab == ef:
    print('This triangule is: Equilateral')
elif ab != cd and ab != ef:
    print('Your triangule is: Scalene!!')
else:
    print('Your triangule is: Isosceles!!')
