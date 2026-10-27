#Versión mejorada:

DESCUENTO_BAJO = 0.05
DESCUENTO_MEDIO = 0.10
DESCUENTO_ALTO = 0.15



monto_compra = float(input("Ingrese el monto de la compra: ₡"))

if monto_compra >= 100000:
    porcentaje_descuento = DESCUENTO_ALTO
elif monto_compra >= 60000:
    porcentaje_descuento = DESCUENTO_MEDIO
elif monto_compra >= 30000:
    porcentaje_descuento = DESCUENTO_BAJO
else:
    porcentaje_descuento = 0

monto_descuento = monto_compra * porcentaje_descuento
total_pagar = monto_compra - monto_descuento

print("Descuento: ₡", monto_descuento)
print("Total a pagar: ₡", total_pagar)
