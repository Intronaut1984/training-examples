import math
num=int(input('Escolha um angulo'))
cvalue= math.cos(math.radians(num))
svalue= math.sin(math.radians(num))
tvalue= math.tan(math.radians(num))
print('Cos, Sin e Tang de {} é {:.2f},{:.2f} e {:.2f} respectivamente'.format(num,cvalue,svalue,tvalue))