# FUNCIONES-PYTHON
lista=[numero for numero in range(0,6)if numero %2==0]
print(lista)

def pares (n):
    for numero in range(n+1):
        if numero %2==0:
            yield numero 
for numero in pares(10):
    print (numero)

def cuadrados(numero):
    for numero in range(1,numero+1):
        yield numero,numero**2
print(cuadrados)
