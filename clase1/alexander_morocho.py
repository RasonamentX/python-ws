#Ejercicio 1

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

def ingreso():
    #Pedido de números a comparar
    a = input("Ingresa el número menor: ")
    b = input("Ingresa el número mayor: ")

if __name__ == "__main__":
    #Pedido de datos a usuario
    name = input("Nombre: ")
    edad = input("Edad: ")
    talla = float(input("Talla (m): "))
    peso = float(input("Peso (kg): "))
    
    msn = ejercicio1(peso, talla)
    print(f"Hola {name} tienes {edad} años y estás en: {msn}")


