# Daniela Ramirez 16-10940
# Programa que maneja expresiones sobre booleanos

import sys

# Funcion para convertir las expresiones a booleanos
def convertir(left: str, right: str):
    if (left == 'True' or left == 'true') and (right == 'True' or right == 'true'):
        left = True
        right = True

    elif (left == 'False' or left == 'false') and (right == 'False' or right == 'false'):
        left = False
        right = False

    elif (right == 'True' or right == 'true') and (left == 'False' or left == 'false'):
        right = True
        left = False

    elif (right == 'False' or right == 'false') and (left == 'True' or left == 'true'):
        right = False
        left = True

    return left, right

# Funcion para operar las expresiones
def opBin(op: str, left: str, right: str) -> bool:

    izq, der = convertir(left, right)

    if op == "^":
        res = not izq
        return res
    elif op == "&":
        return izq and der
    elif op == "|":
        return izq or der
    elif op == "=>":
        return izq <= der

# Funcion para mostrar las expresiones
def mostrarBinPRE(op: str, left: str, right: str) -> str:

    if op == "&" or op == "|":
        #if len(right) > 6:
            #right = "(" + right + ")"

        return left + " " + op + " " + right

    elif op == "=>":
        #if len(left) > 1:
            #left = "(" + left

        return left + " " + op + " " + right

    elif op == "^":
        if len(left) > 5:
            l = left[len(left)-5:]
            res = op + l
            return left[:len(left)-5] + " " + res
        else:
            return op + left

# Funcion para mostrar las expresiones
def mostrarBinPOST(op: str, left: str, right: str) -> str:

    if op == "&" or op == "|":
        #if len(right) > 6:
            #right = "(" + right + ")"

        return left + " " + op + " " + right

    elif op == "=>":
        #if len(left) > 1:
            #left = "(" + left

        return left + " " + op + " " + right

    elif op == "^":
        if len(right) > 5:
            r = right[:5]
            res = op + r
            return res + right[5:]
        else:
            return op + right

# Funcion para mostrar la expresion en orden prefijo
def prefijo(act: str, expr: list) -> str:
    lista = []

    # Se recorre la lista con la expresion de derecha a izquiera
    for i in range(len(expr)-1, -1, -1):

        # Se verifica si i es el operador ^
        if expr[i] == "^":

            # Se guarda el operando en una variable
            left = lista.pop()

            # Se guarda el operador en una variable
            op = expr[i]

            # Se verifica la accion a realizar
            if act == "EVAL":
                fin = opBin(op, left, right)

            elif act == "MOSTRAR":
                fin = mostrarBinPRE(op, left, right)

            # Se guarda el resultado
            lista.append(f'{fin}')

        # Se verifica si i es un operador (&, |, =>)
        elif expr[i] == "&" or expr[i] == "|" or expr[i] == "=>":

            # Se guardan los operandos en sus respectivas variables
            left = lista.pop()
            right = lista.pop()

            # Se guarda el operador en una variable
            op = expr[i]

            # Se verifica la accion a realizar
            if act == "EVAL":
                fin = opBin(op, left, right)

            elif act == "MOSTRAR":
                fin = mostrarBinPRE(op, left, right)

            # Se guarda el resultado
            lista.append(f'{fin}')

        # Si i no es un operador, es decir es un operando, se guarda en la lista
        else:
            lista.append(expr[i])

    # Se retorna el resultado
    return lista[0]

# Funcion para mostrar la expresion en orden postfijo
def postfijo(act: str, expr: list) -> str:
    lista = []

    # Se recorre la lista con la expresion de izquiera a derecha
    for i in range(0, len(expr)):

        # Se verifica si i es el operador ^
        if expr[i] == "^":

            # Se guarda el operando en una variable
            right = lista.pop()

            # Se guarda el operador en una variable
            op = expr[i]

            # Se verifica la accion a realizar
            if act == "EVAL":
                fin = opBin(op, left, right)

            elif act == "MOSTRAR":
                fin = mostrarBinPOST(op, left, right)

            # Se guarda el resultado
            lista.append(f'{fin}')

        # Se verifica si i es un operador (&, |, =>)
        elif expr[i] == "&" or expr[i] == "|" or expr[i] == "=>":

            # Se guardan los operandos en sus respectivas variables
            right = lista.pop()
            left = lista.pop()

            # Se guarda el operador en una variable
            op = expr[i]

            # Se verifica la accion a realizar
            if act == "EVAL":
                fin = opBin(op, left, right)

            elif act == "MOSTRAR":
                fin = mostrarBinPOST(op, left, right)

            # Se guarda el resultado
            lista.append(f'{fin}')

        # Si i no es un operador, es decir es un operando, se guarda en la lista
        else:
            lista.append(expr[i])

    # Se retorna el resultado
    return lista[0]

# Funcion donde se verifica la accion a realizar y se llama a la funcion correspondiente
def evaluar(act: str) -> str:

    # Se lee lo ingresado por el usuario
    act = act.strip().split()

    # Se verifica si se desea evaluar la expresion
    if act[0].upper() == "EVAL":

        # Se verifica que el usuario haya escrito el orden (PRE o POST)
        try:
            ord = act[1]
        except IndexError:
            return "Error: falta el orden"

        # Si el usuario escribio un orden que no es PRE o POST
        if ord != "POST" and ord != "PRE":
            return "Error: orden invalido"

        # Se almacena la expresion ingresada por el usuario
        expr = act[2:]

        # Si el usuario no escribio ninguna expresion se devuelve un error
        if expr == []:
            return "Error: falta la expresion"

        # Se verfica el orden ingresado y se llama a su funcion correspondiente
        if ord == "POST":
            final = postfijo("EVAL", expr)
            return final

        elif ord == "PRE":
            final = prefijo("EVAL", expr)
            return final

    # Si el usuario desea mostrar la expresion
    elif act[0].upper() == "MOSTRAR":

        # Se verifica que el usuario haya escrito el orden (PRE o POST), sino retorna error
        try:
            ord = act[1]
        except IndexError:
            return "Error: falta el orden"

        # Si el usuario escribio un orden que no es PRE o POST se retorna error
        if ord != "POST" and ord != "PRE":
            return "Error: orden invalido"

        # Se almacena la expresion ingresada por el usuario
        expr = act[2:]

        # Si el usuario no escribio ninguna expresion se devuelve un error
        if expr == []:
            return "Error: falta la expresion"

        # Se verfica el orden ingresado y se llama a su funcion correspondiente
        if ord == "POST":
            final = postfijo("MOSTRAR", expr)
            return final

        elif ord == "PRE":
            final = prefijo("MOSTRAR", expr)
            return final

    # Si el usuario desea salir
    elif act[0].upper() == "SALIR":
        print("\nBye!")
        sys.exit()

    # Si el usuario escribio un comando invalido se retorna error
    else:
        return "Error: comando invalido"

# Main: Se le pide al usuario que accion desea realizar
if __name__ == "__main__":

    # Cuando una accion finaliza se le vuelve a preguntar que desea hacer
    while True:
        act = input("Ingrese un comando:\nEVAL <orden> <expr>\nMOSTRAR <orden> <expr>\nSALIR\n\n")
        resultado = evaluar(act)
        print(f'{resultado}\n')
