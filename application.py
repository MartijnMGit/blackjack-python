from flask import Flask, render_template, request, session, redirect, url_for
from blackjack import deal_card, adjust_for_ace, compare_scores
from art import logo
import boto3

def get_secret_key():
    ssm = boto3.client('ssm', region_name='us-east-1')
    response = ssm.get_parameter(Name='/SECRET_KEY', WithDecryption=True)
    return response['Parameter']['Value']

application = Flask(__name__)
application.secret_key = get_secret_key()

@application.route("/", methods=["GET", "POST"])
def index():
    if "player_cards" not in session:
        # Start new game
        session["player_cards"] = [deal_card(), deal_card()]
        session["pc_cards"] = [deal_card(), deal_card()]
        session["game_over"] = False
        session["result"] = ""

    player_cards = session["player_cards"]
    pc_cards = session["pc_cards"]

    if request.method == "POST":
        if "hit" in request.form and not session["game_over"]:
            player_cards.append(deal_card())
            player_cards = adjust_for_ace(player_cards)
            session["player_cards"] = player_cards
            if sum(player_cards) > 21:
                session["game_over"] = True
                session["result"] = compare_scores(sum(player_cards), sum(pc_cards))
        elif "stand" in request.form:
            # Computer plays
            pc_cards = adjust_for_ace(pc_cards)
            while sum(pc_cards) < 17:
                pc_cards.append(deal_card())
                pc_cards = adjust_for_ace(pc_cards)

            session["game_over"] = True
            session["pc_cards"] = pc_cards
            session["result"] = compare_scores(sum(player_cards), sum(pc_cards))

        elif "restart" in request.form:
            session.clear()
            return redirect(url_for("index"))

    return render_template("index.html",
                           logo=logo,
                           player_cards=session["player_cards"],
                           pc_cards=session["pc_cards"] if session["game_over"] else [session["pc_cards"][0], "?"],
                           player_score=sum(session["player_cards"]),
                           pc_score=sum(session["pc_cards"]) if session["game_over"] else "?",
                           result=session["result"],
                           game_over=session["game_over"])


if __name__ == "__main__":
    application.run(debug=True)
