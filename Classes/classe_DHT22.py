"""Lit la temperature et l'humidite du capteur DHT22."""

from machine import Pin
import dht
import time

from constantes import PIN_DHT22


class classe_DHT22:
    """Initialise et lit le capteur DHT22."""

    def __init__(self):
        self.capteur = dht.DHT22(Pin(PIN_DHT22))

    def mesurer(self):
        """Effectue une mesure et retourne temperature et humidite."""
        time.sleep(1)
        self.capteur.measure()
        return self.capteur.temperature(), self.capteur.humidity()

    def auto_test(self):
        """Effectue une mesure et affiche ses valeurs."""
        temperature, humidite = self.mesurer()
        print("Temperature : {:.1f} C".format(temperature))
        print("Humidite    : {:.1f} %".format(humidite))
        print("AUTO TEST classe_DHT22 : PASSED")
        return True


if __name__ == "__main__":
    classe_DHT22().auto_test()
