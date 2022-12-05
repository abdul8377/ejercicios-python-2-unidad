#dados dos nuemros enteros a y b, 
# determinhar cual es mayor con respecto al otro

a: int=int(input("ingrese el nuemro 1: "))
b: int=int(input("ingrese el numero 2: "))

if a>b:
    print(f'{a} es mayor que {b}')
elif b>a:
    print(f'{b} es mayor que {b}')
else:
    print("son iguales")