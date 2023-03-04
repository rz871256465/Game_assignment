import sqlite3
from flask import Flask, g, render_template

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

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# 404 error handling function
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', message="404 Error: Page not found."), 404

# database error handling function
@app.errorhandler(sqlite3.Error)
def database_error(error):
    return render_template('error.html', message="An error occurred while accessing the database."), 500


# define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    try:
        db = get_db()
        cur = db.execute("select * from vgsales")
        rows = cur.fetchall()
        return render_template('game.html', rows=rows)
    except sqlite3.Error as e:
        print("An error occurred while executing the SQL statement:", e)
        return render_template('error.html', message="An error occurred while fetching the data.")

@app.route('/developer')
def developer():
    try:
        db = get_db()
        cur = db.execute("select * from vgsales_details")
        rows = cur.fetchall()
        return render_template('developer.html', rows=rows)
    except sqlite3.Error as e:
        print("An error occurred while executing the SQL statement:", e)
        return render_template('error.html', message="An error occurred while fetching the data.")


