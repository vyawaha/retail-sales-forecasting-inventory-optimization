import numpy as np

def compute_kpis(actual, predicted):

    lost_sales = np.maximum(actual - predicted, 0).sum()
    overstock = np.maximum(predicted - actual, 0).sum()

    service_level = 1 - (lost_sales / (actual.sum() + 1e-6))

    return {
        "lost_sales": float(lost_sales),
        "overstock": float(overstock),
        "service_level": float(service_level)
    }