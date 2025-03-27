from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from src.linkedin_agentic_bot.core.prompts import (
    DRAFTER_PROMPT,
    FINALIZER_PROMPT,
    PLANNER_PROMPT,
)
from src.linkedin_agentic_bot.graph.utils.helpers import get_chat_model


def get_planner_chain():
    chat_model = get_chat_model()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                PLANNER_PROMPT,
            ),
        ]
    )
    return prompt | chat_model | RunnableLambda(lambda x: x.content)


def get_drafter_chain():
    chat_model = get_chat_model()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                DRAFTER_PROMPT,
            ),
        ]
    )
    return prompt | chat_model | RunnableLambda(lambda x: x.content)


def get_finalizer_chain():
    chat_model = get_chat_model()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                FINALIZER_PROMPT,
            ),
        ]
    )
    return prompt | chat_model | RunnableLambda(lambda x: x.content)
