# Función para mostrar el menú y obtener la elección del usuario
def mostrar_menu():
    print("\n--- Calculadora Simple ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("--------------------------")
    opcion = input("Elige una opción (1-5): ")
    return opcion

# Bucle principal de la calculadora
while True: # Esto creará un bucle infinito que solo se detendrá cuando el usuario elija "Salir"
    opcion_elegida = mostrar_menu()

    # Si el usuario elige salir, rompemos el bucle
    if opcion_elegida == '5':
        print("¡Gracias por usar la calculadora! Adiós.")
        break # 'break' sale del bucle 'while'

    # Pedir los números (solo si no eligió salir)
    try:
        num1_str = input("Introduce el primer número: ")
        num1 = float(num1_str)

        num2_str = input("Introduce el segundo número: ")
        num2 = float(num2_str)
    except ValueError: # Manejo de errores: si el usuario no introduce un número válido
        print("Error: Por favor, introduce solo números válidos.")
        continue # 'continue' salta al siguiente ciclo del bucle (vuelve a mostrar el menú)

    # Realizar la operación según la opción elegida
    if opcion_elegida == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion_elegida == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion_elegida == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion_elegida == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else: # Si la opción no es válida
        print("Opción no válida. Por favor, elige un número del 1 al 5.")

    input("\nPulsa Enter para continuar...") # Pausa para que el usuario pueda ver el resultado