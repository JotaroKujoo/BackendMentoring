isOn = True

while isOn:
    word = input("Introduce una palabra: ")



    def analyze_word(word):
        print("Texto original: ",word)
        print("Primer caracter: ",word[0])


    if len(word) > 0:
        analyze_word(word)
        print("Que deseas hacer? \n 1. Reintentar \n 2. Salir")
        if option == 1:
            print("Reintentando...")
        if option == 2:
            print("Cerrando el programa")
            isOn = False
    else:
        print("La palabra debe contener al menos 1 caracter para ser evaluada")
        print("Que deseas hacer? \n 1. Reintentar \n 2. Salir")
        option = int(input("Introduce la opcion: "))
        if option == 1:
            print("Reintentando...")
        if option == 2:
            print("Cerrando el programa")
            isOn = False