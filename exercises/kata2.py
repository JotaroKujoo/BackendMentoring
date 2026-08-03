stock = ["espada", "escudo", "arco"]

def show_stock(stock):
    print(stock)

def add_element_to_stock(stock):
    item = input("Que objeto quieres añadir?: ")
    
    if item.isalpha():
        if item not in stock:
            stock.append(item.lower())
            print("El objeto ha sido añadido con exito al inventario")
        else:
            print("El objeto ya esta en el inventario")
    else:
        print("Error, introduce un palabra solo con letras")
        

def choice_selector(attempts, max_attempts):
    while attempts < max_attempts:
        print("\n1. Ver stock \n2. Añadir objeto \n3. Salir")
        try:
            option = int(input("Introduce una opcion: "))
        except ValueError:
            attempts += 1
            print(f"introduce un numero por favor, te quedan {(max_attempts-attempts)} intentos")
            continue
        
        if option == 1:
            show_stock(stock)
        elif option == 2:
            add_element_to_stock(stock)
        elif option == 3:
            return False
        else:
            attempts += 1
            print(f"Opcion erronena, te quedan {(max_attempts-attempts)} intentos")
    print("Demasiados intentos, saliendo...")
    
def main(stock):
    is_on = True
    attempts = 0
    max_attempts = 3
    
    
    while is_on:
        print("Bienvenido a tu inventario")
        show_stock(stock)
        print("Que deseas hacer?")
        is_on = choice_selector(attempts, max_attempts)
        
        
main(stock)