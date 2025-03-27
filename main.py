import argparse
import asyncio

from langchain.callbacks.tracers import ConsoleCallbackHandler

from src.linkedin_agentic_bot.graph.state import State
from src.linkedin_agentic_bot.graph.workflow import build_graph


async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="LinkedIn Agentic Bot")
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug mode with callbacks"
    )
    args = parser.parse_args()

    # Configure callbacks based on debug flag
    callbacks = [ConsoleCallbackHandler()] if args.debug else []

    # Prompt user for topic
    topic = input("Enter a topic for your LinkedIn post: ")

    graph = build_graph().compile()
    initial_state = State(topic=topic)
    result = await graph.ainvoke(initial_state, config={"callbacks": callbacks})
    print("\nGenerated LinkedIn Post:")
    print("-----------------------")
    print(result["final"])


if __name__ == "__main__":
    asyncio.run(main())
