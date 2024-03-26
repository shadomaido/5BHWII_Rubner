import random
from collections import Counter

def lotto():
    eingabe = int(input("Wieviele Zahlen möchten Sie ziehen?: "))
    max_ziehungen = 6 * eingabe
    verfuegbare_zahlen = list(range(1, 46))
    ziehungen = []

    for _ in range(max_ziehungen):
        if not verfuegbare_zahlen:
            print("Nicht genügend verfügbare Zahlen für die angegebene Anzahl von Ziehungen.")
            break

        zufallszahl = random.choice(verfuegbare_zahlen)
        ziehungen.append(zufallszahl)

    return ziehungen

def lotto_statistic():
    ziehungen = lotto()
    statistic = Counter(ziehungen)

    print("Lotto-Statistik (sortiert nach Häufigkeit):")
    for zahl, häufigkeit in statistic.most_common():
        print(f"Zahl {zahl}: {häufigkeit} Mal gezogen")

if __name__ == '__main__':
    lotto_statistic()
