"""Commande l'ecran LCD I2C."""

from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd

from constantes import PIN_LCD_SCL, PIN_LCD_SDA

class classe_EcranLCD:
    """Initialise un ecran LCD I2C de 2 lignes et 16 caracteres."""

    def __init__(self):
        self.i2c = I2C(
            1,
            scl=Pin(PIN_LCD_SCL),
            sda=Pin(PIN_LCD_SDA),
            freq=400000,
        )
        adresses = self.i2c.scan()
        if not adresses:
            raise RuntimeError("Aucun ecran I2C detecte.")
        self.ecran = I2cLcd(self.i2c, adresses[0], 2, 16)

    def auto_test(self):
        """Affiche un message de test puis efface l'ecran."""
        print("AUTO TEST classe_EcranLCD : affichage du message.")
        try:
            self.ecran.putstr(" MJC Mini Serre\n  Hello World ")
            from time import sleep
            sleep(1)
        finally:
            self.ecran.clear()

        print("AUTO TEST classe_EcranLCD : PASSED")
        return True


if __name__ == "__main__":
    classe_EcranLCD().auto_test()
