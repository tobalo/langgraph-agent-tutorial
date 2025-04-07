import os
import requests
from ..models.state import StockAnalysisState

def fetch_news(state: StockAnalysisState):
    """
    Fetch recent news articles about the stock.
    
    Args:
        state: The current state containing the ticker symbol
        
    Returns:
        Dict with news articles to update the state
    """
    try:
        # Use NewsAPI if API key is provided
        api_key = os.environ.get("NEWSAPI_KEY")
        if api_key:
            url = f"https://newsapi.org/v2/everything?q={state['ticker']}&apiKey={api_key}"
            response = requests.get(url).json()
            news_articles = [{"title": article["title"], "url": article["url"]} 
                            for article in response.get("articles", [])[:5]]
        else:
            # Provide sample news if no API key
            news_articles = [
                {"title": f"{state['ticker']} Announces Quarterly Results", "url": "https://example.com/news1"},
                {"title": f"Analysts Update Price Target for {state['ticker']}", "url": "https://example.com/news2"},
                {"title": f"Market Outlook: How {state['ticker']} Fits in Your Portfolio", "url": "https://example.com/news3"},
            ]
    except Exception as e:
        news_articles = [{"title": f"Error fetching news: {str(e)}", "url": ""}]
    
    return {"news": news_articles}
