isOn = True

while isOn:
    word = input("Introduce una palabra: ")
    
    def displayWord(word):
        print("Texto original: ",word)
    
    def displayFirstLetter(word):
        print("Primer caracter: ",word[0])

    def displayLastLetter(word):
        print("Ultimo caracter: ",word[-1])

    def displayFirst4Letters(word):
        print("Primeros 4 caracteres: ", word[:4])
    
    def displayLast4Letters(word):
        print("ultimos 4 caracteres: ", word[-4:])
        
    def displayInvertedWord(word):
        inverted= ""
        for letter in word:
            inverted = letter + inverted
        
        print("Texto invertido: ", inverted)
    
    def displayWordLenght(word):
        print("Numero de caracteres: ", len(word))
        
    def displayEvenIndex(word):
        print("Caracteres en posiciones pares")
        for index, caracter in enumerate(word):
            if index%2==0:
                print(caracter)
    
    def displayNonEvenIndex(word):
        print("Caracteres en posiciones impares")
        for index, caracter in enumerate(word):
            if index%2!=0:
                print(caracter)
        
    def analyze_word(word):
        displayWord(word)
        displayFirstLetter(word)
        displayLastLetter(word)
        displayFirst4Letters(word)
        displayLast4Letters(word)
        displayInvertedWord(word)
        displayWordLenght(word)
        displayEvenIndex(word)    
        displayNonEvenIndex(word)
                


    if len(word) > 0 & word.isalpha():
        analyze_word(word)
        print("Que deseas hacer? \n 1. Reintentar \n 2. Salir")
        option = int(input("Introduce la opcion: "))
        if option == 1:
            print("Reintentando...")
        if option == 2:
            print("Cerrando el programa")
            isOn = False
    else:
        print("La palabra debe contener al menos 1 caracter para ser evaluada y no debe contener numeros")
        print("Que deseas hacer? \n 1. Reintentar \n 2. Salir")
        option = int(input("Introduce la opcion: "))
        if option == 1:
            print("Reintentando...")
        if option == 2:
            print("Cerrando el programa")
            isOn = False