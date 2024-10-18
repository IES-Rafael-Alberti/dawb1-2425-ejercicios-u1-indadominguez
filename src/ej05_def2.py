# ejercicio 5_def__2

def calcula_precio(importe: float, iva: float) -> str:
    
    if iva < 0 or iva > 100:
        iva = 21  
    
    
    iva_calculado = importe * (iva / 100)
    
    precio_final = importe + iva_calculado
    
    
    return f"El precio final del artículo con IVA ({iva:.2f}) es {precio_final:.2f}€."

def main():
    
   
    importe = float(input("Introduce el importe sin IVA del artículo: "))
    
    iva = float(input("Introduce el tipo de IVA a aplicar (en %): "))
    
    
    resultado = calcula_precio(importe, iva)
    
    print(resultado)


if __name__ == "__main__":
    main()