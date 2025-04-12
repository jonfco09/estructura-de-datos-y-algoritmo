print()
# 1. Crea una tupla con los nombres de 5 países y muestra el tercer elemento.
print("1. Crea una tupla con los nombres de 5 países y muestra el tercer elemento.")
print()
paises = ("México", "España", "Francia", "Alemania", "Italia")
print("El tercer país es:", paises[2])

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

# 2. Crea un diccionario con información de una persona (nombre, edad, ciudad) y muestra la edad.

print("2. Crea un diccionario con información de una persona (nombre, edad, ciudad) y muestra la edad.")
print()
persona = {
    "nombre": "Jonathan",
    "edad": 33,
    "ciudad": "Puerto Plata"
}

print("La edad de la persona es:", persona["edad"])

print() 
print("------------------------------ Jonathan Francisco ------------------------------")
print()

# 3. Crear una calculadora usando funciones

print("3. Crear una calculadora usando funciones")
print()

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        print("Resultado:", suma(a, b))
    elif opcion == "2":
        print("Resultado:", resta(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")

calculadora()

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()

#4-Crear una calculadora usando bibliotecas

print("4-Crear una calculadora usando bibliotecas")
print()

import math

def calculadora_bibliotecas():
    print("Seleccione una operación usando bibliotecas:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Raíz cuadrada (math.sqrt)")
    print("6. Potencia (math.pow)")
    
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    
    if opcion in ["1", "2", "3", "4"]:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        if opcion == "1":
            print("Resultado:", a + b)
        elif opcion == "2":
            print("Resultado:", a - b)
        elif opcion == "3":
            print("Resultado:", a * b)
        elif opcion == "4":
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Error: División por cero")
    elif opcion == "5":
        num = float(input("Ingrese un número: "))
        print("Resultado:", math.sqrt(num))
    elif opcion == "6":
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        print("Resultado:", math.pow(base, exponente))
    else:
        print("Opción no válida")

calculadora_bibliotecas()

print()
print("------------------------------ Jonathan Francisco ------------------------------")
print()