import pandas as pd

df = pd.read_csv("youtube-ing.csv")

#1
sonuc = df.head(10)

#2
sonuc = df[5:10]

#3
sonuc = df.columns
sonuc = len(df.columns)
#4
sonuc = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)

#5
sonuc = df["likes"].mean()
sonuc = df["dislikes"].mean()

#6
sonuc = df[["title","likes","dislikes"]].head(50) # result = df.head(50)[["title","likes","dislikes"]] bu da olur

#7
sonuc = df[ (df["views"].max() ) == df["views"]]["title"].iloc[0]

#8
sonuc = df[ (df["views"].min() ) == df["views"]]["title"].iloc[0]

#9
sonuc = df.sort_values("views",ascending= False).head(10)[["title","views"]]

#10
sonuc = df.groupby("category_id")["likes"].mean().sort_values()

#11
sonuc = df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)

#12
sonuc = df["category_id"].value_counts()

#13
df["uzunluk"] = df["title"].apply(len)
sonuc = df

#14

df["tag_count"] = df["tags"].apply( lambda x: len( x.split("|") ) ) # böyle yapabilirsin
sonuc = df

def tagcount(tag):
    return len( tag.split("|") )                                    # böyle de yapabilirsin

df["tag_count"] = df["tags"].apply(tagcount)                        

print(sonuc)
#15

def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])



