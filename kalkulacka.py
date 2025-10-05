
class  Kalkulacka:

    def soucet(self, a, b):
        """
        Vypocita soucet dvou cisel.
        :param a: Prvni cislo.
        :param b: Druhe cislo.
        :return: Soucet cisel a a b.
        """
        return a + b

    def rozdil(self, a, b):
        """
        Vypocita rozdil dvou cisel.
        :param a: Prvni cislo.
        :param b: Druhe cislo.
        :return: Rozdil cisel a a b.
        """
        return a - b

    def soucin(self, a, b):
        """
        Vypocita soucin dvou cisel.
        :param a: Prvni cislo.
        :param b: Druhe cislo.
        :return: Soucin cisel a a b.
        """
        return a * b
    
    def podil(self, a, b):
        """
        Vypocita podil dvou cisel.
        :param a: Prvni cislo.
        :param b: Druhe cislo.
        :return: Podil cisel a a b.
        :raises ValueError: Pokud je b rovno nule.
        """
        if b == 0:
            raise ValueError("Deleni nulou neni povoleno.")
        return a / b

