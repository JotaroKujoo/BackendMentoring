equipment = ["cuerda", "antorcha", "mapa", "agua", "comida"]
reserve_equipment = []


def normalize_word(word):
    return word.strip().lower()


def show_equipment(equipment, reserve_equipment=reserve_equipment):
    if len(equipment) > 0:
        print("============ MOCHILA PRINCIPAL ============")
        for index, element in enumerate(equipment):
            print(f"{index + 1}. {element}")

    else:
        print("============ MOCHILA PRINCIPAL ============")
        print("La mochila principal esta vacia")

    if len(reserve_equipment) > 0:
        print("============ MOCHILA DE RESERVA ============")
        for index, element in enumerate(reserve_equipment):
            print(f"{index + 1}. {element}")
    else:
        print("============ MOCHILA DE RESERVA ============")
        print("La mochila de reserva esta vacia")


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
    equipment.insert(desired_position - 1, item)


def move_items_handler(equipment):
    is_on = True

    while is_on:
        item = normalize_word(input("Primer objeto a intercambiar: "))
        if validate_item_in_equipment(item, equipment):
            try:
                desired_position = int(input("A que posicion lo deseas mover"))
            except ValueError:
                print("Introduce un valor numerico")
                is_on = error_handler()
                continue

            if desired_position <= len(equipment) and desired_position > 0:
                move_item_in_equipment(item, desired_position, equipment)
                print("El objeto ha sido movido con exito")
                show_equipment(equipment)
                return
            else:
                print("Introduce una posicion existente")
                is_on = error_handler()
        else:
            print("El objeto no se encuentra en la mochila")
            is_on = error_handler()
    print("Saliendo...")


def show_manual_section(option_1, option_2, equipment):
    start_position = option_1 - 1
    end_position = option_2
    print(equipment[start_position:end_position])


def show_section_handler(equipment):
    is_on = True

    while is_on:
        try:
            option_1 = int(input("Desde donde deberia empezar: "))

        except ValueError:
            print("Introduce una opcion numerica!")
            is_on = error_handler()
            continue

        if option_1 <= len(equipment) and option_1 > 0:
            try:
                option_2 = int(input("Hasta donde deberia terminar: "))

            except ValueError:
                print("Introduce una opcion numerica!")
                is_on = error_handler()
                continue

            if option_2 <= len(equipment) and option_2 > 0 and option_1 <= option_2:
                show_manual_section(option_1, option_2, equipment)
                return
            else:
                print("Opcion fuera del rango!")
                is_on = error_handler()
        else:
            print("Opcion fuera del rango!")
            is_on = error_handler()

    print("Saliendo...")


def create_reserve_equipment(equipment):
    copy_equipment = equipment[:]
    return copy_equipment


def reserve_equipment_handler(equipment):
    is_on = True

    while is_on:
        print("Creando mochila de reserva")
        if len(equipment) > 0:
            reserve_equipment_copy = create_reserve_equipment(equipment)
            print("Mochila de reserva creada")
            print(reserve_equipment_copy)
            print("""
                          
                    ===== AÑADIR OBJETO =====
                        1. Si
                        2. No
                        
                        """)

            try:
                option = int(input("Introduce una opcion: "))
            except ValueError:
                print("Introduce un opcion numerica")
                is_on = error_handler()
                continue
            match option:
                case 1:
                    add_item_handler(reserve_equipment_copy)
                    return reserve_equipment_copy
                case 2:
                    return reserve_equipment_copy
                case _:
                    print("Opcion erronea")
                    is_on = error_handler()
        else:
            print("La mochila esta vacia no es posible crear una reserva")
            return []
    print("Saliendo, en caso de error la mochila de reserva se vaciará")
    return []


def main(equipment, reserve_equipment):
    is_on = True

    while is_on:
        display_menu()
        try:
            choice = int(input("Introduce una opcion: "))
        except ValueError:
            print("Introduce un numero por favor")
            is_on = error_handler()
            continue

        match choice:
            case 1:
                show_equipment(equipment, reserve_equipment)
            case 2:
                add_item_handler(equipment)
            case 3:
                remove_item_handler(equipment)
            case 4:
                replace_item_handler(equipment)
            case 5:
                move_items_handler(equipment)
            case 6:
                show_section_handler(equipment)
            case 7:
                reserve_equipment = reserve_equipment_handler(equipment)
            case 8:
                print("Saliendo...")
                return
            case _:
                print("Opcion erronea")
                is_on = error_handler()


main(equipment, reserve_equipment)
