precio_original = float(input("Ingrese el precio original del producto: "))

porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

monto_descuento = (porcentaje_descuento / 100) * precio_original

precio_final = precio_original - monto_descuento

print(f"El precio final después de aplicar el descuento es: ${precio_final:.2f}")
print("\n")
