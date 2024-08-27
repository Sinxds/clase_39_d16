import funcion_documentada
from funcion_documentada import calcular

print(funcion_documentada.calcular)

print(calcular(2, 6))


import modulo_operaciones

print(modulo_operaciones.sumar(3, 5))
print(modulo_operaciones.restar(4, 6))


from modulo_operaciones import sumar, restar

print(sumar(3, 5))
print(restar(4, 6))

from modulo_operaciones import sumar as add, restar as minus

print(add(3, 5))
print(minus(4, 6))