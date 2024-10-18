# ejercicio 23

correo_usuario = input("Introduce su correo electrónico: ")

nombre, dominio = correo_usuario.split("@")

nuevo_correo = f"{nombre}@ceu.es"

print(f"Nuevo correo electrónico es: {nuevo_correo}")