# ejercicio 6 

importe_final = float(input("introduce el importe final del artículo "))

tipo_iva = 0.10

importe_sin_iva = importe_final / (1 + tipo_iva)

iva_pagado = importe_final - importe_sin_iva

print(f"Importe sin IVA: {importe_sin_iva:.2f} €")
print(f"IVA pagado: {iva_pagado:.2f} €") 






   






