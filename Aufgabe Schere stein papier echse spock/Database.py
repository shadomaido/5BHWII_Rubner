import sqlite3
import json


"""Methode, welche es mir erlaubt results und symbols auszulesen und
    in eine Datenbank zu schreiben
"""

def read_json_and_insert(file_name, table_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        drop_tables_query = f"DROP TABLE IF EXISTS {table_name}"
        cursor.execute(drop_tables_query)
        if (table_name =="playerresults"):
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ("
                       f"id INTEGER PRIMARY KEY AUTOINCREMENT, "
                       f"player INT, computer INT, draw INT)")
        else:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ("
                       f" "
                       f"Echse INT, Spock INT, Papier INT, Stein INT, SCHERE INT)")

        if (table_name == "playerresults"):
            cursor.execute(f"INSERT INTO {table_name} (player, computer, draw) VALUES (?, ?, ?)",
                       (data['player'], data['computer'], data['draw']))
        else:

            cursor.execute(f"INSERT INTO {table_name} (Echse, Spock, Papier, Stein, Schere) VALUES(?,?,?,?,?)",
                       (data['Echse'], data['Spock'], data['Papier'], data['Stein'], data['Schere']))

        connection.commit()


def display_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"Table: {table_name}")
    for row in rows:
        print(row)
    print()

if __name__ == "__main__":
    connection = sqlite3.connect("playerdata.db")
    cursor = connection.cursor()

    read_json_and_insert('results.json', 'playerresults')
    read_json_and_insert('symbols.json', 'allsymbols')

    display_table('playerresults')
    display_table('allsymbols')











