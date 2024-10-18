# ejercicio 2_def

def calcular_importe_total(horas_trabajo, precio_por_hora):
    return horas_trabajo * precio_por_hora

def main():
    horas_trabajo = float(input("Introduce las horas de trabajo: "))
    precio_por_hora = float(input("Introduce el precio por hora: "))
    
    importe_total = calcular_importe_total(horas_trabajo, precio_por_hora)
    
    print(f"El importe total del servicio es: {importe_total:.2f}")

if __name__ == "__main__":
    main()