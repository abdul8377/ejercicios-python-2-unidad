# dado 5 numeros y un divisor determinar cuantos 
# numeros multiplos hay del divisor en los 5 nuemros
# ingresados


numero1:int=int(input("ingrese el numero 1: "))
numero2:int=int(input("ingrese el numero 2: "))
numero3:int=int(input("ingrese el numero 3: "))
numero4:int=int(input("ingrese el numero 4: "))
numero5:int=int(input("ingrese el numero 5: "))
divisor:int=int(input("ingrese un divisor: "))
print()
print()
print("lista de divisores")
print()
print()
if numero1%divisor==0:
    multiplos = []
    for i in range (divisor,numero1+divisor,divisor):
        cantidad=numero1/divisor
        multiplos.append(i)
    print(multiplos)
    print(f'la cantidad de multiplos de {divisor} de {numero1} es {+int(cantidad)}')
    print()
    print()

if numero2%divisor==0:
    multiplos = []
    for i in range (divisor,numero2+divisor,divisor):
        cantidad=numero2/divisor
        multiplos.append(i)
    print(multiplos)
    print(f'la cantidad de multiplos de {divisor} de {numero2} es {+int(cantidad)}')
    print()
    print()
if numero3%divisor==0:
    multiplos = []
    for i in range (divisor,numero3+divisor,divisor):
        cantidad=numero3/divisor
        multiplos.append(i)
    print(multiplos)
    print(f'la cantidad de multiplos de {divisor} de {numero3} es {+int(cantidad)}')
    print()
    print()

if numero4%divisor==0:
    multiplos = []
    for i in range (divisor,numero4+divisor,divisor):
        cantidad=numero4/divisor
        multiplos.append(i)
    print(multiplos)
    print(f'la cantidad de multiplos de {divisor} de {numero4} es {+int(cantidad)}')
    print()
    print()
if numero5%divisor==0:
    multiplos = []
    for i in range (divisor,numero5+divisor,divisor):
        cantidad=numero5/divisor
        multiplos.append(i)
    print(multiplos)
    print(f'la cantidad de multiplos de {divisor} de {numero5} es {+int(cantidad)}')
    print()
    print()

else:
    print("no es multiplo")