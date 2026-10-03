from dotenv import load_dotenv

from src.graph import graph


load_dotenv()


def main():

    print("AI Research Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        if not question.strip():
            continue

        result = graph.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        })

        final_message = result["messages"][-1]

        print("\nAssistant:")
        print(final_message.content)
        print()


if __name__ == "__main__":
    main()