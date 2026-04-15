from xgboost import XGBRegressor

def train_model(df):

    features = [
        'day', 'month', 'dayofweek',
        'lag_1', 'lag_7', 'rolling_mean_7'
    ]

    X = df[features]
    y = df['qty_sold']

    split = int(len(df) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("✅ Model trained successfully")

    return model, X_test, y_test, preds



