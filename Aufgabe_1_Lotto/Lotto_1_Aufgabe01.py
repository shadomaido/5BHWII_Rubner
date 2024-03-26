import random


def lotto():
    liste = list(range(1, 46))  # Liste der verfügbaren Zahlen von 1 bis 45

    gezogene_zahlen = set()  # Verwendung eines Sets, um doppelte Zahlen zu verhindern

    for _ in range(6):
        if not liste:
            print("Nicht genügend verfügbare Zahlen für die angegebene Anzahl von Ziehungen.")
            break

        zufallszahl = random.choice(liste)
        liste.remove(zufallszahl)
        gezogene_zahlen.add(zufallszahl)

    return list(gezogene_zahlen)


def lotto_statistic():
    while True:
        try:
            ziehungen = int(input("Wie viele Ziehungen möchten Sie haben? (1-45, 0 zum Beenden): "))

            if ziehungen == 0:
                break
            elif ziehungen < 1 or ziehungen > 45:
                print("Bitte geben Sie eine Anzahl zwischen 1 und 45 ein.")
                continue  # Zurück zur Eingabeaufforderung
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 45 ein.")
            continue  # Zurück zur Eingabeaufforderung

        gezogene_zahlen = []

        for _ in range(ziehungen):
            gruppe = lotto()

            if gruppe in gezogene_zahlen:
                continue  # Wenn eine doppelte Gruppe gezogen wurde, die Ziehung überspringen

            gezogene_zahlen.append(gruppe)

            print("Lotto-Ziehungen:")
            print("Gruppe:", gruppe)


if __name__ == '__main__':
    lotto_statistic()
