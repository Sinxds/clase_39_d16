
a = 10
b = 10

# Usar id() para obtener el identificador de ambos objetos
print(f"ID de a: {id(a)}")
print(f"ID de b: {id(b)}")

# Verificar si a y b son el mismo objeto en memoria
if id(a) == id(b):
    print("a y b son el mismo objeto en memoria.")
else:
    print("a y b son objetos diferentes.")



a = 99999999999999999999999999999999999999999999999999999999999999999 # Valor fuera del rango optimizado
b = 99999999999999999999999999999999999999999999999999999999999999999 # Otro objeto con el mismo valor

print(f"ID de a: {id(a)}")
print(f"ID de b: {id(b)}")

if id(a) == id(b):
    print("a y b son el mismo objeto en memoria.")
else:
    print("a y b son objetos diferentes.")
