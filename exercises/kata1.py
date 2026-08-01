is_on = True

    
def analyze_word(word):
    print("Texto original: ", word)
    print("Primer caracter: ", word[0])
    print("Ultimo caracter: ", word[-1])
    print("Primeros 4 caracteres: ", word[:4])
    print("ultimos 4 caracteres: ", word[-4:])
    print("Cada dos valores: ", word[::2])
    
    inverted= ""
    for letter in word:
        inverted = letter + inverted
    
    print("Texto invertido: ", inverted)
    
    print("Numero de caracteres: ", len(word))
    print("Caracteres en posiciones pares")
    
    for index, caracter in enumerate(word):
        if index % 2 == 0:
            print(caracter)
    print("Caracteres en posiciones impares")
    
    for index, caracter in enumerate(word):
        if index % 2 != 0:
            print(caracter)

def choice_selector():
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
        print("Que deseas hacer? \n 1. Reintentar \n 2. Salir")
        print(f"\nTienes {(max_intentos - intentos)} intentos")
        try:
            option = int(input("\nIntroduce la opcion: "))
            
        except ValueError:
            print("\nDebes introducir un numero")
            intentos += 1    
            continue
          
        if option == 1:
            print("\nReintentando...")
            return True
        
        elif option == 2:
            print("Cerrando el programa")
            return False
    
        else:
            intentos += 1
            print("\nOpcion no valida")
            
    
        
    print("Demasiados intentos, cerrando..")
    return False

while is_on:
    word = input("Introduce una palabra: ")
    if word.isalpha():
        analyze_word(word)
        is_on = choice_selector()
    else:
        print("La palabra debe contener al menos 1 caracter para ser evaluada y no debe contener numeros")
        is_on = choice_selector()