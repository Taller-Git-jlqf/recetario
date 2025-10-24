from recetas import receta_pasta
from recetas import receta_sandwich
from recetas import receta_costillas
from recetas import receta_salmon

# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("5. Costillas de cerdo a la BBQ")
    print("6. Sandwich de jamon")
    print("20. Salmon")
    # Agrega aquí tu receta con un número nuevo

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "6":
        receta_sandwich()
    elif opcion == "5":
        receta_costillas()
    elif opcion == "20":
        receta_salmon()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
