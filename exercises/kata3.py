equipment = ["cuerda", "antorcha", "mapa", "agua", "comida"]


def normalize_word(word):
    return word.strip().lower()


def show_equipment(equipment):
    for index, element in enumerate(equipment):
        print(f"{index + 1}. {element}")


def display_menu():
    print("""
   ===== EXPEDICIÓN =====
        1. Mostrar equipo
        2. Añadir objeto
        3. Retirar objeto
        4. Reemplazar objeto
        5. Mover objeto
        6. Mostrar una sección
        7. Crear mochila de reserva
        8. Salir
        """)


def validate_item_in_equipment(item, equipment):
    return item in equipment


def remove_item_from_equipment(item, equipment):
    equipment.remove(item)


def error_handler():
    while True:
        print("""
              
        ===== ERROR =====
            1. Reintentar
            2. Salir
            
            """)

        try:
            option = int(input("Introduce una opcion: "))

        except ValueError:
            print("La opcion debe ser un numero")
            continue

        match option:
            case 1:
                return True
            case 2:
                return False
            case _:
                print("Opcion invalida")


def remove_item_handler(equipment):
    is_on = True

    while is_on:
        item = normalize_word(input("Que objeto deseas eliminar?\n"))
        if item.isalpha():
            if validate_item_in_equipment(item, equipment):
                remove_item_from_equipment(item, equipment)
                print(f"{item} ha sido eliminado/a con exito")
                return
            else:
                print("El objeto no se encuentra en la mochila")
                is_on = error_handler()
        else:
            print("Debe ser una palabra sin espacios, caracteres especiales ni numeros")
            is_on = error_handler()
    print("Saliendo...")


def add_item_to_equipment(item, equipment):
    equipment.append(item)


def add_item_handler(equipment):
    is_on = True

    while is_on:
        item = normalize_word(input("Que objeto deseas añadir?\n"))
        if item.isalpha():
            if not validate_item_in_equipment(item, equipment):
                add_item_to_equipment(item, equipment)
                print(f"{item} ha sido añadido/a con exito")
                return
            else:
                print("El objeto ya se encuentra en la mochila")
                is_on = error_handler()
        else:
            print("Debe ser una palabra sin espacios, caracteres especiales ni numeros")
            is_on = error_handler()
    print("Saliendo...")


def replace_item_from_equipment(item1, item2, equipment):
    equipment[equipment.index(item1)] = item2


def replace_item_handler(equipment):
    is_on = True

    while is_on:
        item1 = normalize_word(input("Que objeto deseas reemplazar?\n"))

        if item1.isalpha():
            if validate_item_in_equipment(item1, equipment):

                item2 = normalize_word(input("Que objeto deseas añadir en su lugar?\n"))

                if item2.isalpha():
                    if not validate_item_in_equipment(item2, equipment):
                        replace_item_from_equipment(item1, item2, equipment)
                        print(f"El objeto {item1} ha sido  reemplazado por {item2}")
                        return
                    else:
                        print(
                            "El objeto ya se encuentra en el inventario, no es posible crear duplicados"
                        )
                        is_on = error_handler()
                else:
                    print(
                        "Debe ser una palabra sin espacios, caracteres especiales ni numeros"
                    )
                    is_on = error_handler()
            else:
                print("El objeto no se encuentra en la mochila")
                is_on = error_handler()
        else:
            print("Debe ser una palabra sin espacios, caracteres especiales ni numeros")
            is_on = error_handler()
    print("Saliendo...")


def move_item_in_equipment(item, desired_position, equipment):
    item_index = equipment.index(item)
    equipment.pop(item_index)
    equipment.insert(desired_position, item)


def move_items_handler(equipment):
    is_on = True

    while is_on:
        item = input("Primer objeto a intercambiar: ")
        if validate_item_in_equipment(item, equipment):
            desired_position = int(input("A que posicion lo deseas mover"))
            if desired_position < len(equipment):
                move_item_in_equipment(item, desired_position, equipment)
                print("El objeto ha sido movido con exito")
            else:
                print("Introduce una posicion existente")
                is_on = error_handler()
        else:
            print("El objeto no se encuentra en la mochila")
            is_on = error_handler()
    print("Saliendo...")


def main(equipment):
    is_on = True

    while is_on:
        display_menu()
        try:
            choice = int(input("Introduce una opcion: "))
        except ValueError:
            print("Introduce un numero por favor")
            is_on = error_handler()

        match choice:
            case 1:
                show_equipment(equipment)
            case 2:
                add_item_handler(equipment)
            case 3:
                remove_item_handler(equipment)
            case 4:
                replace_item_handler(equipment)
            case 5:
                move_items_handler(equipment)
            case 8:
                print("Saliendo...")
                return
            case _:
                print("Opcion erronea")
                is_on = error_handler()


main(equipment)
