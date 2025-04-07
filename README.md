# LangGraph Agents Workshop

This workshop demonstrates how to build stateful agents using LangGraph and LangChain, showcasing a practical stock analysis agent implementation.

## What is LangGraph?

LangGraph is an orchestration framework for building stateful, multi-actor applications with LLMs. It provides:

- **Stateful workflows**: Maintain context across interactions
- **Cyclic graphs**: Enable complex decision-making loops
- **Multi-actor systems**: Coordinate multiple AI agents

## LangGraph vs. LangChain

| LangGraph | LangChain |
|-----------|-----------|
| Low-level orchestration | High-level abstractions |
| Complex agent systems | Simple chains and retrieval |
| Explicit state management | Implicit state handling |
| Cyclic execution flows | Linear execution flows |

## Getting Started

### Setup
Dependencies: 
- [Python 3](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (recommended)
- [Ollama](https://ollama.com/download)
- [NewsAPI KEY](https://newsapi.org/)

1. Run Ollama with Llama3.1 in a separate terminal: `ollama run llama3.1`

2. Create .env file: `cp .env.example .env`

### Installation

```bash
cd stock-agent
# Using uv (recommended)
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

### Stock Analysis Agent Example

This repository includes a practical example of a stock analysis agent built with LangGraph. The agent performs the following steps:

1. Fetches fundamental data for a stock
2. Generates price trend charts
3. Analyzes pros and cons using an LLM (Ollama with llama3.1)
4. Retrieves recent news articles

#### Running the Example

The stock analysis agent supports analyzing one or multiple stocks with various options:

```bash
# Basic usage - analyze a single stock
python3 agent.py AAPL

# Analyze multiple stocks
python3 agent.py --ticker AAPL,MSFT,GOOG

# Specify analysis type
python3 agent.py --ticker TSLA --type value

# Add custom analysis instructions
python3 agent.py --ticker NVDA --prompt "Focus on AI market potential"

# Display summary results instead of detailed analysis
python3 agent.py --ticker AMZN --summary
```

#### Command-line Options

```text
usage: agent.py [-h] [--ticker TICKERS] [--type {growth,value,general,dividend,momentum}]
                [--prompt CUSTOM_PROMPT] [--summary]
                [ticker]

Stock Analysis Agent - Analyze stocks using LangGraph

positional arguments:
  ticker                Stock ticker symbol (e.g., AAPL)

options:
  -h, --help            show this help message and exit
  --ticker TICKERS, -t TICKERS
                        Comma-separated list of ticker symbols (e.g., AAPL,MSFT,GOOG)
  --type {growth,value,general,dividend,momentum}, -y {growth,value,general,dividend,momentum}
                        Type of analysis to perform
  --prompt CUSTOM_PROMPT, -p CUSTOM_PROMPT
                        Custom instructions for the analysis
  --summary, -s         Display summary results instead of detailed analysis

Examples:
  python agent.py AAPL                   # Analyze Apple stock
  python agent.py --ticker AAPL,MSFT,GOOG  # Analyze multiple stocks
  python agent.py --ticker TSLA --type value  # Value analysis for Tesla
  python agent.py --ticker NVDA --prompt "Focus on AI market potential"
```

## Key Concepts

### Stateful Nodes

Stateful nodes maintain context between invocations, enabling:

- Memory of past interactions
- Persistent reasoning chains
- Conditional logic based on history

In our stock agent example, each node receives the current state, processes it, and returns updates to that state. The state accumulates information as it flows through the graph.

### Graph-Based Workflows

LangGraph uses directed graphs to define agent behavior:

- Nodes represent processing steps
- Edges define possible transitions
- Conditional routing based on agent decisions

Our stock analysis workflow demonstrates a linear graph, but LangGraph supports complex branching and cyclic flows for more advanced use cases.

### Multi-Agent Orchestration

LangGraph excels at coordinating multiple specialized agents:

- Research agents gather information
- Reasoning agents analyze data
- Planning agents create action plans
- Execution agents implement solutions

## Advanced Examples

For more advanced examples, explore:

- Tool-using agents with dynamic tool selection
- Multi-agent collaboration with specialized roles
- Human-in-the-loop workflows for approval steps
- Persistent memory systems for long-running agents

## Resources

- [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
- [LangChain Documentation](https://python.langchain.com/docs/get_started)
- [GitHub Repository](https://github.com/langchain-ai/langgraph)
