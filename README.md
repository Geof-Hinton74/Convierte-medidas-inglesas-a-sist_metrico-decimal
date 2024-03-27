def main():print("Convierte Medidas Inglesas a sistema metrico decimal")     # El programa te va preguntar que vas a convertir : Millas? / pies? / pulgadas? 
millas = float(input("Cuantas Millas?:"))
pies = float(input("Y Cuantos Pies?:"))
pulgadas = float(input("Y Cuantas Pulgadas?:"))
metros = float(1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas)        # Cuando se te pregunte, selecciona una opcion es decir si quieres convertir,
                                                                             # millas solamente type: la cantidad de millas,y las demas lo dejas en cero.
                                                                             # Ejemplo si quiero convertir 5 millas a metros; Cuantas Millas?: 5
                                                                             #                                                Cuantos pies?: 0
                                                                             #                                                Cuantas pulgadas?: 0
                                                                             #  Y obtendras como resultado 8046.72 metros
print("La longitud es de",metros,"metros")
main()
