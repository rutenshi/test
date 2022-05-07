# Agricultura de precisión
import math
import msvcrt as m

x_grados = int(input("Longitud (grados): "))
x_minutos = int(input("Longitud (minutos): "))
x_segundos = int(input("Longitud (segundos): "))
longitud = input("Este ('E') o Oeste ('W'): ").upper()

y_grados = int(input("Latitud (grados): "))
y_minutos = int(input("Latitud (minutos): "))
y_segundos = int(input("Latitud (segundos): "))
latitud = input("Norte ('N') o Sur ('S'): ").upper()

a = 6378137
b = 6356752.31424518
e = 0.081819191
e_prima = 0.082094438
e_prima_2 = 6.739496742e-03
c = 6399593.626
alfa = 3.352810665e-03

# Grados decimales
longitud_decimal = x_grados + (x_minutos/60) + (x_segundos/3600)
latitud_decimal = y_grados + (y_minutos/60) + (y_segundos/3600)

if longitud == 'W':
	longitud_decimal *= (-1)
if latitud == 'S':
	latitud_decimal *=(-1)

#print(f"Longitud decimal: {longitud_decimal}")
#print(f"Latitud decimal: {latitud_decimal}")

# Grados radianes
longitud_radianes = longitud_decimal*(math.pi/180)
latitud_radianes = latitud_decimal*(math.pi/180)

#print(f"Longitud radianes: {longitud_radianes}")
#print(f"Latitud radianes: {latitud_radianes}")

huso = (longitud_decimal/6)+31
huso = math.floor(huso)
#print(f"Huso: {huso}")


meridianoc = (huso*6)-183
distanciaa = longitud_radianes-(meridianoc*math.pi/180)

#print(f"Meridiano central: {meridianoc}")
#print(f"Distancia angular: {distanciaa}")

# Parámetros Coticchia-Surace 

A = math.cos(latitud_radianes)*math.sin(distanciaa)
#print(f"A = {A}")

epsilon = (1/2)*math.log((1+A)/(1-A))
#print(f"Epsilon = {epsilon}")

n = math.atan((math.tan(latitud_radianes))/(math.cos(distanciaa)))-latitud_radianes
#print(f"n = {n}")

v = (c/(math.sqrt(1+(e_prima_2*math.cos(latitud_radianes)))))*0.9996
#print(f"v = {v}")

zeta = (e_prima_2/2)*epsilon**2*math.cos(latitud_radianes)
#print(f"zeta = {zeta}")

A1 = math.sin(2*latitud_radianes)
#print(f"A1 = {A1}")

A2 = A1 * math.cos(latitud_radianes)**2
#print(f"A2 = {A2}")

J2 = latitud_radianes + A1/2
#print(f"J2 = {J2}")

J4 = (3*J2+A2)/4
#print(f"J4 = {J4}")

J6 = (5*J4+A2*math.cos(latitud_radianes)**2)/3
#print(f"J6 = {J6}")

alpha = 0.75*(e_prima_2)
#print(f"alpha = {alpha}")

beta = (5/3)*(alpha**2)
#print(f"beta = {beta}")

gamma = (35/27)*(alpha**3)
#print(f"gamma = {gamma}")

B = 0.9996*c*(latitud_radianes-alpha*J2+beta*J4-gamma*J6)
#print(f"B = {B}")


# Cálculo Final de Coordenadas
X = epsilon*v*(1+zeta/3)+500000
print(f"X = {X}")
Y = n*v*(1+zeta)+B
print(f"Y = {Y}")

print("Ha finalizado el programa. Presione una tecla para salir...")
m.getch()