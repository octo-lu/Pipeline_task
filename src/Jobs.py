import pandas as pd

def filter_GO(df):
    df_GO = df[df['LOCAL'] == 'GO']
    return df_GO

def filter_DF(df):
    df_DF = df[df['LOCAL'] == 'GO']
    return df_DF

def origin_document_col(df):

    return df

def dataframe_merger(list):

    df_merge = pd.concat(list)
    return df_merge