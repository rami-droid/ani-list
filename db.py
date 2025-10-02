import sqlite3 as sq


db = sq.connect("ani_list.db")
cur = db.cursor()

create_table = """ 
CREATE TABLE IF NOT EXISTS
watchlist(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
mal_id INTEGER UNQIUE NOT NULL,
title TEXT NOT NULL,
status TEXT CHECK(status IN ('watching', 'finished', 'want_to_watch')) NOT NULL,
episodes_watched INTEGER DEFAULT 0,
total_episodes INTEGER,
timestamp_added DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

cur.execute(create_table)
