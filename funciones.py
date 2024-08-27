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