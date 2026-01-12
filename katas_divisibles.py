def fizzbuzz():
    entrada = input("Introduce un número: ")

    if not entrada.isdigit():
        print('No me vengas con "' + entrada + '" aquí solo hablamos con números')
        return

    numero = int(entrada)

    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print("El número " + str(numero) + " no es divisible ni entre 3 ni entre 5")

fizzbuzz()
