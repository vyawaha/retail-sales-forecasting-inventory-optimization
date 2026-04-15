import pandas as pd
import numpy as np

def simulate_retail_environment(df):

    df = df.copy()

    # Simulate stock
    df["stock_on_hand"] = np.random.randint(20, 200, size=len(df))

    # Simulate demand shocks
    df["demand_multiplier"] = np.random.normal(1.0, 0.2, len(df))
    df["simulated_sales"] = df["qty_sold"] * df["demand_multiplier"]

    # Stockout logic
    df["stockout_flag"] = df["simulated_sales"] > df["stock_on_hand"]

    df.loc[df["stockout_flag"], "simulated_sales"] = df["stock_on_hand"]

    return df
