# Video Game Sales Analysis Web App
This is a web application that displays video game sales data from a SQLite database. The application is built using Python Flask framework and HTML/CSS
## Features
**Home page**: Displays an overview of the database records and allows the user to filter the records by platform or genre.

**Game details** page: Displays detailed information about a specific video game, including its rank, name, platform, year, genre, publisher, and sales data.

**Developer details page**: Displays detailed information about a specific game developer, including its rank, name, genre, ESRB rating, platform, publisher, and game review scores.

## File structure

```game.py```: Python script that defines the Flask application and the different routes of the web application.

```setup_db.py```: Python script that creates the SQLite database and populates it with data from a CSV file.

```templates```/: Directory that contains all HTML templates used by the web application.

```index.html```: Home page template.

```game.html```: Game details page template.

```developer.html```: Developer details page template.

## how to run
please make sure you have installed flask
```pip install flask```
```
cd Game_assignment
export FLASK_APP=game.py
export FLASK_ENV=development
python -m flask run -h 0.0.0.0
```
## Precautions

please make sure you have loaded the flask framework before using.

you can put ``` pip list ```
to check whether the framework is installed


