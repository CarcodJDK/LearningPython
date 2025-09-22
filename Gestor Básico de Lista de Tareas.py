#GESTOR

# Lista para almacenar nuestras tareas
# ¡Empieza con algunas tareas de ejemplo o déjala vacía!
lista_de_tareas = ["Aprender Python", "Aprender Python aplicado a scripting", "Aprender Python aplicado a Sistemas + Cloud"]

# --- Función para mostrar el menú ---
def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Marcar tarea como completada") # O "Eliminar tarea"
    print("4. Salir")
    print("------------------------")
    opcion = input("Elige una opción (1-4): ")
    return opcion

# --- Bucle principal del programa ---
while True:
    opcion_elegida = mostrar_menu()

    if opcion_elegida == '1':
        print("\n--- Tareas pendientes ---")
        if not lista_de_tareas #Comprobación para ver si la lista está vacía
            print("No hay tareas pendientes en tu lista")
        else 
            for indice, tarea in enumerate(lista_de_tareas):
                 # 'enumerate' nos da el índice (posición) y el valor (la tarea)
                # Sumamos 1 al índice para que la numeración empiece en 1 (para el usuario)
                print(f"{indice + 1}. {tarea}")
        print("----------------------------")       
        # --- LÓGICA PARA VER TAREAS ---
        # Usa un bucle 'for' con 'enumerate' para imprimir cada tarea numerada
        # Si la lista está vacía, imprime un mensaje.
        pass # 'pass' es un marcador de posición, quítalo cuando escribas tu código aquí
        
    elif opcion_elegida == '2':
        # --- LÓGICA PARA AÑADIR TAREA ---
        # Pide al usuario la nueva tarea con input()
        # Usa .append() para añadirla a 'lista_de_tareas'
        pass

    elif opcion_elegida == '3':
        # --- LÓGICA PARA MARCAR/ELIMINAR TAREA ---
        # Primero, muestra de nuevo las tareas numeradas para que el usuario sepa qué número elegir.
        # Pide al usuario el número de la tarea a eliminar (recuerda la conversión a int y el índice -1).
        # Usa try/except para manejar ValueError (si no es un número) e IndexError (si el número está fuera de rango).
        # Si todo es correcto, usa 'del lista_de_tareas[indice]' para eliminarla.
        pass

    elif opcion_elegida == '4':
        print("¡Adiós! Que tengas un gran día.")
        break # Salir del bucle y del programa

    else:
        print("Opción no válida. Por favor, elige un número del 1 al 4.")

    input("\nPulsa Enter para continuar...") # Pausa para que el usuario pueda ver el resultado1