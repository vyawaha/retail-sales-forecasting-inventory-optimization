import pandas as pd

def load_and_clean_data(path):

    df = pd.read_csv(path)

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['store_id', 'item_id', 'date'])

    # target column
    df['qty_sold'] = df['qty_sold'].fillna(0)

    df = df[df['qty_sold'] >= 0]

    print("✅ Data loaded and cleaned:", df.shape)

    return df