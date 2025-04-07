#!/usr/bin/env python
"""
Stock Analysis Agent

This script runs a stock analysis workflow using LangGraph to orchestrate
the process of fetching data, generating visualizations, analyzing fundamentals,
and retrieving news for a given stock ticker.
"""

import os
import json
import argparse
import sys
from src.models.state import StockAnalysisState
from src.graph.workflow import create_stock_analysis_graph

def run_analysis(ticker, analysis_type="general", custom_prompt=""):
    """
    Run the complete stock analysis workflow.
    
    Args:
        ticker: Stock ticker symbol (e.g., "AAPL")
        analysis_type: Type of analysis to perform (e.g., "general", "growth", "value")
        custom_prompt: Additional instructions for the analysis
        
    Returns:
        The final state containing all analysis results
    """
    app = create_stock_analysis_graph()
    
    initial_state = StockAnalysisState(
        ticker=ticker,
        analysis_type=analysis_type,
        custom_prompt=custom_prompt,
        fundamentals={},
        graphs=[],
        pros_cons="",
        news=[]
    )
    return app.invoke(initial_state)

def display_results(result, verbose=True):
    """
    Display the results of the stock analysis in a readable format.
    
    Args:
        result: The final state from the workflow
        verbose: Whether to display detailed results or just a summary
    """
    if verbose:
        print("\n=== Stock Analysis Results ===")
        print(f"Ticker: {result['ticker']}")
        print(f"Analysis Type: {result['analysis_type']}")
        
        print("\nFundamentals:")
        for key, value in result["fundamentals"].items():
            print(f"  {key}: {value}")
        
        print("\nCharts Generated:")
        for chart in result["graphs"]:
            print(f"  {chart}")
        
        print("\nPros and Cons Analysis:")
        print(result["pros_cons"])
        
        print("\nRecent News:")
        for article in result["news"]:
            print(f"  {article['title']}")
            print(f"  URL: {article['url']}")
            print()
    else:
        # Summary mode
        print(f"\n[{result['ticker']}] Analysis completed - Chart saved to {result['graphs'][0]}")
        # Extract a short summary from the pros_cons
        summary_lines = result['pros_cons'].split('\n')[:3]
        print(f"Summary: {' '.join(summary_lines)}")

def load_env_file():
    """Load environment variables from .env file if it exists"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        print("Loading environment variables from .env file...")
        with open(env_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Stock Analysis Agent - Analyze stocks using LangGraph",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python agent.py AAPL                   # Analyze Apple stock
  python agent.py --ticker AAPL,MSFT,GOOG  # Analyze multiple stocks
  python agent.py --ticker TSLA --type value  # Value analysis for Tesla
  python agent.py --ticker NVDA --prompt "Focus on AI market potential"
        """
    )
    
    parser.add_argument('ticker', nargs='?', help='Stock ticker symbol (e.g., AAPL)')
    parser.add_argument('--ticker', '-t', dest='tickers', help='Comma-separated list of ticker symbols (e.g., AAPL,MSFT,GOOG)')
    parser.add_argument('--type', '-y', dest='analysis_type', default='growth', 
                        choices=['growth', 'value', 'general', 'dividend', 'momentum'],
                        help='Type of analysis to perform')
    parser.add_argument('--prompt', '-p', dest='custom_prompt', default='Focus on long-term investment potential.',
                        help='Custom instructions for the analysis')
    parser.add_argument('--summary', '-s', action='store_true', 
                        help='Display summary results instead of detailed analysis')
    
    return parser.parse_args()

if __name__ == "__main__":
    # Load environment variables
    load_env_file()
    
    # Parse command line arguments
    args = parse_arguments()
    
    # Get ticker(s) from arguments
    tickers = []
    if args.ticker:
        tickers.append(args.ticker)
    if args.tickers:
        tickers.extend(args.tickers.split(','))
    
    # If no tickers provided, use default
    if not tickers:
        tickers = ["AAPL"]
    
    # Remove duplicates and convert to uppercase
    tickers = [ticker.strip().upper() for ticker in tickers]
    tickers = list(dict.fromkeys(tickers))  # Remove duplicates while preserving order
    
    # Display analysis configuration
    print(f"Running stock analysis for {len(tickers)} ticker(s): {', '.join(tickers)}")
    print(f"Analysis type: {args.analysis_type}")
    print(f"Custom prompt: {args.custom_prompt}")
    
    # Analyze each ticker
    results = []
    for ticker in tickers:
        print(f"\nAnalyzing {ticker}...")
        try:
            result = run_analysis(
                ticker, 
                analysis_type=args.analysis_type, 
                custom_prompt=args.custom_prompt
            )
            results.append(result)
            
            # Display results
            display_results(result, verbose=not args.summary)
            
        except Exception as e:
            print(f"Error analyzing {ticker}: {str(e)}")
    
    # Final summary
    print(f"\nAnalysis complete for {len(results)}/{len(tickers)} stocks!")
    if results:
        print("Charts saved to the 'charts' directory.")