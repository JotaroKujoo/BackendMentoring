stock = ["espada", "escudo", "arco"]


# Features
def validate_user_input(item):
    return item.isalpha()


def validate_item_in_stock(stock, item):
    return item in stock


def show_stock(stock):
    if len(stock) > 0:
        for index, item in enumerate(stock):
            print(f"{index+1}. {item}")
    else:
        print("El inventario esta vacio")


def add_element_to_stock(stock):
    item = input("Que objeto quieres añadir?: ").strip().lower()

    if validate_user_input(item):
        if not validate_item_in_stock(stock, item):
            stock.append(item)
            print(f"{item} ha sido añadido/a con exito al inventario\n")
        else:
            print(f"{item} ya se encuentra en el inventario\n")
    else:
        print(
            "\nIntroduce un nombre compuesto únicamente por letras y sin espacios internos y sin espacios\n"
        )


def remove_element_from_stock(stock):
    item = input("Que objeto quieres eliminar?: ").strip().lower()

    if validate_user_input(item):
        if validate_item_in_stock(stock, item):
            stock.remove(item)
            print(f"{item} ha sido eliminado con exito")
        else:
            print("\nObjeto no encontrado en el inventario\n")
    else:
        print(
            "\nIntroduce un nombre compuesto únicamente por letras y sin espacios internos.\n"
        )


def search_element_in_stock(stock):
    item = input("Que objeto quieres buscar?: ").strip().lower()

    if validate_user_input(item):
        if validate_item_in_stock(stock, item):
            print(
                f"El objeto {item} se encuentra en el inventario en la posicion {stock.index(item)+1}\n"
            )
        else:
            print(f"El objeto {item} no se encuentra en el inventario")
    else:
        print(
            "Introduce un nombre compuesto únicamente por letras y sin espacios internos\n"
        )


# Selector function
def choice_selector(stock):
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print(
            "\n1. Ver stock \n2. Añadir objeto \n3. Eliminar objeto \n4. Buscar objeto \n5. Salir\n"
        )
        try:
            option = int(input("Introduce una opcion: "))
        except ValueError:
            attempts += 1
            print(
                f"introduce un numero por favor, te quedan {max_attempts-attempts} intentos\n"
            )
            continue

        match option:
            case 1:
                show_stock(stock)
                attempts = 0
            case 2:
                add_element_to_stock(stock)
                attempts = 0
            case 3:
                remove_element_from_stock(stock)
                attempts = 0
            case 4:
                search_element_in_stock(stock)
                attempts = 0
            case 5:
                print("Saliendo del programa...")
                return
            case _:
                attempts += 1
                print(f"Opcion errónea, te quedan {(max_attempts-attempts)} intentos")

    print("Demasiados intentos, saliendo...")
    return False


# Main function
def main(stock):
    print("Bienvenido a tu inventario")
    print("Que deseas hacer?")
    choice_selector(stock)


main(stock)
