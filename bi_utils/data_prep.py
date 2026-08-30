import pandas as pd
import numpy as np

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def handle_missing_dates(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        df[col] = df[col].fillna(pd.Timestamp('1900-01-01'))
    return df
