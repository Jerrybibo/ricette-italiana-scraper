import sqlite3

# Connect to the recipes DB and execute
con = sqlite3.connect('ricette_italiana.db')
cur = con.cursor()
with open('init_tables.sql', 'r') as init_script:
    cur.executescript(init_script.read())

# Save (commit) the changes and close the connection
con.commit()
con.close()
