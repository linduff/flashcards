from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime

app = Flask(__name__)

decks = [
    {"deck_id": 0, "deck_name": "Months"},
    {"deck_id": 1, "deck_name": "Days of the Week"},
    {"deck_id": 2, "deck_name": "Best Picture Winners"}
]

cards = [
    {"card_id": 0, "deck_id": 0, "card_front": "January", "card_back": 1},
    {"card_id": 1, "deck_id": 0, "card_front": "February", "card_back": 2},
    {"card_id": 2, "deck_id": 0, "card_front": "March", "card_back": 3},
    {"card_id": 3, "deck_id": 0, "card_front": "April", "card_back": 4},
    {"card_id": 4, "deck_id": 0, "card_front": "May", "card_back": 5},
    {"card_id": 5, "deck_id": 0, "card_front": "June", "card_back": 6},
    {"card_id": 6, "deck_id": 0, "card_front": "July", "card_back": 7},
    {"card_id": 7, "deck_id": 0, "card_front": "August", "card_back": 8},
    {"card_id": 8, "deck_id": 0, "card_front": "September", "card_back": 9},
    {"card_id": 9, "deck_id": 0, "card_front": "October", "card_back": 10},
    {"card_id": 10, "deck_id": 0, "card_front": "November", "card_back": 11},
    {"card_id": 11, "deck_id": 0, "card_front": "December", "card_back": 12},
    {"card_id": 12, "deck_id": 1, "card_front": "Sunday", "card_back": 1},
    {"card_id": 13, "deck_id": 1, "card_front": "Monday", "card_back": 2},
    {"card_id": 14, "deck_id": 1, "card_front": "Tuesday", "card_back": 3},
    {"card_id": 15, "deck_id": 1, "card_front": "Wednesday", "card_back": 4},
    {"card_id": 16, "deck_id": 1, "card_front": "Thursday", "card_back": 5},
    {"card_id": 17, "deck_id": 1, "card_front": "Friday", "card_back": 6},
    {"card_id": 18, "deck_id": 1, "card_front": "Saturday", "card_back": 7},
    {"card_id": 19, "deck_id": 2, "card_front": "Wings", "card_back": "1927/1928"},
    {"card_id": 20, "deck_id": 2, "card_front": "The Broadway Melody", "card_back": "1928/1929"},
    {"card_id": 21, "deck_id": 2, "card_front": "All Quiet on the Western Front", "card_back": "1929/1930"},
    {"card_id": 22, "deck_id": 2, "card_front": "Cimarron", "card_back": "1930/1931"},
    {"card_id": 23, "deck_id": 2, "card_front": "Grand Hotel", "card_back": "1931/1932"},
    {"card_id": 24, "deck_id": 2, "card_front": "Cavalcade", "card_back": "1932/1933"},
    {"card_id": 25, "deck_id": 2, "card_front": "It Happened One Night", "card_back": "1934"},
    {"card_id": 26, "deck_id": 2, "card_front": "Mutiny On the Bounty", "card_back": "1935"}
]

@app.route("/", methods=['GET', 'POST'])
def homePage():
    if request.method == 'POST':
        decks.append({"deck_id": len(decks), "deck_name": request.form['deck_name']})
    return render_template("home.html", decks = decks)

@app.route("/deck/<deck_id>", methods=['GET', 'POST'])
def deck(deck_id):
    if request.method == 'POST':
        cards.append({"card_id": len(cards), "deck_id": deck_id, "card_front": request.form['card_front'], "card_back": request.form['card_back']})
    deck_cards = []
    for card in cards:
        if int(card["deck_id"]) == int(deck_id):
            deck_cards.append(card)
    return render_template("deck.html", cards = deck_cards, deck_id = deck_id)

if __name__ == "__main__":
    app.run()
