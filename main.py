import pandas as pd
import matplotlib.pyplot as plt

from src.preprocessing import load_and_clean_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.forecasting import generate_forecast
from src.inventory import compute_inventory_plan
from src.evaluate_model import evaluate

def main():

    print("🚀 Starting Retail Forecasting Pipeline...")

    df = load_and_clean_data("data/raw/retail_data.csv")

    df = create_features(df)

    model, X_test, y_test, preds = train_model(df)

    evaluate(y_test, preds)

    forecast_df = generate_forecast(model, df)

    inventory_df = compute_inventory_plan(forecast_df)

    # SAVE OUTPUTS
    forecast_df.to_csv("outputs/forecast.csv", index=False)
    inventory_df.to_csv("outputs/inventory_plan.csv", index=False)

    print("✅ Pipeline Completed Successfully!")
    print("📁 Outputs saved in /outputs")

    # SAFE VISUALIZATION (FIXED)
    plt.figure(figsize=(10,5))
    plt.plot(y_test.values[:100], label="Actual")
    plt.plot(preds[:100], label="Predicted")
    plt.title("Forecast vs Actual")
    plt.legend()
    plt.savefig("outputs/model_plot.png")

    print("📊 Plot saved to outputs/model_plot.png")

if __name__ == "__main__":
    main()
