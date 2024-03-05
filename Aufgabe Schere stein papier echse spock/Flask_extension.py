import sqlite3
import json
from flask import Flask, render_template

app = Flask(__name__)

def display_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

@app.route('/')
def home():
    # Lese die Daten aus der Datenbank
    player_results = display_table('playerresults')
    all_symbols = display_table('allsymbols')
    return render_template('showplayerresults.html', player_results=player_results, all_symbols=all_symbols)


if __name__ == '__main__':
    connection = sqlite3.connect("playerdata.db",check_same_thread=False)
    cursor = connection.cursor()
    app.run(debug=True)
