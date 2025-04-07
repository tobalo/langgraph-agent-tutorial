import yfinance as yf
from ..models.state import StockAnalysisState

def fetch_stock_data(state: StockAnalysisState):
    """
    Fetch fundamental data for a stock using yfinance.
    
    Args:
        state: The current state containing the ticker symbol
        
    Returns:
        Dict with fundamentals data to update the state
    """
    stock = yf.Ticker(state["ticker"])
    return {
        "fundamentals": {
            "Market Cap": stock.info.get("marketCap"),
            "P/E Ratio": stock.info.get("trailingPE"),
            "Revenue": stock.info.get("totalRevenue"),
            "EPS": stock.info.get("trailingEps"),
            "Debt-to-Equity": stock.info.get("debtToEquity"),
        }
    }
