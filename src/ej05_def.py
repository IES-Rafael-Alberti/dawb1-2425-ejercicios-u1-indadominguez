# ejercicio 5_def

def calcular_precio_final(importe_sin_iva, tipo_iva):
    
    iva = importe_sin_iva * (tipo_iva / 100)
    
    
    precio_final = importe_sin_iva + iva
    
    
    print(f"El precio final del artículo es: {precio_final:.2f} (IVA incluido)")

def main():
    
    importe_sin_iva = float(input("Introduce el importe sin IVA del artículo: "))
    
    
    tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en %): "))
    
    
    calcular_precio_final(importe_sin_iva, tipo_iva)

if __name__ == "__main__":
    main()