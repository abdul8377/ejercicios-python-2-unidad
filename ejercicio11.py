#una fruteria ofrece las manzanas con descuento 
# segun la siguiente tabla:
#    ______________________________
#    |   kilos    | descuento      |
#    |   0-2      |      0%        |
#    |   2.01-5   |      10%       |
#    |   5,01-10  |      20%       |
#    |mayor a 10  |      30%       |
#
#determianr cuanto pagara una persona que compre manzanas en esta 
# fruteria

print("kilo de manzana  = 20$ ")
precio_kilo_manzanas= 20
kilos:float=float(input("ingrese la cantidad de kilos: "))

if 0<=kilos<=2:
    print("no hay descuento9")
elif 2.01<=kilos<=5:
    precio_total = kilos*precio_kilo_manzanas
    descuento= precio_total*0.10
    print("el desceunto es $",descuento)
    print("el total a pagar es $",(precio_total-descuento))
elif 5.01<=kilos<=10:
    precio_total = kilos*precio_kilo_manzanas
    descuento= precio_total*0.20
    print("el desceunto es $",descuento)
    print("el total a pagar es $",(precio_total-descuento))
elif kilos>=10.01:
    precio_total = kilos*precio_kilo_manzanas
    descuento= precio_total*0.30
    print("el desceunto es $",descuento)
    print("el total a pagar es $",(precio_total-descuento))
else:
    print("ingrese de nuevo los valores")