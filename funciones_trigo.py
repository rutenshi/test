import math

def factorial_function(num):
   factorial = 1
   if num < 0:
      print("No existe factorial para números negativos")
   elif num == 0:
      print("El factorial de 0 es 1")
   else:
      for i in range(1, num + 1):
         factorial *= i
      print(f"El factorial de {num} es {factorial}")
   return factorial

def my_sin(theta):
   theta = (theta + math.pi) % (2 * math.pi) - math.pi
   resultado = 0
   signo = 1
   potencia = 1
   
   for i in range(10):
      resultado += ((theta**potencia) / factorial_function(potencia)) * signo
      signo *= -1
      potencia += 2
   return resultado

def my_cos(theta):
   theta = (theta + math.pi) % (2 * math.pi) - math.pi
   resultado = 0
   signo = 1
   potencia = 0
   
   for i in range(10):
      resultado += ((theta**potencia) / factorial_function(potencia)) * signo
      signo *= -1
      potencia += 2
   return resultado
   
def my_tan(theta):
   tan = my_sin(theta)/my_cos(theta)
   return tan


print(my_sin(101))
print(math.sin(101))

print(my_cos(101))
print(math.cos(101))

print(my_tan(101))
print(math.tan(101))