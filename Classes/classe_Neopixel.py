"""Commande le ruban NeoPixel de la mini-serre."""

from neopixel import Neopixel
import time

from constantes import PIN_NEOPIXEL

class classe_Neopixel:
    """Commande le ruban NeoPixel et fournit un test visuel."""

    def __init__(self):
        self.nombre_leds = 8
        self.neopixel = Neopixel(self.nombre_leds, 0, PIN_NEOPIXEL, "GRB")
        self.neopixel.brightness(15)
        self.neopixel.clear()
        self.neopixel.show()

    def auto_test(self):
        """Affiche rouge, vert et bleu une seconde chacun, puis eteint le ruban."""
        print("AUTO TEST classe_Neopixel : rouge, vert, bleu.")
        couleurs = (
            ("rouge", (255, 0, 0)),
            ("vert", (0, 255, 0)),
            ("bleu", (0, 0, 255)),
        )
        try:
            for nom, couleur in couleurs:
                print("  {}".format(nom))
                self.neopixel.fill(couleur)
                self.neopixel.show()
                time.sleep(1)
        finally:
            self.neopixel.clear()
            self.neopixel.show()

        print("AUTO TEST classe_Neopixel : PASSED")
        return True


if __name__ == "__main__":
    classe_Neopixel().auto_test()
