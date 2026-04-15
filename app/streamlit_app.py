import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# =========================
# 🔥 FIX: ADD ROOT PATH
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Now imports will work on Streamlit Cloud
from src.visualization import plot_forecast
from src.kpis import compute_kpis

st.set_page_config(page_title="Retail Intelligence System", layout="wide")

# =========================
# FILE PATH SETUP
# =========================
file_path = os.path.join(BASE_DIR, "outputs", "inventory_plan.csv")

# =========================
# FILE CHECK (VERY IMPORTANT)
# =========================
if not os.path.exists(file_path):
    st.error("❌ Inventory file not found. Please run main.py first.")
    st.stop()

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(file_path)

# =========================
# UI HEADER
# =========================
st.title("📊 Retail Forecasting System")

# =========================
# SIDEBAR STATUS
# =========================
st.sidebar.title("System Status")

if os.path.exists(file_path):
    st.sidebar.success("✅ Pipeline Ready")
else:
    st.sidebar.error("❌ Run main.py first")

# =========================
# MAIN DASHBOARD
# =========================
st.write("Inventory Optimization Dashboard")

# =========================
# SAFETY CHECK FOR REQUIRED COLUMNS
# =========================
required_cols = ["store_id", "item_id", "predicted_sales", "qty_sold", "order_qty"]

missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    st.error(f"❌ Missing columns in dataset: {missing_cols}")
    st.stop()

# =========================
# FILTERS
# =========================
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
        st.error(f"🚨 REORDER REQUIRED: {row['order_qty']:.0f} units")
    else:
        st.success("✅ Stock OK")



