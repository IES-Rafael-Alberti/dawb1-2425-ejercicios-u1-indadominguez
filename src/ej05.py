# ejercicio 5


def calcular_precio_final(importe_sin_iva, tipo_iva):
    iva = importe_sin_iva * (tipo_iva / 100)
    precio_final = importe_sin_iva + iva
    return precio_final


importe_sin_iva = float(input("Introduce el importe sin IVA del artículo: "))


tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en porcentaje): "))


precio_final = calcular_precio_final(importe_sin_iva, tipo_iva)


print(f"El precio final del artículo, incluyendo IVA, es: {precio_final:.2f} €")