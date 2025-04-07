import matplotlib.pyplot as plt
import os
import yfinance as yf
from ..models.state import StockAnalysisState

def generate_stock_graphs(state: StockAnalysisState):
    """
    Generate and save a price chart for the stock.
    
    Args:
        state: The current state containing the ticker symbol
        
    Returns:
        Dict with graph file paths to update the state
    """
    stock = yf.Ticker(state["ticker"])
    hist = stock.history(period="1y")
    
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist["Close"], label="Closing Price", color="blue")
    plt.legend()
    plt.title(f"{state['ticker']} Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    
    # Create a charts directory if it doesn't exist
    charts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "charts")
    os.makedirs(charts_dir, exist_ok=True)
    
    chart_filename = os.path.join(charts_dir, f"{state['ticker']}_chart.png")
    plt.savefig(chart_filename)
    plt.close()
    
    return {"graphs": [chart_filename]}
