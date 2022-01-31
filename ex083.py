#validar expressões matemáticas

lista = []
formula = input('Insira uma fórmula matemática: ')
for simb in formula:
    if simb == ('('):
        lista.append(simb)
    elif simb == (')'):
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) > 0:
    print('Fórmula inválida')
else:
    print('Fórmula válida')










# Resposta não está 100% correta
'''listaab = []
listafe = []
form = input('Insira uma fórmula matématica: ')
for simb in form:
    if simb == ('('):
        listaab.append('(')
    elif simb == (')'):
        listafe.append(')')
abrir = listaab.count('(')
fechar = listafe.count(')')
if abrir == fechar:
    print('Comando matemático válido!')
elif abrir != fechar:
    print('Comando matemático inválido')'''


