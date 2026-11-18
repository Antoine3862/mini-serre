"""Commande les quatre LEDs de la mini-serre."""

from machine import Pin
import time

from constantes import (
    PIN_LED_BLEU,
    PIN_LED_BLANCHE,
    PIN_LED_JAUNE,
    PIN_LED_ROUGE,
)

class classe_LED:
    """Commande les quatre LEDs colorees numerotees de 1 a 4."""

    def __init__(self):
        leds_config = (
            ("BLEUE", PIN_LED_BLEU),
            ("ROUGE", PIN_LED_ROUGE),
            ("BLANCHE", PIN_LED_BLANCHE),
            ("JAUNE", PIN_LED_JAUNE),
        )
        self.leds = {
            numero: {"nom": nom, "pin": Pin(broche, Pin.OUT)}
            for numero, (nom, broche) in enumerate(leds_config, start=1)
        }
        for led in self.leds.values():
            led["pin"].value(0)

    def auto_test(self):
        """Allume chaque LED pendant 500 ms puis l'eteint."""
        print("AUTO TEST classe_LED : sequence des quatre LEDs.")
        try:
            for led in self.leds.values():
                print("  LED {}".format(led["nom"]))
                led["pin"].value(1)
                time.sleep(0.5)
                led["pin"].value(0)
                time.sleep(0.5)
        finally:
            for led in self.leds.values():
                led["pin"].value(0)

        print("AUTO TEST classe_LED : PASSED")
        return True


if __name__ == "__main__":
    classe_LED().auto_test()
