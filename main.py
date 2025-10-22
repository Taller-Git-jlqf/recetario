from recetas import receta_pasta, receta_arroz_con_leche

# Aquí se irán importando más recetas a medida que se agreguen
def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("2. Arroz con leche")  # Usa número consecutivo y solo espacios

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "2":
        receta_arroz_con_leche()  # Llamada a función, no olvides los paréntesis
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

