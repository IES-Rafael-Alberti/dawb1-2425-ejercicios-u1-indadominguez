
def comprobar_entero(cadena: str):
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())
    

def dame_entero():
    cadena = input("Escribe un numero entero: ")
    
    while not comprobar_entero(cadena):
        cadena = input("**ERROR** Eso no es un entero!!!\n\nEscribe un numero entero otra vez: ")

    return int(cadena)
    
def main():
    num = dame_entero()
    print(f"Has introducido el numero {num}")

if __name__== "__main__":
    main()
        
        
    