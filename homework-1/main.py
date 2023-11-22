"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='5758'
)

cur = conn.cursor()

with open('north_data/customers_data.csv', encoding='utf-8') as file:
    csv.field_size_limit(10**8)
    for line in csv.reader(file):
        try:
            cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (line[0], line[1], line[2]))

        finally:
            conn.commit()

with open('north_data/employees_data.csv', encoding='utf-8') as file:
    csv.field_size_limit(10**8)
    for line in csv.reader(file):
        try:
            cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                        (line[0], line[1], line[2], line[3], line[4], line[5]))
        finally:
            conn.commit()

with open('north_data/orders_data.csv', encoding='utf-8') as file:
    csv.field_size_limit(10**8)
    for line in csv.reader(file):
        try:
            cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                        (line[0], line[1], line[2], line[3], line[4]))
        finally:
            conn.commit()

conn.close()
