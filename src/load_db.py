import sqlite3
import os
import csv
from settings import *


def connect_db(db):
    con = sqlite3.connect(db)
    return con, con.cursor()


def load_csv_to_table(input_csv, table, columns, clear_table=False, encoding='utf-8'):
    """
    Load a csv file into a SQLite table.
    CSV column names must be the same as the table columns.
    :param input_csv: The input csv file name
    :param table: The table name
    :param columns: Column names
    :param clear_table: Whether to clear the table or not before importing data.
    :param encoding: The encoding of the csv file
    """
    con, cur = connect_db(DB_FILE)
    if clear_table:
        cur.execute(f'DELETE FROM {table}')
    with open(input_csv, 'r', encoding=encoding) as input_file:
        dr = csv.DictReader(input_file)
        to_db = [tuple(int(i[col]) if i[col].isnumeric() else i[col] for col in columns) for i in dr]
    cur.executemany(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(len(columns) * ['?'])});", to_db)
    con.commit()
    con.close()


def main():
    load_csv_to_table('ingredients.csv', 'ingredients', ['id', 'name'], True, 'utf-16')
    load_csv_to_table('culinary_terms.csv', 'preparations', ['id', 'term', 'definition'], True, 'utf-16')
    load_csv_to_table('recipe_ingredients.csv', 'recipe_ingredients', ['ingredient_id', 'recipe'], True, 'utf-8')


if __name__ == '__main__':
    main()
