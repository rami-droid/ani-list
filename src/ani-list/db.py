import sqlite3 as sq
from rich.console import Console


db = sq.connect("ani_list.db")
db.row_factory = sq.Row
cur = db.cursor()

create_table = """ 
CREATE TABLE IF NOT EXISTS
watchlist(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
mal_id INTEGER UNIQUE NOT NULL,
title TEXT NOT NULL,
status TEXT CHECK(status IN ('watching', 'finished', 'want_to_watch')) NOT NULL,
episodes_watched INTEGER DEFAULT 0,
total_episodes INTEGER,
timestamp_added DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

console = Console()


cur.execute("SELECT mal_id, title, status FROM watchlist")
rows = cur.fetchall()

for r in rows:
    print(r)


def init():
    cur.execute(create_table)
    db.commit()


def fetch_all():
    command = """ 
     SELECT * FROM watchlist
    """
    cur.execute(command)
    database = cur.fetchall()
    data = [dict(r) for r in database]
    return data


def fetch_one(mal_id):
    command = """ 
     SELECT * FROM watchlist WHERE mal_id = ? 
    """
    cur.execute(command)
    row = cur.fetchone()
    if row:
        return row
    return None


def add_anime(mal_id, title, status, total_episodes):
    cur.execute("SELECT 1 FROM watchlist WHERE mal_id = ?", (mal_id,))
    exists = cur.fetchone()

    if exists is None:
        add_row = """ 
        INSERT INTO watchlist (mal_id, title, status, total_episodes) VALUES (?, ?, ?, ?) 
        """
        cur.execute(add_row, (mal_id, title, status, total_episodes))
        db.commit()
    else:
        console.print("This ID is already in table")


def remove_anime(mal_id):
    delete_row = """ 
    DELETE FROM watchlist WHERE mal_id=?
    """
    cur.execute(delete_row, (mal_id,))
    db.commit()


def update_anime(mal_id, episodes_watched=None, status=None):
    if status is None and episodes_watched is not None:
        update_row = """ 
        UPDATE watchlist set episodes_watched = ?
        WHERE mal_id = ?
        """
        cur.execute(update_row, (episodes_watched, mal_id))
    if status is not None and episodes_watched is None:
        update_row = """ 
        UPDATE watchlist set status = ?
        WHERE mal_id = ?
        """
        cur.execute(update_row, (episodes_watched, mal_id))
    else:
        update_row = """ 
        UPDATE watchlist set episodes_watched = ?, status= ? 
        WHERE mal_id = ?
        """
        cur.execute(update_row, (episodes_watched, status, mal_id))
    db.commit()
