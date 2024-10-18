# ejercicio 16

precio_habitual = 3.49

descuento_porcentaje = 0.60


num_barras_no_frescas = int(input("Introduce el número de barras de pan no frescas vendidas: "))


descuento = precio_habitual * descuento_porcentaje


precio_con_descuento = precio_habitual - descuento


coste_total = precio_con_descuento * num_barras_no_frescas


print(f"Precio habitual de una barra de pan: {precio_habitual:.2f}€")
print(f"Descuento por no ser fresca: {descuento:.2f}€")
print(f"Coste total de las barras no frescas: {coste_total:.2f}€")

    
