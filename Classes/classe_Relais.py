"""Commande les quatre relais de la mini-serre."""

from machine import Pin
import time

from constantes import (
    PIN_RELAIS_CHAUFFAGE,
    PIN_RELAIS_LUMIERE_INTERIEURE,
    PIN_RELAIS_POMPE,
    PIN_RELAIS_VENTILATEUR,
)


class classe_Relais:
    """Commande les relais numerotes de 1 a 4."""

    def __init__(self):
        broches = (
            ("CHAUFFAGE", PIN_RELAIS_CHAUFFAGE),
            ("POMPE", PIN_RELAIS_POMPE),
            ("VENTILATEUR", PIN_RELAIS_VENTILATEUR),
            ("LUMIERE INTERIEURE", PIN_RELAIS_LUMIERE_INTERIEURE),
        )
        self.relais = {
            numero: {"nom": nom, "pin": Pin(broche, Pin.OUT)}
            for numero, (nom, broche) in enumerate(broches, start=1)
        }
        for relais in self.relais.values():
            relais["pin"].value(0)

    def set_status(self, numero, etat):
        """Active ou desactive le relais indique."""
        self.relais[numero]["pin"].value(1 if etat else 0)

    def allumer(self, numero):
        self.set_status(numero, True)

    def eteindre(self, numero):
        self.set_status(numero, False)

    def auto_test(self):
        """Active chaque relais une seconde, puis le desactive."""
        print("AUTO TEST classe_Relais : sequence des quatre relais.")
        try:
            for numero, relais in self.relais.items():
                print("  Relais {} ({})".format(numero, relais["nom"]))
                self.allumer(numero)
                time.sleep(1)
                self.eteindre(numero)
                time.sleep(1)
        finally:
            for relais in self.relais.values():
                relais["pin"].value(0)

        print("AUTO TEST classe_Relais : PASSED")
        return True


if __name__ == "__main__":
    classe_Relais().auto_test()
