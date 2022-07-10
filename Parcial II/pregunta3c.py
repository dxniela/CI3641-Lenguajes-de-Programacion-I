# Daniela Ramirez 16-10940
# Programa que genera todas las expresiones bien parentizadas que se pueden formar con n paréntesis

def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def permutaciones(list):
    if list:
        for m in permutaciones(list[1:]):
            for i in ins(list[0], m):
                yield i
    else:
        yield []

def bienParentizadas(n):
    list = [0] * n * 2
    pila = []

    for i in range(len(list)):
        if i % 2 == 0 or i == 0:
            list[i] = '('
        else:
            list[i] = ')'

    for i in permutaciones(list):
        if i[0] == ')' or i[-1] == '(':
            continue
        pila = []
        for j in i:
            if j == '(':
                pila.append(j)
            else:
                if pila:
                    pila.pop()
                else:
                    pila.append(j)
                    break

        if pila:
            yield []
        else:
            yield i

while True:
    try:
        n = int(input("Ingrese el numero de parejas de parentesis: "))
        break
    except ValueError:
        print("Error: ingrese un numero valido")
        continue

lista = []
for c in bienParentizadas(n):
    if (c in lista) == True:
        pass
    else:
        if c == []:
            pass
        else:
            lista.append(c)

for i in lista:
    print(i)
