#dado un numero y un divisor, determine cuak es el 
# numero multiplo antecesor al numero ingresadoo, por 
# ejemplo si ingresa N = 21 y D = 3, entonces R = 18 por 
# que es el multiplo de 3 antecesor de 21



n:int=int(input("ingrese el numero: "))
d: int=int(input("ingrese el divisor: "))


multiplo_antecesor= n-d

print("el multiplo antecesor es", multiplo_antecesor)