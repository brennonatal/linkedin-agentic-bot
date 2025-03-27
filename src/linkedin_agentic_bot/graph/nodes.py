from langchain_core.runnables import RunnableConfig

from src.linkedin_agentic_bot.graph.state import State
from src.linkedin_agentic_bot.graph.utils.chains import (
    get_drafter_chain,
    get_finalizer_chain,
    get_planner_chain,
)


async def planner(state: State, config: RunnableConfig):
    chain = get_planner_chain()
    response = await chain.ainvoke(
        {"topic": state.topic},
        config,
    )
    return {"plan": response}


async def drafter(state: State, config: RunnableConfig):
    chain = get_drafter_chain()
    response = await chain.ainvoke(
        {"plan": state.plan},
        config,
    )
    return {"draft": response}


async def finalizer(state: State, config: RunnableConfig):
    chain = get_finalizer_chain()
    response = await chain.ainvoke(
        {"draft": state.draft},
        config,
    )
    return {"final": response}
