from typing import TypedDict, List, Annotated

class StockAnalysisState(TypedDict):
    """
    State definition for the stock analysis workflow.
    This state is passed between nodes in the graph and accumulates information.
    """
    ticker: str
    analysis_type: str
    custom_prompt: str
    fundamentals: Annotated[dict, "fundamentals"]
    graphs: Annotated[List[str], "graphs"]
    pros_cons: Annotated[str, "pros_cons"]
    news: Annotated[List[dict], "news"]
