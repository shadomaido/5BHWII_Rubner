import random
from linkedlist import ChainedList

if __name__ == "__main__":

    chained_list = ChainedList()
    #zufällige Zahlen hinzu
    for _ in range(5):
        chained_list.append(random.randint(1, 100))

    print("Alle Elemente der Liste:")
    chained_list.print_all()

    print("Länge der Liste:", chained_list.get_length())

    print("Liste durch Iterator:")
    for item in chained_list:
        print(item, end=" ")
