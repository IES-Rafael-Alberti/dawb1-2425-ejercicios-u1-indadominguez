# ejercicio 16

precio_habitual = 3.49

descuento = 0.60

def main():
    
    try:
        num_barras = int(input("Introduce el número de barras que no son del día: "))
        if num_barras < 0:
            print("El numero de barras no puede ser negativo. ")
            return
        
        precio_con_descuento = precio_habitual * (1 - descuento)

        coste_total = precio_con_descuento * num_barras

        print(f"El precio de la barra de pan habitual: {precio_habitual:.2f}€ ")
        print(f"El precio de descuento por no ser fresca: {descuento * 100}% ")
        print(f"El Precio de la barra de pan con descuento: {coste_total:.2f}€ ")

    except ValueError:
        print("Por favor, introduce un número válido. ")

if __name__ == "__main__":
    main()

    
