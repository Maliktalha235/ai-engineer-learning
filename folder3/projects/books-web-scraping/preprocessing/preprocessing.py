import pandas as pd

df=pd.read_csv("Book_Data_multipages.csv")
print("Original Data: ")
print(df.head())
print(df.info())

df["price"]=df["price"].str.replace("Â","",regex=False).astype(float)
rating_map={
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}
df["rating"]=df["rating"].map(rating_map)
#availability:
df["availability"]=df["availability"].apply(lambda x:1
                                            if "In stock" in x else 0)
#duplicates:
df=df.drop_duplicates()
df=df.dropna()
df.to_csv("Cleaned_Bookdata.csv")