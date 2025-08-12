from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Define individual agents
web_agent = Agent(
    name="Web Agent",
    role="search the web for news and recent updates about companies",
    model=Groq(id="qwen/qwen3-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the latest headlines and sources in markdown format",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="analyze financial data for given companies",
    model=Groq(id="qwen/qwen3-32b"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_info=True
        )
    ],
    instructions="Use tables and bullet points to present data clearly",
    show_tool_calls=True,
    markdown=True,
)

# Combine agents into a team
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen/qwen3-32b"),
    instructions=[
        "Always include sources",
        "Use tables to display data",
        "Analyze financial + web data and make decisions based on user's investment goals"
    ],
    show_tool_calls=True,
    markdown=True,
)

# User Input & Investment Logic
def main():
    print("\n📈 Welcome to Smart Investment Advisor\n")
    
    companies = input("🔹 Enter company names or tickers (comma separated): ").strip()
    try:
        amount = float(input("💰 Enter investment amount (INR): "))
        profit_target = float(input("🎯 Enter expected profit (INR): "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values for amount and profit.")
        return

    # Compose intelligent prompt
    prompt = f"""
You are a financial advisor AI.
The user wants to invest ₹{amount} and is expecting a minimum profit of ₹{profit_target}.
Analyze the following companies: {companies}

You must:
- Search for current news or risks related to each company
- Fetch stock fundamentals like price, PE ratio, analyst rating
- Suggest the best company (or mix) for long-term investment
- Allocate the amount optimally to meet/exceed the profit goal
- Explain ROI and include sources and tables in markdown format
- Be realistic and suggest safe options if profit is too ambitious

Ensure all data is well-structured and easy to understand.
    """

    print("\n🔎 Analyzing... Please wait...\n")
    agent_team.print_response(prompt)

if __name__ == "__main__":
    main()
