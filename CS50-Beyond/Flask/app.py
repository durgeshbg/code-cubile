from flask import Flask, session, render_template, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None],
                            [None, None, None],
                            [None, None, None]]
        session["turn"] = "X"
    return render_template("game.html", board=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"
    return redirect("/")

def game():
    board = session["board"]
    turn = session["turn"]
    for i in range(3):
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                ...
            if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
                ...