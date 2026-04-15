import streamlit as st
import pandas as pd
import numpy as np
import os
from src.visualization import plot_forecast
from src.kpis import compute_kpis

st.set_page_config(page_title="Retail Intelligence System", layout="wide")

# =========================
# A. PATH SETUP (FIXED)
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "outputs", "inventory_plan.csv")

# =========================
# B. FILE CHECK (FIXED)
# =========================
if not os.path.exists(file_path):
    st.error("❌ Inventory file not found. Please run main.py first.")
    st.stop()

# =========================
# C. LOAD DATA (FIXED)
# =========================
df = pd.read_csv(file_path)

st.title("📊 Retail Forecasting System")

# =========================
# D. SIDEBAR STATUS (FIXED)
# =========================
st.sidebar.title("System Status")

if os.path.exists(file_path):
    st.sidebar.success("Pipeline Ready")
else:
    st.sidebar.error("Run main.py first")

# =========================
# MAIN UI
# =========================
st.write("Inventory Optimization Dashboard")

# Safety check for columns
required_cols = ["store_id", "item_id", "predicted_sales", "qty_sold", "order_qty"]

missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    st.error(f"Missing columns in dataset: {missing_cols}")
    st.stop()

# Filters
store = st.sidebar.selectbox("Store ID", df["store_id"].unique())
item = st.sidebar.selectbox("Item ID", df["item_id"].unique())

filtered = df[(df["store_id"] == store) & (df["item_id"] == item)]

# =========================
# INVENTORY TABLE
# =========================
st.subheader("📦 Inventory Status")
st.dataframe(filtered)

# =========================
# KPI SECTION
# =========================
st.subheader("📈 Business KPIs")

kpis = compute_kpis(
    filtered["predicted_sales"],
    filtered["qty_sold"]
)

st.write(kpis)

# =========================
# ALERTS
# =========================
st.subheader("⚠ Stock Alerts")

for _, row in filtered.iterrows():
    if row["order_qty"] > 0:
        st.error(f"REORDER REQUIRED: {row['order_qty']:.0f} units")
    else:
        st.success("Stock OK")


