#obtener la cantidad de los primeros n numeros multilpos de 5

n:int=int(input("ingregese un numero: "))

if n%5==0:
    for i in range (5,n+5,5):
        cantidad=n/5
        print(i)
    print("la cantidad de multiplos de 5 es: ", +int(cantidad))
else:
    print("no es ")