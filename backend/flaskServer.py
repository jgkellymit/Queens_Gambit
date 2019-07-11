from flask import Flask, request, redirect
from flask_cors import CORS
import json
import threading
import time

app = Flask(__name__)
CORS(app)

CURRENT_GAME = None
PLAYERS = []

@app.route('/test', methods=['POST'])
def table_name():
    formName = list(request.form["position"])
    print(request)
    print(formName)
    return json.dumps({"a":1})


@app.route('/start', methods=['POST'])
def start():
    global PLAYERS
    possible_player = list(request.form.keys())
    player_name = possible_player[0] if len(possible_player) > 0 and possible_player[0] not in PLAYERS else "player" + str(len(PLAYERS))
    PLAYERS.append(player_name)
    if len(PLAYERS) == 2:
        return PLAYERS[0]
    else:
        while len(PLAYERS) < 2:
            time.sleep(2)
        return PLAYERS[1]


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")