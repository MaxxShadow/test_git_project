"""
Nástroje pro různé pomocné funkce.

- ``TemperatureConverter``: Třída pro převod teplot mezi Celsiem a Fahrenheitem.
- ``StringUtils``: Třída pro různé operace s řetězci.

.. note:: Tento modul je určen pro demonstrační účely a nemusí pokrývat všechny okrajové případy.
"""
class TemperatureConverter:
    """
    Třída pro převod teplot mezi Celsiem a Fahrenheitem."""
    def c_to_f(self, c):
        """
        Převod `Celsia` na `Fahrenheita`.
        :param c: teplota ve stupních Celsia
        :return: teplota ve stupních Fahrenheita

        *Příklad*

        .. code-block:: python
            from utils import TemperatureConverter
            t = TemperatureConverter()
            t.c_to_f(0)  # Výsledek bude 32.0
            t.c_to_f(100)  # Výsledek bude 212.0
        """
        return c * 9 / 5 + 32
 
    def f_to_c(self, f):
        """
        Převod `Fahrenheita` na `Celsia`.
        :param f: teplota ve stupních Fahrenheita
        :return: teplota ve stupních Celsia
        """
        return (f - 32) * 5 / 9
 
 
class StringUtils:
    """
    Třída pro různé operace s řetězci."""
    def reverse(self, text):
        """
        Obrátí řetězec.
        :param text: vstupní řetězec
        :return: obrácený řetězec
        :raises TypeError: pokud text není řetězec
        """
        if not isinstance(text, str):
            raise TypeError("Text musí být řetězec")
        return text[::-1]
 
    def is_palindrome(self, text):
        """
        Zkontroluje, zda je řetězec palindrom.
        :param text: vstupní řetězec
        :return: `True` pokud je palindrom, jinak `False`
        :raises TypeError: pokud text není řetězec

        .. warning:: Tato metoda nerozlišuje velká a malá písmena a ignoruje mezery.
        """

        if not isinstance(text, str):
            raise TypeError("Text musí být řetězec")
        return text == text[::-1]