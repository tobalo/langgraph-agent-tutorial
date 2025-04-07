from langgraph.graph import StateGraph, END
from ..models.state import StockAnalysisState
from ..tools.stock_data import fetch_stock_data
from ..tools.visualization import generate_stock_graphs
from ..tools.analysis import analyze_pros_cons
from ..tools.news import fetch_news

def create_stock_analysis_graph():
    """
    Create and return the stock analysis workflow graph.
    
    Returns:
        A compiled LangGraph workflow
    """
    graph = StateGraph(StockAnalysisState)
    
    # Add nodes
    graph.add_node("fetch_stock_data", fetch_stock_data)
    graph.add_node("generate_stock_graphs", generate_stock_graphs)
    graph.add_node("analyze_pros_cons", analyze_pros_cons)
    graph.add_node("fetch_news", fetch_news)
    
    # Set entry point
    graph.set_entry_point("fetch_stock_data")
    
    # Add edges
    graph.add_edge("fetch_stock_data", "generate_stock_graphs")
    graph.add_edge("generate_stock_graphs", "analyze_pros_cons")
    graph.add_edge("analyze_pros_cons", "fetch_news")
    graph.add_edge("fetch_news", END)
    
    return graph.compile()

# Export the graph for langgraph.json
graph = create_stock_analysis_graph()
