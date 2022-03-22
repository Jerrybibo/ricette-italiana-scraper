import sqlite3
import os
import csv

DB_FILE = os.path.join('.', 'sqlite', 'ricette-italiana.db')


def connect_db(db):
    con = sqlite3.connect(db)
    return con, con.cursor()


def load_csv_to_table(input_csv, table, columns, clear_table=False):
    con, cur = connect_db(DB_FILE)
    if clear_table:
        cur.execute(f'DELETE FROM {table}')
    with open(input_csv, 'r') as input_file:
        dr = csv.DictReader(input_file)
        to_db = [tuple(int(i[col]) if i[col].isnumeric() else i[col] for col in columns) for i in dr]
        print(to_db)
    cur.executemany(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(len(columns) * ['?'])});", to_db)
    con.commit()
    con.close()


def main():
    load_csv_to_table('ingredients.csv', 'ingredients', ['id', 'name'], True)


if __name__ == '__main__':
    main()
