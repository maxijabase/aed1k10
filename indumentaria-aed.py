# carga de datos

t1 = int(input("==PRENDA 1==\n\nTipos de prenda:\n0=Remeras\n1=Camisas\n2=Pantalones\n3=Faldas\n4=Vestidos\n5=Abrigos\n6=Calzado\n\nIngrese tipo de prenda:"))
p1 = float(input("Ingrese el precio de la prenda: AR$"))
s1 = str(input("¿Desea participar del programa SuperPuntos? (s/n)"))

t2 = int(input("==PRENDA 2==\n\nTipos de prenda:\n0=Remeras\n1=Camisas\n2=Pantalones\n3=Faldas\n4=Vestidos\n5=Abrigos\n6=Calzado\n\nIngrese tipo de prenda:"))
p2 = float(input("Ingrese el precio de la prenda: AR$"))
s2 = str(input("¿Desea participar del programa SuperPuntos? (s/n)"))

t3 = int(input("==PRENDA 3==\n\nTipos de prenda:\n0=Remeras\n1=Camisas\n2=Pantalones\n3=Faldas\n4=Vestidos\n5=Abrigos\n6=Calzado\n\nIngrese tipo de prenda:"))
p3= float(input("Ingrese el precio de la prenda: AR$"))
s3 = str(input("¿Desea participar del programa SuperPuntos? (s/n)"))

fp = int(input("¿Cómo desea pagar?\n1=Contado\n2=Tarjeta..."))

tipos = ["Remeras", "Camisas", "Pantalones", "Faldas", "Vestidos", "Abrigos","Calzado."]

tsp = p1+p2+p3
subtot = p1+p2+p3

tt1 = None
tt2 = None
tt3 = None

if t1 == 0:
    tt1 = "Remeras"
if t1 == 1:
    tt1 = "Camisas"
if t1 == 2:
    tt1 = "Pantalones"
if t1 == 3:
    tt1 = "Faldas"
if t1 == 4:
    tt1 = "Vestidos"
if t1 == 5:
    tt1 = "Abrigos"
if t1 == 6:
    tt1 = "Calzado"

if t2 == 0:
    tt2 = "Remeras"
if t2 == 1:
    tt2 = "Camisas"
if t2 == 2:
    tt2 = "Pantalones"
if t2 == 3:
    tt2 = "Faldas"
if t2 == 4:
    tt2 = "Vestidos"
if t2 == 5:
    tt2 = "Abrigos"
if t2 == 6:
    tt2 = "Calzado"

if t3 == 0:
    tt3 = "Remeras"
if t3 == 1:
    tt3 = "Camisas"
if t3 == 2:
    tt3 = "Pantalones"
if t3 == 3:
    tt3 = "Faldas"
if t3 == 4:
    tt3 = "Vestidos"
if t3 == 5:
    tt3 = "Abrigos"
if t3 == 6:
    tt3 = "Calzado"

ahorro = 0

# Si la forma de pago es Tarjeta, se debe cargar además la cantidad de cuotas elegida.

cuotas = 0

if fp == 2:
    cuotas = int(input("Ingrese la cantidad de cuotas en las que pagará"))

# Promo 3x2 - Si las 3 prendas son del mismo tipo, la de menor valor es gratis.
subtotp = 0

if t1 == t2 == t3:
    pg = min(p1, p2, p3)
    subtotp = subtot - pg
    subtot = subtot - pg
    ahorro = ahorro + pg

# Promo 50% - Si hay 2 prendas del mismo tipo, la de mayor precio tiene 50% de descuento.

if t1 == t2:
    cincDesc = (max(t1,t2)) / 2
    subtot = subtot - cincDesc
    ahorro = ahorro + cincDesc
    subtotp = subtotp - cincDesc
elif t1 == t3:
    cincDesc = (max(t1,t3)) / 2
    subtot = subtot - cincDesc
    ahorro = ahorro + cincDesc
    subtotp = subtotp - cincDesc
elif t2 == t3:
    cincDesc = (max(t2,t3)) / 2
    subtot = subtot - cincDesc
    ahorro = ahorro + cincDesc
    subtotp = subtotp - cincDesc

# Por pago contado se realiza un descuento del 10%.

contDesc = (10*(p1+p2+p3)) / 100

if fp == 1:
    subtot = subtot - contDesc
    ahorro = ahorro + contDesc

# Por pago con tarjeta se recarga 2% si son 3 cuotas o menos, y 5% si son más

if cuotas <= 3:
    subtot = subtot + ((2 * subtot) / 100)
elif cuotas > 3:
    subtot = subtot + ((5 * subtot) / 100)

# las prendas que participen del programa SuperPuntos le dan al cliente
# tantos puntos como indica su precio de venta.
# En caso de que las 3 prendas participen del programa, los puntos se
# duplican.

if s1 == "s" and s2 == "s" and s3 == "s":
    sp = tsp*2
else:
    sp = tsp

# prints

print("---------------------------------------------------------")
print("----")
print("TIENDA ELEGANCIA\nTipo Precio Superpuntos")
print(tt1, p1, s1)
print(tt2, p2, s2)
print(tt3, p3, s3)
print("Total sin promo: $", tsp)
print("Ahorro: $", ahorro)
print("Total con promo: $", subtotp)
if fp == 1:
    print("Forma de pago: Contado (10% de descuento)")
else:
    print("Forma de pago: Tarjeta (", cuotas, "cuotas)")
print("Monto a pagar: $", subtot)
print("Usted obtiene", sp, "SuperPuntos.")