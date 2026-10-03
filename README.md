# Agentic AI Research Assistant

An agentic AI application that uses an LLM, custom tools, and LangGraph to answer user questions through dynamic tool-based workflows.

## Overview

This project demonstrates how to build an agentic AI system where an LLM can decide when to use external tools and then use the tool results to generate a final response.

The system currently provides:

- Wikipedia-based information search
- Basic arithmetic calculations
- LLM-based reasoning
- Tool calling
- LangGraph-based workflow orchestration
- Conditional tool routing

## Architecture

```text
User Question
      |
      v
   Agent / LLM
      |
      v
Need a Tool?
   /       \
 Yes        No
  |          |
  v          v
Tools       END
  |
  v
Tool Result
  |
  v
Agent / LLM
  |
  v
Final Answer

Tech Stack
- Python
- Mistral AI
- LangChain
- LangGraph
- Requests
- python-dotenv
Project Structure
agentic_ai/
|
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── tools.py
│   └── graph.py
|
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Tools
1. Wikipedia Search
The search_wikipedia tool uses the Wikipedia API to retrieve information about a topic.
Example:
What is Retrieval Augmented Generation?

The agent can decide to call the Wikipedia search tool and use the returned information to generate the answer.
2. Calculator
The calculate tool supports:
- Addition
- Subtraction
- Multiplication
- Division
Example:
What is 125 multiplied by 24?

The agent can select the calculator tool to perform the calculation.
LangGraph Workflow
The workflow is implemented using LangGraph.
The main components are:
- State — stores the conversation messages
- Agent Node — sends messages to the LLM
- Tool Node — executes selected tools
- Conditional Edge — determines whether the workflow should execute a tool or finish
The workflow can loop between the agent and tools:
START
  |
  v
Agent
  |
  v
Tool required?
 /        \
Yes        No
 |          |
 v          v
Tools       END
 |
 v
Agent

Setup
1. Clone the repository
git clone https://github.com/Chananya1912/agentic_ai.git
cd agentic_ai

2. Create a virtual environment
python -m venv venv

Activate it on Windows:
venv\Scripts\activate

3. Install dependencies
python -m pip install -r requirements.txt

4. Configure the API key
Create a .env file:
MISTRAL_API_KEY=your_mistral_api_key_here

Do not commit the .env file to GitHub.
5. Run the application
python main.py

Example
AI Research Assistant
Type 'exit' to quit.

You: What is RAG?

Assistant:
[RAG explanation generated using the available tools]

Another example:
You: What is 125 multiplied by 24?

Assistant:
125 multiplied by 24 is 3000.

Key Concepts Demonstrated
This project was built to understand and demonstrate:
- LLM integration
- Prompt and model abstractions with LangChain
- Custom tools
- Tool calling
- Agentic workflows
- LangGraph
- State
- Nodes
- Edges
- Conditional routing
- Tool execution loops
Future Improvements
Possible improvements include:
- Add more research tools
- Add web search
- Add structured outputs
- Add conversation memory
- Add multiple specialized agents
- Add FastAPI backend
- Add Docker support
- Add logging and monitoring
- Deploy the application
Learning Objective
The main goal of this project is to understand how an LLM-based application can move from a simple fixed chain to a dynamic agentic workflow where the model can select and use tools based on the user's request.