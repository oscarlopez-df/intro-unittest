"""
Módulo con funciones matemáticas.

Contiene las siguientes funciones:
    - suma: Suma dos números.

"""

from typing import Union


def sum(a: Union[float, int], b: Union[float, int]) -> float:
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Suma de los dos números.

    Raises:
        TypeError: Si alguno de los argumentos no es un `float` o un `int`.

    """
    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        return a + b
    else:
        raise TypeError("Los argumentos deben ser tipo `float` o `int`.")
