import asyncio

from langchain.callbacks.tracers import ConsoleCallbackHandler

from src.linkedin_agentic_bot.graph.state import State
from src.linkedin_agentic_bot.graph.workflow import build_graph


async def main():
    graph = build_graph().compile()
    initial_state = State(topic="AI")
    result = await graph.ainvoke(
        initial_state, config={"callbacks": [ConsoleCallbackHandler()]}
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
