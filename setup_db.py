import csv
import sqlite3
from flask import Flask, render_template


conn = sqlite3.connect('games.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS vgsales')
conn.execute('DROP TABLE IF EXISTS vgsales_details')

    # Create tables for both CSV files
cur.execute('''CREATE TABLE vgsales (
                Rank INTEGER,
                Name TEXT PRIMARY KEY,
                Platform TEXT,Year INTEGER,
                Genre TEXT,
                Publisher TEXT,
                NA_Sales REAL,
                EU_Sales REAL,
                JP_Sales REAL,
                Other_Sales REAL,
                Global_Sales REAL)''')
cur.execute('''CREATE TABLE vgsales_details (
                Rank TEXT PRIMARY KEY ,
                Name TEXT,
                Genre TEXT,
                ESRB_Rating TEXT,
                Platform TEXT,
                Publisher TEXT,
                Developer TEXT,
                Critic_Score INTEGER,
                User_Score REAL,
                Year INTEGER,
                FOREIGN KEY (Name) REFERENCES vgsales(Name))''')

    # Read data from the first CSV file and insert into the 'vgsales' table
with open('database/vgsales.csv', 'r', newline='') as f:
    reader = csv.reader(f,delimiter=",")
    next(reader) # skip header row
    for row in reader:
        #print(row)
        Rank = (row[0])
        Name = (row[1])
        Platform = (row[2])
        Genre = (row[3])
        Publisher = (row[4])
        NA_Sales = (row[5])
        EU_Sales = (row[6])
        JP_Sales = (row[7])
        Other_Sales = (row[8])
        Global_Sales = (row[9])

        cur.execute("INSERT INTO vgsales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)", row)

    # Read data from the second CSV file and insert into the 'vgsales_details' table
with open('database/vgsales-12-4-2019-develop - .csv', 'r',newline='') as f:
    reader = csv.reader(f,delimiter=",")
    next(reader) # skip header row
    for row in reader:
        print(row)
        Rank = (row[0])
        Name = (row[1])
        Genre = (row[2])
        ESRB_Rating = (row[3])
        Developer = (row[4])
        Publisher = (row[5])
        Critic_Score = (row[6])
        User_Score = (row[7])
        Year = (row[8])
        print(row)
        cur.execute("INSERT INTO vgsales_details VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

    conn.commit()

    # Query both tables and join on 'Name'
cur.execute('''SELECT vgsales.*, vgsales_details.*
                FROM vgsales
                INNER JOIN vgsales_details
                ON vgsales.Name = vgsales_details.Name''')
games = cur.fetchall()


conn.close()


