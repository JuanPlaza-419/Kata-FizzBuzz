from katas_divisibles import fizzbuzz
import pytest

def test_fizzbuzz_divisible_entre_3():
    #Revisa si es un numero divisible por 3
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_divisible_entre_5():
    #Revisa si es un numero divisible por 5
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_divisible_entre_3_y_5():
    #Revisa si es un numero divisible por 3 y 5
    assert fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_no_divisible_1():
    #Revisa si es un nummero no divisible como el 1
    assert fizzbuzz(1) == "Es 1, no es divisible"


def test_fizzbuzz_no_divisible_7():
    #Revisa si es un nummero no divisible como el 7
    assert fizzbuzz(7) == "Es 7, no es divisible"


def test_fizzbuzz_numero_grande_divisible_3():
    #Revisa si el numero es un numero mayor a 3
    assert fizzbuzz(99) == "Fizz"


def test_fizzbuzz_numero_grande_divisible_5():
    #Revisa si el numero es un numero mayor a 5
    assert fizzbuzz(100) == "Buzz"


def test_fizzbuzz_retorna_string():
    #Revisa si retorna el numero
    resultado = fizzbuzz(8)
    assert isinstance(resultado, str)


def test_fizzbuzz_cero():
    #Revisa si el numero es 0
    assert fizzbuzz(0) == "Es 0, no es divisible"


def test_fizzbuzz_numero_negativo():
    #Revisa si el numero es negativo
    """
    No valen numeros negativos.
    """
    assert fizzbuzz(-15) == "FizzBuzz"
