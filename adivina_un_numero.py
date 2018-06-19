number_to_guess = 2
user_number = int(input("Adivina un número: "))

if user_number == number_to_guess:
    print("Has ganado")
else:
    user_number = int(input("No es correcto, elige otro número: "))

    if user_number == number_to_guess:
        print("Has ganado")
    else:
        user_number = int(input("No es correcto, elige otro número: "))

        if user_number == number_to_guess:
            print("Has ganado")
        else:
            user_number = int(input("No es correcto, elige otro número: "))

            if user_number == number_to_guess:
                print("Has ganado")
            else:
                user_number = int(input("No es correcto, elige otro número: "))

                if user_number == number_to_guess:
                    print("Has ganado")
                else:
                    print("Has perdido")