# Agentic-AI


## 🚀 AI Agent Team with Agno Framework & Groq API

This project demonstrates how to build a multi-agent AI system using the **[Agno framework](https://github.com/agnodice/agno)**, powered by **Groq's blazing-fast LLMs**. The setup includes two specialized agents—one for **web search** and another for **financial analysis**—working together to analyze company data and make long-term investment suggestions.

---

### 📦 Key Components

* **LLM Provider**: [Groq API](https://groq.com) using `Qwen-QWQ-32B` model
* **Agent Framework**: [`agno`](https://github.com/agnodice/agno)
* **Tools**:

  * 🔍 `DuckDuckGoTools`: For web search queries
  * 📊 `YFinanceTools`: For real-time financial market data

---

### 🧠 Agents Overview

#### 1. **Web Agent**

* **Role**: Searches the web for general information using DuckDuckGo.
* **Model**: `Groq Qwen-QWQ-32B`
* **Instructions**: Includes the source of the information in the response.
* **Tools**: `DuckDuckGoTools`

#### 2. **Finance Agent**

* **Role**: Retrieves detailed financial data of companies.
* **Model**: `Groq Qwen-QWQ-32B`
* **Instructions**: Presents data in structured tables.
* **Tools**: `YFinanceTools` (supports price, recommendations, fundamentals, company info)

---

### 🤖 Agent Team

The `agent_team` is a **composite agent** that combines both the `web_agent` and `finance_agent`. It:

* Delegates tasks to the appropriate agent based on context
* Ensures output includes **sources** and **tabular financial data**
* Uses the same underlying model for consistency

---

### 💡 Example Use Case

```python
agent_team.print_response(
    "Analyze companies like Tesla, NVDA, Apple and suggest which to buy for long term"
)
```

This command will:

1. Use the **Finance Agent** to gather stock prices, fundamentals, analyst recommendations, etc.
2. Optionally use the **Web Agent** to fetch recent news or sentiment.
3. Aggregate the information into a **formatted markdown response**, enriched with **tables and sources**.
4. Print a detailed investment analysis directly to the terminal or notebook.

---

### 🔐 Environment Variables

Make sure to set your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can load them using:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

### ✅ How to Run

1. Clone the repo
2. Create a virtual environment and install dependencies:

   ```bash
   pip install agno python-dotenv
   ```
3. Set your `.env` with `GROQ_API_KEY`
4. Run the script!

---

Let me know if you want a ready-to-use `README.md` file version!
