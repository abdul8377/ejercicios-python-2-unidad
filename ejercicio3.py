#dado la hora minuto y segundo encuentre la hora del siguiente segundo


hora:int=int(input("ingrese la hora: "))

while hora>12:
    hora:int=int(input("ingrese nuevamente la hora: "))

minuto:int=int(input("ingrese el minuto: "))

while minuto>60:
    minuto:int=int(input("ingrese nuevamente el minuto: "))

segundo:int=int(input("ingrese el segundo: "))

while segundo>60:
    segundo:int=int(input("ingrese nuevamente el segundo: "))


hora1=minuto +1
hora2=segundo +1
if hora1 and hora2 >= 60:
    print(f'la hora es {hora +1}:00:00')

else:
    print(f'la hora es1 {hora}:{minuto +1}:{segundo +1}')