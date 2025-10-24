from recetas import receta_pasta, receta_arroz_con_leche, receta_carlota 

# Aquí se irán importando más recetas a medida que se agreguen
def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("2. Arroz con leche")
    print("3. Carlota")

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "2":
        receta_arroz_con_leche()
    elif opcion == "3":
        receta_carlota()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

