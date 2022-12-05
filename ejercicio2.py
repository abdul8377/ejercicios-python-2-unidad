#determinar si un numero es posito, negativo o neutro

n:int=int(input("ingrese un numero: "))


if n<0:
    print("el numero es negativo")
elif n>0:
    print("el nuemro es positivo")
else:
    print("el nuemro es neutro")