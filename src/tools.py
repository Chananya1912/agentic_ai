import requests
from langchain_core.tools import tool


@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for information about a topic."""

    search_url = "https://en.wikipedia.org/w/api.php"

    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 3
    }

    response = requests.get(
        search_url,
        params=search_params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("query", {}).get("search", [])

    if not results:
        return "No Wikipedia results found."

    output = []

    for result in results:
        output.append(
            f"Title: {result['title']}\n"
            f"Information: {result['snippet']}"
        )

    return "\n\n".join(output)


@tool
def calculate(a: float, b: float, operation: str) -> float:
    """Perform basic arithmetic operations: add, subtract, multiply, divide."""

    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":
        if b == 0:
            return "Cannot divide by zero."

        return a / b

    return "Unsupported operation."