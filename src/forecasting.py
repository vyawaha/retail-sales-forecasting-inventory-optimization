def generate_forecast(model, df):

    last_data = df.groupby(['store_id','item_id']).tail(1)

    features = ['day','month','dayofweek','lag_1','lag_7','rolling_mean_7']

    last_data['predicted_sales'] = model.predict(last_data[features])

    print("✅ Forecast generated")

    return last_data