def suma_divisores(numero):
    hasta=numero
    suma = 0
    for i in range(1, hasta):
        if numero % i == 0:
            suma += i
    return suma



numero = int(input("Ingresa el número: "))

print("La suma es de sus divisores es: ")

print(suma_divisores(numero))