import sqlite3
from flask import Flask,g, render_template

app = Flask(__name__)

# database details - to remove some duplication
# conn = sqlite3.connect('games.db')
# cur = conn.cursor()

def connect_db():
    conn = sqlite3.connect('games.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# define routes
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/game')
def game():
    db = get_db()
    cur=db.execute("select * from vgsales")
    # cur.execute('SELECT * FROM games')
    rows = cur.fetchall()
    print(rows)
    return render_template('game.html', rows=rows)


@app.route('/developer')
def developer():
    db = get_db()
    cur = db.execute("select * from vgsales_details")

    rows = cur.fetchall()
    return render_template('developer.html', rows=rows)

