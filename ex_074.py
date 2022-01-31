# Tuples with radint
from random import randint

sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(sorteio)

print(f'O maior número é {max(sorteio)}')
print(f'O menor número é {min(sorteio)}')
