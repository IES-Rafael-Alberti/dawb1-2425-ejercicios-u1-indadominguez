# ejercicio 1_def

def dar_bienvenida(nombre):
    
    return f"Hola, {nombre}!"

if __name__ == "__main__":

    nombre_usuario = input("Por favor, ingresa tu nombre: ")


    mensaje_bienvenida = dar_bienvenida(nombre_usuario)


    print(mensaje_bienvenida)