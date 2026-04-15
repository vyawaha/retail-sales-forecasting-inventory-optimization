import plotly.graph_objects as go

def plot_forecast(actual, predicted):

    fig = go.Figure()

    fig.add_trace(go.Scatter(y=actual, name="Actual"))
    fig.add_trace(go.Scatter(y=predicted, name="Predicted"))

    fig.update_layout(
        title="Retail Demand Forecast",
        xaxis_title="Time",
        yaxis_title="Sales"
    )

    return fig
