import sqlite3
import os
import csv

DB_FILE = os.path.join('.', 'sqlite', 'ricette_italiana.db')


def connect_db(db):
    con = sqlite3.connect(db)
    return con, con.cursor()


def load_csv_to_table(input_csv, table, columns, clear_table=False):
    """
    Load a csv file into a SQLite table.
    CSV column names must be the same as the table columns.
    :param input_csv: The input csv file name
    :param table: The table name
    :param columns: Column names
    :param clear_table: Whether to clear the table or not before importing data.
    """
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
    load_csv_to_table('culinary_terms.csv', 'preparations', ['id', 'name', 'description'], True)


if __name__ == '__main__':
    main()
