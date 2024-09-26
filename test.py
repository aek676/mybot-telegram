import readline

def main():
    # Configuración de readline
    readline.set_startup_hook(lambda: readline.insert_text("Texto inicial. "))

    try:
        # Leer la entrada del usuario
        entrada = input("Escribe algo: ")
    finally:
        # Limpiar el hook de inicio
        readline.set_startup_hook()

    print("Texto ingresado:", entrada)

# Ejecutar el programa
if __name__ == "__main__":
    main()
