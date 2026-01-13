def fizzbuzz():
    entrada = input("Introduce un número: ")

    try:
        numero = int(entrada)
    except ValueError:
        print(f'No me vengas con "{entrada}" aquí solo hablamos con números')
        return False

    resultado = ""

    if numero % 3 == 0:
        resultado += "Fizz"
    if numero % 5 == 0:
        resultado += "Buzz"

    print(resultado or f"El número {numero} no es divisible ni entre 3 ni entre 5")
    return True


while True:
    correcto = fizzbuzz()

    if correcto:
        print("¡Dame otro!")
    else:
        print("Dame un número de verdad, no tonterías de esas")