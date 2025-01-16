import pandas as pd
import os
import Jobs
import Generate_dataset

#Create output directory

os.makedirs('./output', exist_ok=True)

#Load data
df_1 = pd.DataFrame(Generate_dataset.df_1)
df_2 = pd.DataFrame(Generate_dataset.df_2)
df_3 = pd.DataFrame(Generate_dataset.df_3)
#print(df_1)

df_1.to_excel('teste.xlsx')

df1_GO = Jobs.filter_GO(df_1)
df1_DF = Jobs.filter_DF(df_1)

df2_GO = Jobs.filter_GO(df_2)
df2_DF = Jobs.filter_DF(df_2)

df3_GO = Jobs.filter_GO(df_3)
df3_DF = Jobs.filter_DF(df_3)

df1_GO.to_excel('C:\\Users\\pedro\\OneDrive\\Documentos\\Prog\\Bolsa\\pipeline\\src\\output\\df1_GO.xlsx', index=False)
df1_DF.to_excel('C:\\Users\\pedro\\OneDrive\\Documentos\\Prog\\Bolsa\\pipeline\\src\\output\\df1_DF.xlsx', index=False)

#print(df_GO)

df_merge_DF = Jobs.dataframe_merger([df1_DF, df2_DF, df3_DF])
df_merge_GO = Jobs.dataframe_merger([df1_GO, df2_GO, df3_GO])

df_merge_GO.to_excel('C:\\Users\\pedro\\OneDrive\\Documentos\\Prog\\Bolsa\\pipeline\\src\\output\\Merged_GO.xlsx', index=False)

df_merge_DF.to_excel('C:\\Users\\pedro\\OneDrive\\Documentos\\Prog\\Bolsa\\pipeline\\src\\output\\Merged_DF.xlsx', index=False)


