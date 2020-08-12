#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")

print("Opened database successfully")
