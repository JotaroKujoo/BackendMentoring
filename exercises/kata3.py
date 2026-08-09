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


def remove_item_handler(equipment):
    attempts_handler = 0
    max_attempts_handler = 3

    while attempts_handler < max_attempts_handler:
        item = normalize_word(input("Que objeto deseas eliminar?\n"))
        if item.isalpha():
            if validate_item_in_equipment(item, equipment):
                remove_item_from_equipment(item, equipment)
                print(f"{item} ha sido eliminado/a con exito")
                return
            else:
                print("El objeto no se encuentra en la mochila")
                attempts_handler += 1
                print(f"Intentos restantes {max_attempts_handler - attempts_handler}")
        else:
            print("Debe ser una palabra sin espacios, caracteres especiales ni numeros")
            attempts_handler += 1
            print(f"Intentos restantes {max_attempts_handler - attempts_handler}")
    print("Demasiados intentos, saliendo...")


def add_item_to_equipment(item, equipment):
    equipment.append(item)


def add_item_handler(equipment):
    attempts_handler = 0
    max_attempts_handler = 3

    while attempts_handler < max_attempts_handler:
        item = normalize_word(input("Que objeto deseas añadir?\n"))
        if item.isalpha():
            if not validate_item_in_equipment(item, equipment):
                add_item_to_equipment(item, equipment)
                print(f"{item} ha sido añadido/a con exito")
                return
            else:
                print("El objeto ya se encuentra en la mochila")
                attempts_handler += 1
                print(f"Intentos restantes {max_attempts_handler - attempts_handler}")
        else:
            print("Debe ser una palabra sin espacios, caracteres especiales ni numeros")
            attempts_handler += 1
            print(f"Intentos restantes {max_attempts_handler - attempts_handler}")
    print("Demasiados intentos, saliendo...")


def replace_item_from_equipment(item1, item2, equipment):
    equipment[equipment.index(item1)] = item2
    print(equipment)


def replace_item_handler(equipment):
    attempts_handler = 0
    max_attempts_handler = 3

    while attempts_handler < max_attempts_handler:
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
                        attempts_handler += 1
                else:
                    print(
                        "Debe ser una palabra sin espacios, caracteres especiales ni numeros"
                    )
                    attempts_handler += 1
                    print(
                        f"Intentos restantes {max_attempts_handler - attempts_handler}"
                    )
                return
            else:
                print("El objeto no se encuentra en la mochila")
                attempts_handler += 1
                print(f"Intentos restantes {max_attempts_handler - attempts_handler}")
        else:
            print("Debe ser una palabra sin espacios, caracteres especiales ni numeros")
            attempts_handler += 1
            print(f"Intentos restantes {max_attempts_handler - attempts_handler}")
    print("Demasiados intentos, saliendo...")


def main(equipment):
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        display_menu()
        try:
            choice = int(input("Introduce una opcion: "))
        except ValueError:
            print("Introduce un numero por favor")
            attempts += 1
            continue

        match choice:
            case 1:
                show_equipment(equipment)
                attempts = 0
            case 2:
                add_item_handler(equipment)
                attempts = 0
            case 3:
                remove_item_handler(equipment)
                attempts = 0
            case 4:
                replace_item_handler(equipment)
                attempts = 0
            case 8:
                print("Saliendo...")
                return
            case _:
                print("Opcion erronea")
                attempts += 1
                print(f"Intentos restantes: {max_attempts - attempts}")


main(equipment)
