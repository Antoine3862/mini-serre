"""Lance les auto-tests de tous les composants de la mini-serre."""

from classe_Bouton import classe_Bouton
from classe_DHT22 import classe_DHT22
from classe_DS3231 import classe_DS3231
from classe_EcranLCD import classe_EcranLCD
from classe_LED import classe_LED
from classe_Neopixel import classe_Neopixel
from classe_Relais import classe_Relais
from classe_Servo import classe_Servo


def main_auto_test():
    """Execute les tests dans l'ordre et affiche un bilan."""
    tests = (
        ("BOUTONS", classe_Bouton),
        ("LED", classe_LED),
        ("DHT22", classe_DHT22),
        ("NEOPIXEL", classe_Neopixel),
        ("RELAIS", classe_Relais),
        ("SERVO", classe_Servo),
        ("ECRAN LCD", classe_EcranLCD),
        ("DS3231", classe_DS3231),
    )
    resultats = []

    for nom, composant in tests:
        print("\n--- AUTO TEST {} ---".format(nom))
        try:
            resultat = composant().auto_test()
            statut = "OK" if resultat else "ECHEC"
        except Exception as erreur:
            print("Erreur auto-test {} : {}".format(nom, erreur))
            statut = "ERREUR"
        resultats.append((nom, statut))

    print("\n=== BILAN DES AUTO-TESTS ===")
    for nom, statut in resultats:
        print("{} : {}".format(nom, statut))

    return all(statut == "OK" for _, statut in resultats)


if __name__ == "__main__":
    main_auto_test()
