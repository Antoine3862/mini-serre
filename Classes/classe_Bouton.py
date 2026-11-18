"""Gere les boutons definis dans constantes.py et leur anti-rebond."""

from machine import Pin
import time

from constantes import (
    PIN_BP_BAS,
    PIN_BP_CENTRE_OK,
    PIN_BP_DROIT,
    PIN_BP_GAUCHE,
    PIN_BP_HAUT,
)


class classe_Bouton:
    """Gere les cinq boutons directionnels et leur anti-rebond."""

    def __init__(self):
        boutons_config = (
            ("DROIT", PIN_BP_DROIT),
            ("GAUCHE", PIN_BP_GAUCHE),
            ("BAS", PIN_BP_BAS),
            ("HAUT", PIN_BP_HAUT),
            ("CENTRE/OK", PIN_BP_CENTRE_OK),
        )
        maintenant = time.ticks_ms()
        self.boutons = {
            numero: {
                "nom": nom,
                "pin": Pin(broche, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(maintenant, -501),
                "status": False,
            }
            for numero, (nom, broche) in enumerate(boutons_config, start=1)
        }

        for numero, bouton in self.boutons.items():
            bouton["pin"].irq(
                trigger=Pin.IRQ_FALLING,
                handler=lambda pin, n=numero: self._bouton_handler(pin, n),
            )

    def _bouton_handler(self, pin, numero):
        maintenant = time.ticks_ms()
        bouton = self.boutons[numero]
        if time.ticks_diff(maintenant, bouton["date"]) > 500:
            bouton["status"] = True
            bouton["date"] = maintenant

    def get_status(self, numero):
        """Retourne True une seule fois par appui detecte."""
        bouton = self.boutons[numero]
        if bouton["status"]:
            bouton["status"] = False
            return True
        return False

    def auto_test(self, timeout_ms=10000):
        """Demande un appui sur chacun des cinq boutons."""
        for numero, bouton in self.boutons.items():
            print("Appuyez sur {} (delai : {} s).".format(
                bouton["nom"], timeout_ms // 1000
            ))
            debut = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), debut) < timeout_ms:
                if self.get_status(numero):
                    print("Bouton {} : OK".format(bouton["nom"]))
                    break
                time.sleep_ms(10)
            else:
                print("Bouton {} : aucun appui detecte.".format(bouton["nom"]))
                return False

        print("AUTO TEST classe_Bouton : PASSED")
        return True


if __name__ == "__main__":
    classe_Bouton().auto_test()
