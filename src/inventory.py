import numpy as np

def compute_inventory_plan(df):

    df = df.copy()

    df["forecast_error"] = np.random.normal(2, 0.5, len(df))

    df["safety_stock"] = df["predicted_sales"] * 0.25
    df["reorder_point"] = df["predicted_sales"] * 2 + df["safety_stock"]

    df["order_qty"] = np.maximum(
        df["reorder_point"] - df.get("stock_on_hand", 0),
        0
    )

    df["stock_status"] = df["order_qty"].apply(
        lambda x: "REORDER" if x > 0 else "OK"
    )

    return df

