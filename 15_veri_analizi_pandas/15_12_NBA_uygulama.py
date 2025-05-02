import pandas as pd

df =pd.read_csv("nba.csv")

#1
sonuc = df.head(10)

#2
sonuc = len(df.index)  # sonuc = df.index  bu da aynı görevi yapar

#3
sonuc = df["Salary"].mean()

#4
sonuc = df["Salary"].max()


#5
sonuc = df[ df["Salary"] == df["Salary"].max() ]["Name"].iloc[0] #0 burda ilk satırdır yani ilk satır ile Name sütununun kesiştiği yeri aldık
# maaşı en yüksek maaşa eşit olan satırı bize komple getirir ama ben sadece ismi istiyorum bu yüzden["Name"].iloc[0] ile sadece ismi aldık


#6
sonuc = df[ (df["Age"]>=20) & (df["Age"]<25) ][["Name","Team","Age"]].sort_values("Age",ascending= False)


#7
sonuc = df[ df["Name"] == "John Holland"]["Team"].iloc[0]


#8
sonuc = df.groupby("Team")["Salary"].mean()  #sonuc = df.groupby("Team").mean()["Salary"] bu şekil de olur


#9
sonuc = df["Team"].nunique()     # sonuc = len(df.groupby("Team"))  # bu şekilde de olur    


#10
sonuc = df["Team"].value_counts() #sonuc = df.groupby("Team")["Name"].nunique() # böyle yaparsan da olur 
#                                                      tekrar etmeyen isimleri aldın aynı kapıya çıktı

#11
#sonuc = df[ df["Name"].str.contains("and")] # NaN değerler old. için hata verir onları silmek lazım

df.dropna(inplace=True)                   # df = df.dropna() aynı şey

sonuc = df[ df["Name"].str.contains("and")]

def isimbul(name):
    if "and" in name.lower():
        return True
    return False

sonuc = df[ df["Name"].apply(isimbul)]
print(sonuc)