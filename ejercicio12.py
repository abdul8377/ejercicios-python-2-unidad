# obtener el factorial de un numero, recuerde que el 
# factorial de un numero es el producto de 1 x 2 x 3 x ... x N

acumulador:int=1
contador:int=1

numero:int=int(input("ingrese el numero: "))

while acumulador<=numero:
    contador = contador * acumulador
    acumulador = acumulador +1
print(contador)
