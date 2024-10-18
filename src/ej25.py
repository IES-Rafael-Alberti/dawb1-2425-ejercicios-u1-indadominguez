# ejercicio 25

fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa por favor: ")

fecha_nacimiento = fecha_nacimiento.replace('/', ' ')

partes_fecha = fecha_nacimiento.split()


if len(partes_fecha) != 3:
    print("**ERROR!** por favor introduce la fecha en formato dd/mm/aaaa.")
else:
    dia = partes_fecha[0].zfill(2)  
    mes = partes_fecha[1].zfill(2)  
    año = partes_fecha[2]

    
    print(f"Día: {dia}, Mes: {mes}, Año: {año}")