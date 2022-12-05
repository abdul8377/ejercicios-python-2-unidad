#dados 2 numeros diga si son amigos o no, recuerde que dos 
# numros son amigos si la suma de sus divisores de uno de ellos es 
# igaul al otro y viceversa, por ejemplo 220 y 284 son amigos: 
# divsiores de 220 son 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 =284 
# divisores de 284 son 1 + 2 + 4 + 71 + 142 = 220 



def suma_divisores(a):
    hasta=a
    suma = 0
    for i in range(1, hasta):
        if a % i == 0:
            suma += i
    return suma

def suma_divisores(b):
    hasta=b
    suma = 0
    for i in range(1, hasta):
        if b % i == 0:
            suma += i
    return suma



a = int(input("Ingresa el número: "))
b = int(input("ingrese un numero: "))

print(f'la suma de los devisores de {a} es: {suma_divisores(a)} ')
print(f'la suma de los devisores de {b} es: {suma_divisores(b)} ')

if suma_divisores(a)==b and suma_divisores(b)==a:
    print("son amigos")
else:
    print("no son amigos")

