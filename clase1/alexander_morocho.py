#Funciones Ejercicio 1

def ejercicio1(peso, talla):
    #Cálculo IMC
    imc = peso / (talla * talla)
    if imc < 18.5:
        mensaje = "Bajo peso"
    if 18.5 <= imc < 24.9:
        mensaje = "Peso saludable"
    if 25 <= imc <= 29.9:
        mensaje = "Sobrepeso"
    if imc >= 30:
        mensaje = "Obesidad"
    return mensaje

#Funciones Ejercicio 2

def numeros():
    #Pedido de números a comparar
    a = int(input("Ingresa el número menor: "))
    b = int(input("Ingresa el número mayor: "))
    return a, b

def entero_positivo(a, b):
    #Validar que son números enteros positivos
    return a > 0 and b > 0

def mayor_menor(a, b):
    #Validar que el primer número sea menor que el segundo
    return b > a

def pares(a, b):
    pares = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            pares.append(num)
    print(f"Cantidad total de números en el intervalo: {b - a + 1}")
    print(f"Números pares entre {a} y {b}: ")
    for p in pares:
        print(p)
    return pares

if __name__ == "__main__":
    #Ejercicio 1
    name = input("Nombre: ")
    edad = input("Edad: ")
    talla = float(input("Talla (m): "))
    peso = float(input("Peso (kg): "))
    
    msn = ejercicio1(peso, talla)
    print(f"Hola {name} tienes {edad} años y estás en: {msn}")
    
    
    #Ejercicio 2
    a, b = numeros()
    
    if not entero_positivo(a, b):
        print("Los números deben ser enteros positivos")
    elif not mayor_menor(a, b):
        print("El primer número debe ser mayor al segundo número")
    else:
        pares(a, b)