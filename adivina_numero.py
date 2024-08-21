import random

def adivina_el_numero():
    print("¡Bienvenido al juego de adivinanza de números!")
    
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    # Número máximo de intentos
    intentos = 10
    
    print("He escogido un número entre 1 y 100. ¡Tienes 10 intentos para adivinarlo!")
    
    for intento in range(1, intentos + 1):
        # Pedirle al usuario que ingrese un número
        try:
            adivinanza = int(input(f"Intento {intento}: ¿Cuál es tu adivinanza? "))
            
            if adivinanza < 1 or adivinanza > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            # Comparar la adivinanza con el número secreto
            if adivinanza < numero_secreto:
                print("Demasiado bajo. ¡Intenta con un número más alto!")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. ¡Intenta con un número más bajo!")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intento} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    else:
        print(f"Lo siento, te has quedado sin intentos. El número era {numero_secreto}.")

# Ejecutar el juego
if __name__ == "__main__":
    adivina_el_numero()
