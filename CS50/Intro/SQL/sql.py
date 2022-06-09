import csv
from cs50 import SQL
db = SQL("sqlite:///shows.db")
title = input("Title: ").strip().upper()
rows = db.execute("SELECT COUNT(*) AS counter FROM shows WHERE title = ?", title)
row = rows[0]
print(row["counter"])