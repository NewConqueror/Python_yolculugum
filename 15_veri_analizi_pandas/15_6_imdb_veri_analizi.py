import pandas as pd

df = pd.read_csv("imdb.csv")

#1
sonuc = df
sonuc = df.columns
sonuc = df.info

#2
sonuc = df.head()

#3
sonuc = df.head(10)

#4
sonuc = df.tail()

#5
sonuc = df.tail(10)

#6
sonuc = df["Movie_Title"]

#7
sonuc = df["Movie_Title"].head()

#8
sonuc = df[["Movie_Title","Rating"]].head()

#9
sonuc = df[["Movie_Title","Rating"]].tail(7)

#10
sonuc = df[5:10][["Movie_Title","Rating"]] # sonuc = df[5:][["Movie_Title","Rating"]].head()

#11
sonuc = df[ (df["Rating"] > 8.0) ] [["Movie_Title","Rating"]].head(50)

#12
sonuc = df[ (df["YR_Released"] >=2014 )  &  (df["YR_Released"] <=2015 ) ][["Movie_Title","YR_Released"]].head(5)

#13
sonuc = df[ (df["Num_Reviews"]  >= 100000) | ( (df["Rating"] >=8) &  (df["Rating"] <=9) ) ] [ ["Movie_Title","Rating","Num_Reviews"] ].head(5)

    
print(sonuc)