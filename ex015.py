km=int(input('Quantos Km percorreu com o seu carro alugado?'))
dia=int(input('Durante quantos dias?'))
predia= 60
preco= (dia * predia) + (km * float(0.15))
print('O valor total para {} dia(s) de aluguer e {}km percorridos é de {}€'.format(dia,km,preco))
