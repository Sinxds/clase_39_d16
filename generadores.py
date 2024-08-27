def generador():
    n = 1
    yield n

    n += 2
    yield n

    n += 4
    yield n


gen1 = generador()

print(next(gen1))
print(next(gen1))
print(next(gen1))



def get_first_primes():
    number = 0
    while True:
        number += 1
        yield number

a = generador()

print(next(a))
print(next(a))
print(next(a))