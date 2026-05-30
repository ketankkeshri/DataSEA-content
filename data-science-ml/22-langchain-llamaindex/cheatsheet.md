```markdown
# LangChain & LlamaIndex — Cheatsheet

## [Core syntax]

| Thing              | Syntax                                      | Notes                                         |
|--------------------|---------------------------------------------|-----------------------------------------------|
| Create a Chain     | `chain = LLMChain(llm=llm, prompt=prompt)` | Combines LLM and prompt for sequential tasks.|
| Create an Agent     | `agent = Agent(llm=llm, tools=tools)`     | Utilizes LLM with tools for multi-step tasks.|
| Query LlamaIndex   | `response = llamaindex.query("your query")` | Queries indexed data for LLM responses.      |
| Comparison of Chains | `comparison = ChainComparison(chains)`   | Compares multiple chains for performance.     |

## [Common operations]

```python
# Setting up a simple chain
from langchain import LLMChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate("What is the capital of {country}?")
llm = OpenAI(model="gpt-3.5-turbo")
chain = LLMChain(llm=llm, prompt=prompt)

# Running the chain
response = chain.run(country="India")
print(response)  # Output: New Delhi
```

```python
# Using an agent with tools
from langchain.agents import initialize_agent, Tool

tools = [Tool(name="Calculator", func=calculate)]
agent = initialize_agent(llm, tools)

# Running the agent
agent_response = agent.run("What is 5 + 3?")
print(agent_response)  # Output: 8
```

## [Gotchas]

- ⚠️ Always ensure your tools are compatible with the agent's LLM.
- ⚠️ Be mindful of token limits in LLMs; long prompts can lead to truncated responses.

## [Mental model]

- **Chain:** Sequential execution of prompts and responses.
- **Agent:** Dynamic response generation utilizing available tools.
- **LlamaIndex:** A way to query indexed data efficiently for better context.
```