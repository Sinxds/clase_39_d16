from collections.abc import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable)) #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #True

encontrado = None
lista = [1, 2, 3, 4]
for numero in lista:
    if numero == 3:
        encontrado == numero
        break
    print(numero)

print("Encontrado :", encontrado)


for i in range(10):
    print("************")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(2,5,2):
    print(lista[i])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista[2:5:2]:
    print(lista[i])



matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for lista in matriz:
    print(lista)


for lista in matriz:
    for numero in lista:
        print(numero)


#recorriendo colecciones

pokemones = [
    {"id": 1, "nombre": "Ditto", "habilidades": ["transformación", "copiar", "duplicar"]},
    {"id": 2, "nombre": "Charizard", "habilidades": ["Escupe fuego", "volar"]},
    {"id": 3, "nombre": "Pikachu", "habilidades": ["Ataque eléctrico", "Saltar", "Correr"]}
]

for pokemon in pokemones:
    print(pokemon)

for pokemon in pokemones:
    print("Nombre pokémon: ", pokemon["nombre"])
    habilidades = pokemon["habilidades"]
    print(f"Cantidad abilidades: {len(habilidades)}")
    for habilidad in pokemon["habilidades"]:
        print("habilidad: ", habilidad)
    print("*************************************")


nombre = "Carlos"
it = iter(nombre)

print(next(it))  # next apunta memoria al elemnto que sigue (built in funtion)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# Ejemplo de uso de iter -> next()

lista = [1, 2, 3, 4, 5, 6, 7]
it =iter(lista)

print(next(it))