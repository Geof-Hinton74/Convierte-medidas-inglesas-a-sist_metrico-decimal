def main():print("Convierte Medidas Inglesas a sistema metrico decimal")
millas = float(input("Cuantas Millas?:"))
pies = float(input("Y Cuantos Pies?:"))
pulgadas = float(input("Y Cuantas Pulgadas?:"))
metros = float(1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas)
print("La longitud es de",metros,"metros")
main()

