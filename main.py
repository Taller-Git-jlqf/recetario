
from recetas import receta_pasta 
from recetas import receta_arrozRojo
from recetas import receta_fresas
from recetas import receta_cereal
from recetas import receta_sandwich
from recetas import receta_costillas
from recetas import receta_kanka
from recetas import receta_salmon
from recetas import receta_carlota


# Aquí se irán importando más recetas a medida que se agreguen
def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("11. Arroz rojo")
    print("4. Fresas con Crema")
    print("3. Cereal con leche")
    print("5. Costillas de cerdo a la BBQ")
    print("6. Sandwich de jamon")
    print("30. kanka")
    print("20. Salmon")
    print("21. carlota")
    # Agrega aquí tu receta con un número nuevo


    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "11":
        receta_arrozRojo()
    elif opcion == "4":
        receta_fresas()
    elif opcion == "3":
        receta_cereal()
    elif opcion == "6":
        receta_sandwich()
    elif opcion == "5":
        receta_costillas()
    elif opcion == "30":
        receta_kanka()
    elif opcion == "20":
        receta_salmon()
    elif opcion == "21":
        receta_carlota()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

