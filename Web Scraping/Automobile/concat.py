import pandas as pd
import numpy as np
automobile=pd.read_csv("cars.csv")
automobile=automobile.drop(columns=['transmission'])
tunisie_annonce=pd.read_csv("cleaner.csv")
tayara=pd.read_csv("clean_data (1).csv")

#rename columns localisation and prix_neuve
tunisie_annonce=tunisie_annonce.rename(columns={'localisaton': 'localisation', 'prix_neuve ':'prix_neuve'})
tayara=tayara.rename(columns={'carosserie': 'carrosserie', 'location':'localisation','kilométrage':'kilometrage'})
tayara=tayara.drop(columns='Unnamed: 0')

con=pd.concat([automobile, tunisie_annonce,tayara], sort=False)
print(con.info())
print(con.head())
print(con.columns)
con.to_csv('concat.csv')







# print(df.info())
# loca=df['localisation']s
# unique_loca=df.drop_duplicates(subset="localisation")
# print(unique_loca)
# # print(f'diffrenet states {loca.drop_duplicates()}')
# by_wileya=df.groupby('localisation')['prix'].agg([np.mean, max,min])
# # print(by_wileya)

