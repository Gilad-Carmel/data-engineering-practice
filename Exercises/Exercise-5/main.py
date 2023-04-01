import psycopg2
from psycopg2 import sql
from pathlib import Path
import csv


def connect_to_db():
    host = 'postgres'
    database = 'postgres'
    user = 'postgres'
    pas = 'postgres'
    conn = psycopg2.connect(host=host, database=database,
                            user=user, password=pas)
    return conn


def write_csv_to_db(csv_file, cur):
    table_name = csv_file.stem
    with open(csv_file, "r") as f:
        next(f)
        cur.copy_from(f, table_name, sep=",")


def main():
    conn = connect_to_db()
    cur = conn.cursor()
    ddl_queries_paths = Path('./DDL-queries').glob('**/*.sql')

    for ddl_q in ddl_queries_paths:
        cur.execute(ddl_q.read_text())

    csvs_paths = Path('./data').glob('**/*.csv')
    for csv_file in csvs_paths:
        write_csv_to_db(csv_file, cur)


if __name__ == '__main__':
    main()
