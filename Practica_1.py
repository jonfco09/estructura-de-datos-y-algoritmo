#1. Calcula el área de un rectángulo. Pide al usuario que ingrese el largo y el ancho, y luego muestra el área.

print()
print("1. Calcula el área de un rectángulo. Pide al usuario que ingrese el largo y el ancho, y luego muestra el área.")
print()
base = float(input("Introduzca la base de su rectagulo en cm: "))
altura = float(input("Introduzca el altura su rectagulo en cm: "))
area = base * altura

print("El área de su rectangulo es: ", area, "cm²")
print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

#2. Convierte grados Celsius a Fahrenheit. Pide al usuario que ingrese la temperatura en Celsius y muestra el resultado en Fahrenheit.

print("2. Convierte grados Celsius a Fahrenheit. Pide al usuario que ingrese la temperatura en Celsius y muestra el resultado en Fahrenheit.")
print()
celsius = float(input("Introduzca la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("La temperatura en Fahrenheit es: ", fahrenheit, "°F")

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

#3. Suma dos números complejos. Define dos números complejos y muestra el resultado de su suma.

print("3. Suma dos números complejos. Define dos números complejos y muestra el resultado de su suma.")
print()
num1 = complex(2, 3)  # 2 + 3i
num2 = complex(4, 5)  # 4 + 5i
suma = num1 + num2
print("La suma de los números complejos es: ", suma)

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

#4. Pide al usuario que ingrese su nombre y luego muestra un mensaje de bienvenida

print("4. Pide al usuario que ingrese su nombre y luego muestra un mensaje de bienvenida")
print()
nombre = input("Introduzca su nombre: ")
print("Bienvenido, ", nombre)

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

#5. Pide al usuario que ingrese su edad y determina si es mayor de edad (18 años o más).

print("5. Pide al usuario que ingrese su edad y determina si es mayor de edad (18 años o más).")
print()
edad = int(input("Introduzca su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")   

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

# 6. Escribe un programa que pida al usuario dos números y muestre la suma,resta, multiplicación y división de esos números.

print("6. Escribe un programa que pida al usuario dos números y muestre la suma, resta, multiplicación y división de esos números.")
print()
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2    
division = num1 / num2 if num2 != 0 else "Error: División por cero"
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

# 7. Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero.

print("7. Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero.")
print()
numero = float(input("Introduzca un número: "))
if numero > 0:
    print("El número es positivo.") 
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()
# 8. Escribe un programa que pida al usuario un número y determine si es par o impar.

print("8. Escribe un programa que pida al usuario un número y determine si es par o impar.")
print()
numero = int(input("Introduzca un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

print()
print("--------------------------------------------------------------------------")

# 9. Escribe un programa que imprima los números del 1 al 10 usando un bucle for.

print("9. Escribe un programa que imprima los números del 1 al 10 usando un bucle for.")
print()
for i in range(1, 11):
    print(i)

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

# 10. Escribe un programa que sume números ingresados por el usuario hasta que ingrese 0.

print("10. Escribe un programa que sume números ingresados por el usuario hasta que ingrese 0.")
print()
suma = 0
while True:
    numero = float(input("Introduzca un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
print("La suma total es: ", suma)

print()
print("-------------------- Gracias por llegar al final --------------------")
print()

