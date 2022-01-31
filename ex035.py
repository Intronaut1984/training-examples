lineab=int(input('Type AB line size'))
linecd=int(input('Type CD line size'))
lineef=int(input('Type EF line size'))

if (lineab + linecd) > lineef and (linecd + lineef) > lineab and (lineef + lineab) > linecd:
    triangule = print('It is posible to do a  triangule!!!')

else:
    print('Not possible to do a triangule')
