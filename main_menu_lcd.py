# Prompt d'origine :
# fait un main_menu_lcd qui va créer un menu de type deroulant sur 
# le lecteur LCD, utilise les boutons pour naviguer et le bouton ok 
# pour selectionner, si besoin complete les classes pour ajouter 
# des fonctions utiles, essaie de garder le main simple et clair

"""Menu deroulant de la mini-serre, pilote par les boutons et le LCD."""

import time

from classe_Bouton import classe_Bouton
from classe_DHT22 import classe_DHT22
from classe_DS3231 import classe_DS3231
from classe_EcranLCD import classe_EcranLCD
from constantes import (
    PIN_BP_BAS,
    PIN_BP_CENTRE_OK,
    PIN_BP_DROIT,
    PIN_BP_GAUCHE,
    PIN_BP_HAUT,
)


class MenuLCD:
    """Affiche un menu defilant et lance l'action choisie."""

    def __init__(self, ecran, boutons):
        self.ecran = ecran
        self.boutons = boutons
        self.capteur_air = None
        self.horloge = None
        self.elements = (
            ("Mesures air", self.afficher_mesures_air),
            ("Date et heure", self.afficher_date_heure),
            ("Quitter", None),
        )
        self.selection = 0

    def afficher_menu(self):
        """Affiche la selection et l'element suivant sur les deux lignes."""
        debut = max(0, min(self.selection - 1, len(self.elements) - 2))
        lignes = []
        for numero in range(debut, debut + 2):
            marqueur = ">" if numero == self.selection else " "
            lignes.append("{}{}".format(marqueur, self.elements[numero][0]))
        self.ecran.afficher(lignes[0], lignes[1])

    def attendre_retour(self):
        """Attend OK ou gauche avant de revenir au menu."""
        self.ecran.afficher("OK ou gauche", "pour revenir")
        while True:
            ok = self.boutons.get_status(PIN_BP_CENTRE_OK)
            gauche = self.boutons.get_status(PIN_BP_GAUCHE)
            if ok or gauche:
                return
            time.sleep_ms(20)

    def afficher_mesures_air(self):
        """Lit le DHT22 et affiche la temperature et l'humidite."""
        if self.capteur_air is None:
            self.capteur_air = classe_DHT22()
        temperature, humidite = self.capteur_air.mesurer()
        self.ecran.afficher(
            "Temp: {:.1f} C".format(temperature),
            "Humid: {:.1f} %".format(humidite),
        )
        self.attendre_retour()

    def afficher_date_heure(self):
        """Lit la RTC et affiche la date et l'heure."""
        if self.horloge is None:
            self.horloge = classe_DS3231()
        valeurs = self.horloge.get_time()
        annee, mois, jour = valeurs[0:3]
        heure, minute, seconde = valeurs[4:7]
        self.ecran.afficher(
            "{:02d}/{:02d}/{:04d}".format(jour, mois, annee),
            "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde),
        )
        self.attendre_retour()

    def lancer(self):
        """Execute la navigation jusqu'a la selection de Quitter."""
        en_cours = True
        self.afficher_menu()

        while en_cours:
            haut = self.boutons.get_status(PIN_BP_HAUT)
            bas = self.boutons.get_status(PIN_BP_BAS)
            gauche = self.boutons.get_status(PIN_BP_GAUCHE)
            droite = self.boutons.get_status(PIN_BP_DROIT)
            ok = self.boutons.get_status(PIN_BP_CENTRE_OK)

            if haut or gauche:
                self.selection = (self.selection - 1) % len(self.elements)
                self.afficher_menu()
            elif bas or droite:
                self.selection = (self.selection + 1) % len(self.elements)
                self.afficher_menu()
            elif ok:
                action = self.elements[self.selection][1]
                if action is None:
                    en_cours = False
                else:
                    action()
                    self.afficher_menu()

            time.sleep_ms(20)

        self.ecran.afficher("Menu termine", "")


def main():
    """Initialise les composants puis lance le menu."""
    menu = MenuLCD(classe_EcranLCD(), classe_Bouton())
    menu.lancer()


if __name__ == "__main__":
    main()
