# dado un rango de numeros determine 
# cuantos numeros capicua hay


valor=()
lista=[]
capicuas = []
i=0
while valor!=0:
    i=i+1
    valor:int=int(input("ingrese un umero: "))
    lista.append(valor)
    if valor > 10 and valor < 100000000000000000000000000:
        a = valor // 100
        b = valor % 10
        if a == b:
            capicuas.append(1)
            print(valor, "es capicua")
          
        
        else:
            print(valor, "no es capicua")
    
    else:
        print("ingrese un numero")
        
print(lista)
suma = 0
for i in capicuas:
    suma = suma + i
print(f'la cantidad de capicuas es {suma}')
