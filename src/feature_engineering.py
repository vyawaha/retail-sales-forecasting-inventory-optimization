import pandas as pd

def create_features(df):

    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['dayofweek'] = df['date'].dt.dayofweek

    df['lag_1'] = df.groupby(['store_id','item_id'])['qty_sold'].shift(1)
    df['lag_7'] = df.groupby(['store_id','item_id'])['qty_sold'].shift(7)

    df['rolling_mean_7'] = df.groupby(['store_id','item_id'])['qty_sold'].transform(
        lambda x: x.shift(1).rolling(7).mean()
    )

    df = df.dropna()

    print("✅ Features created:", df.shape)

    return df