from langchain_mistralai import ChatMistralAI

from langgraph.graph import (
    StateGraph,
    MessagesState,
    START,
    END
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)

from src.config import LLM_MODEL
from src.tools import search_wikipedia, calculate


# -------------------------
# Tools
# -------------------------

tools = [
    search_wikipedia,
    calculate
]


# -------------------------
# LLM
# -------------------------

model = ChatMistralAI(
    model=LLM_MODEL
)

model_with_tools = model.bind_tools(tools)


# -------------------------
# Agent Node
# -------------------------

def call_model(state: MessagesState):

    response = model_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# -------------------------
# Build Graph
# -------------------------

builder = StateGraph(MessagesState)

builder.add_node(
    "agent",
    call_model
)

builder.add_node(
    "tools",
    ToolNode(tools)
)


# START → Agent

builder.add_edge(
    START,
    "agent"
)


# Agent → Tools OR END

builder.add_conditional_edges(
    "agent",
    tools_condition
)


# Tools → Agent

builder.add_edge(
    "tools",
    "agent"
)


# Compile

graph = builder.compile()