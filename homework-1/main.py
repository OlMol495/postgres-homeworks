"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


with open('north_data/customers_data.csv', 'r') as file:
    customer = csv.reader(file)
    for row in customer:
        print(row)


