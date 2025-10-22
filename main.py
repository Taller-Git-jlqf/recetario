from recetas import receta_pasta
from recetas import receta_fresas

# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("4. Fresas con Crema")
    # Agrega aquí tu receta con un número nuevo

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "4":
        receta_fresas()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
