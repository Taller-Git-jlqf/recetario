from recetas import receta_pasta
from recetas import receta_helado

# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("2. Helado de vainilla")
    # Agrega aquí tu receta con un número nuevo

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "2":
        receta_helado()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
