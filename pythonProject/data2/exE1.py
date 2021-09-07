import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
products_df = pd.read_csv("D:/ee/products.csv")
aisles_df = pd.read_csv("D:/ee/aisles.csv")
departments_df = pd.read_csv("D:/ee/departments.csv")
order_products_prior_df = pd.merge(products_df,aisles_df,on='aisle_id',how='left')
order_products_prior_df=pd.merge(order_products_prior_df,departments_df,on='department_id',how='left')
order_products_prior_df.head()
temp = order_products_prior_df[['product_name','aisle','department']]
temp = pd.concat([
    order_products_prior_df.groupby('department')['product_name'].nunique().rename('products_department'),
    order_products_prior_df.groupby('department')['aisle'].nunique().rename('aisle_department')],axis=1).reset_index()
temp = temp.set_index('department')
temp2 = temp.sort_values(by="aisle_department",ascending=False)
# print(temp)
# print(temp2)
color = sns.color_palette()
x = 0
y = 0 
width = 100
height = 100
cmap = matplotlib.cm.viridis
# mini,maxi=temp2.products_department.min(),temp
