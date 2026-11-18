"""Lit l'horloge temps reel DS3231 sur le bus I2C."""

from machine import Pin, I2C
from ds3231 import DS3231

from constantes import PIN_DS3231_SCL, PIN_DS3231_SDA

class classe_DS3231:
    """Initialise le bus I2C et le module DS3231."""

    def __init__(self):
        self.i2c = I2C(
            0,
            sda=Pin(PIN_DS3231_SDA),
            scl=Pin(PIN_DS3231_SCL),
            freq=400000,
        )
        adresses = self.i2c.scan()
        if not adresses:
            raise RuntimeError("Aucun composant I2C detecte sur le bus RTC.")
        self.horloge = DS3231(self.i2c)

    def get_time(self):
        """Retourne les valeurs date/heure fournies par le pilote DS3231."""
        return self.horloge.get_time()

    def auto_test(self):
        """Lit et affiche la date et l'heure de l'horloge."""
        annee, mois, jour, jour_semaine, heure, minute, seconde = self.get_time()
        print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            annee, mois, jour, heure, minute, seconde
        ))
        print("AUTO TEST classe_DS3231 : PASSED")
        return True


if __name__ == "__main__":
    classe_DS3231().auto_test()
