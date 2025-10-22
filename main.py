from recetas import receta_pasta
from recetas import receta_chilaquiles
from recetas import receta_costillas


# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("9. receta_chilaquiles")
    print("5. Costillas de cerdo a la BBQ")
    # Agrega aquí tu receta con un número nuevo

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "9":
        receta_chilaquiles()
    elif opcion == "5":
        receta_costillas()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
