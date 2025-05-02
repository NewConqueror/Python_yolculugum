import sqlite3

import pandas as pd

df = pd.read_csv("sample.csv")                     # csv dosyaları için kaggle

df = pd.read_json("sample.json",encoding="UTF-8")  # json dosyaları için

df = pd.read_excel("sample.xlsx")                  # excel dosyaları için

bağlanti = sqlite3.connect("sample.db")            # database yani veritabanı dosyaları için bağlantı kurmak gerekiyor

df = pd.read_sql_query("SELECT * FROM students",bağlanti) # SQL komutlarını biliyorsun kabaca anla işte

print(df)