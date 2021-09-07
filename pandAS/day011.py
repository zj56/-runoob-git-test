import pandas as pd
df = pd.read_csv("d:/ee/products.csv")
# print(df.info())
# print(df.head())
# print(df.info())
df.sort_values(by="aisle_id",ascending=False)
# print(df[(10<df["aisle_id"])&(df["aisle_id"]<100)])
print(df[:20]["aisle_id"])
print(type(df["aisle_id"]))