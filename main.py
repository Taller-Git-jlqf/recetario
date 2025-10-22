from recetas import receta_pasta
from recetas import receta_sandwich
from recetas import receta_costillas
from recetas import receta_helado

# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("2. Helado de vainilla")
    print("5. Costillas de cerdo a la BBQ")
    print("6. Sandwich de jamon")

    # Agrega aquí tu receta con un número nuevo

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "2":
        receta_helado()
    elif opcion == "6":
        receta_sandwich()
    elif opcion == "5":
        receta_costillas()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
