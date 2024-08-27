# una función es un bloque de código reutilizable
# Por buena práctica, lleva nombre de VERBOS Ej: Saludar, Mostrar, etc.
# es resevada por el lenguaje
# No recibe parámetros

'''
def saludar():
    print("Hola mundo!")


saludar()
saludar()
saludar()

################################################### 

def saludar(saludo):
    print (saludo)


saludar(input("Ingresa saludo: "))
saludar(input("Ingresa saludo: "))
saludar(input("Ingresa saludo: "))

'''

def saludar(saludo):
    return f"¡{saludo}!"

saludar("")


def sumar(nro1, nro2):
    resultado = nro1+nro2
    return(resultado)
 
print(sumar(2,4))

# una función puede recibir n cantidad de paramétros o argumentos
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)

print(resultado)


#################################
def sumar(*valores):
    print(type(valores))
    resultado = 0
    for valor in valores:
        resultado += valor
    
    return resultado

resultado = sumar(3, 5, 6)
print(resultado)


def operaciones(op, *valores):
    resultado = 0

    if op == "sumar":
        for valor in valores:
            resultado += valor
    elif op == "restar":
        for valor in valores:
            resultado -= valor
    else:
        return None

    return resultado

resultado = operaciones("sumar", 4,5,6,7,7)
print(resultado)


def sumar(a, b):
    print(a)
    print(b)
    return a+b

resultado = sumar(b = 2, a = 3) # se puede dar el propio orden asignandolo con el nombre del parametro

print(resultado)


# indicar tipo de dato que recibe la función

def sumar(a: float = 0, b: int = 0) -> list:  # 0 en este caso es un valor por defecto
    return a+b



resultado = sumar("a", "c")

print(resultado)

##########################
numeros = [1, 2, 3, 4, 5, 6]

def sumar(valores):
    print(valores)

sumar(numeros)

##################################
# spread en python

numeros = [1, 2, 3, 4, 5, 6]

def sumar(*valores):
    print(valores)

sumar(*numeros, 5, 4, 7, 8)

