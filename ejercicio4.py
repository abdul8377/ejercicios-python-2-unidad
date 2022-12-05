#dados 2 numeros enteros y un operador +, -, *, / devolver la operacion de
#los 2 numeros segun el operador ingresado, considere que si el numero es cero
#y el operador es /, no es divisible con el primer numero entonces devolver como resultado 0

operacion=(input("ingrese la operacion: "))

if operacion == "+":
    a:int=int(input("ingrese numero a: "))
    b:int=int(input("ingrese numero b: "))
    suma= a+b
    print("la suma es: ",suma)
elif operacion == "-":
    a:int=int(input("ingrese numero a: "))
    b:int=int(input("ingrese numero b: "))
    resta=a-b
    print("la resta es: ",resta)
elif operacion == "*":
    a:int=int(input("ingrese numero a: "))
    b:int=int(input("ingrese numero b: "))
    multiplicacion=a*b
    print("la multiplicacion es: ",multiplicacion)
elif operacion == "/":
    a:int=int(input("ingrese numero a: "))
    b:int=int(input("ingrese numero b: "))

    if b==0:
        print("no se púede dividir entre 0")
    elif a==0:
        print("la division es 0")
    else:
        division=a/b
        print("la division es:",division)   

    

