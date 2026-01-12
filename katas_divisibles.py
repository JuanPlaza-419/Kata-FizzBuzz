def fizzbuzz():
    entrada = input("Introduce un número: ")

    if not entrada.isdigit():
        print(f'No me vengas con "{entrada}" aquí solo hablamos con números')
        return

    numero = int(entrada)
    resultado = ""

    if numero % 3 == 0:
        resultado += "Fizz"
    if numero % 5 == 0:
        resultado += "Buzz"

    print(resultado or f"El número {numero} no es divisible ni entre 3 ni entre 5")

fizzbuzz()
