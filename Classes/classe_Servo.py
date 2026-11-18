"""Commande le servo-moteur de la mini-serre."""

from servo import Servo
import time

from constantes import PIN_SERVO

class classe_Servo:
    """Initialise et deplace le servo-moteur."""

    def __init__(self):
        self.moteur = Servo(pin=PIN_SERVO)

    def positionner(self, angle):
        """Positionne le servo a l'angle indique."""
        self.moteur.move(angle)

    def auto_test(self):
        """Teste le mouvement entre 90 et 180 degres puis revient a 90."""
        print("AUTO TEST classe_Servo : deplacement de 90 a 180 degres.")
        for angle in (90, 180, 90):
            self.positionner(angle)
            time.sleep(0.1)

        print("AUTO TEST classe_Servo : PASSED")
        return True


if __name__ == "__main__":
    classe_Servo().auto_test()
