# ordene 5 numeros segun la forma que 
# se indique A(ascendente) o D(descendente)


valor=()
lista =[]
i=0
while i < 5 :
    i=i+1
    valor:int=int(input("ingrese un numero: "))

    lista.append(valor)

orden:str=str(input("ingrese el orden ascendente o descente: "))

if orden == "ascendente":
    lista.sort()

elif orden == "descendente":
    lista.sort(reverse=True)

print(lista)
