from flask import Flask, render_template
import cards
from cards import deck
import random
# import cards
# from cards import get_deck
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/onecard')
def one_card():
    card_id = random.randint(0,77)
    position = random.randint(0,1)
    if position == 0:
        description = cards.deck[card_id]["desc"]
    else:
        description = cards.deck[card_id]["desc-rev"]
    card_name = cards.deck[card_id]["name"]
    meaning_up = cards.deck[card_id]["meaning_up"]
    meaning_rev = cards.deck[card_id]["meaning_rev"]
    image = cards.deck[card_id]["image"]
    return render_template("onecard.html",
                            position = position,
                            card_name=card_name,
                            meaning_up = meaning_up,
                            meaning_rev = meaning_rev,
                            description = description,
                            image = image)

@app.route('/threecards')
def three_cards():
    return render_template("threecards.html")

if __name__ == '__main__':
    app.run(debug=True)