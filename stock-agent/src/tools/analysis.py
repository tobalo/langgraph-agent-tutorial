import os
import json
import ollama
from ..models.state import StockAnalysisState

def analyze_pros_cons(state: StockAnalysisState):
    """
    Analyze stock fundamentals using Ollama with a local llama3.1 model.
    
    Args:
        state: The current state containing fundamentals and analysis parameters
        
    Returns:
        Dict with pros and cons analysis to update the state
    """
    try:
        prompt = (
            f"Analyze this stock as a {state['analysis_type']} investment:\n"
            f"{json.dumps(state['fundamentals'], indent=2)}\n\n"
            f"Custom Input: {state['custom_prompt']}"
        )
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": prompt}])
        return {"pros_cons": response["message"]["content"]}
    except Exception as e:
        # Fallback in case of errors with Ollama
        analysis = f"Error performing analysis with Ollama: {str(e)}\n\n"
        analysis += f"Analysis for {state['ticker']} as a {state['analysis_type']} investment:\n\n"
        analysis += "Pros:\n- Strong fundamentals based on available data\n- Historical performance shows potential\n\n"
        analysis += "Cons:\n- Market volatility may affect short-term performance\n- Further research recommended\n\n"
        analysis += "Note: This is a simplified fallback analysis due to an error with Ollama."
        return {"pros_cons": analysis}
