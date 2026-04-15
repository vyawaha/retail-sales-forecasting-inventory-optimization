import pandas as pd
import numpy as np

np.random.seed(42)

n_stores = 3
n_products = 10
dates = pd.date_range(start="2022-01-01", end="2022-12-31")

data = []

for store in range(1, n_stores + 1):
    for product in range(1, n_products + 1):
        base = np.random.randint(5, 20)

        for date in dates:
            demand = base + np.random.randint(-3, 5)

            if np.random.rand() < 0.1:
                demand += 10  # promo boost

            if np.random.rand() < 0.05:
                demand = 0  # stockout

            data.append([store, product, date, max(0, demand)])

df = pd.DataFrame(data, columns=["store_id", "item_id", "date", "qty_sold"])

df.to_csv("data/raw/retail_data.csv", index=False)

print("✅ Dataset created!")
