import unittest
from unittest.mock import patch
from katas_divisibles import fizzbuzz

def test_numero_divisible_entre_3():
    """
    Entrada: 3
    Comportamiento esperado:
    - El sistema reconoce el número como válido
    - Imprime 'Fizz'
    - Solicita un nuevo número
    """
    pass


def test_numero_divisible_entre_5():
    """
    Entrada: 5
    Comportamiento esperado:
    - El sistema reconoce el número como válido
    - Imprime 'Buzz'
    - Solicita un nuevo número
    """
    pass


def test_numero_divisible_entre_3_y_5():
    """
    Entrada: 15
    Comportamiento esperado:
    - El sistema reconoce el número como válido
    - Imprime 'FizzBuzz'
    - Solicita un nuevo número
    """
    pass


def test_numero_no_divisible():
    """
    Entrada: 7
    Comportamiento esperado:
    - El sistema reconoce el número como válido
    - Indica que el número no es divisible ni entre 3 ni entre 5
    - Solicita un nuevo número
    """
    pass


def test_numero_fuera_de_rango():
    """
    Entrada: 101
    Comportamiento esperado:
    - El sistema detecta que el número está fuera del rango 1 a 100
    - Muestra el mensaje de rango inválido
    - Solicita un número válido
    """
    pass


def test_texto_galleta():
    """
    Entrada: 'galleta'
    Comportamiento esperado:
    - El sistema detecta que la entrada no es numérica
    - Muestra un mensaje indicando que solo se aceptan números
    - Solicita un número válido
    """
    pass


def test_texto_chorizo():
    """
    Entrada: 'chorizo'
    Comportamiento esperado:
    - El sistema detecta que la entrada no es numérica
    - Muestra un mensaje indicando que solo se aceptan números
    - Solicita un número válido
    """
    pass


def test_texto_leprechaun():
    """
    Entrada: 'leprechaun'
    Comportamiento esperado:
    - El sistema detecta que la entrada no es numérica
    - Muestra un mensaje indicando que solo se aceptan números
    - Solicita un número válido
    """
    pass


def test_texto_roblox():
    """
    Entrada: 'roblox'
    Comportamiento esperado:
    - El sistema detecta que la entrada no es numérica
    - Muestra un mensaje indicando que solo se aceptan números
    - Solicita un número válido
    """
    pass


def test_texto_kolto():
    """
    Entrada: 'kolto'
    Comportamiento esperado:
    - El sistema detecta que la entrada no es numérica
    - Muestra un mensaje indicando que solo se aceptan números
    - Solicita un número válido
    """
    pass

