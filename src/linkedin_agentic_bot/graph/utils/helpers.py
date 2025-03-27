import re

from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

from src.linkedin_agentic_bot.settings import settings


def get_chat_model(temperature: float = 0.7):
    return ChatOllama(
        model=settings.TEXT_MODEL_NAME,
        temperature=temperature,
    )


def remove_quotes_content(text: str) -> str:
    """
    Remove content between double quotes from the text.
    If the result would be empty, returns the original text.
    """
    if not text:
        return ""

    cleaned = re.sub(r'"\s*"', "", text)
    cleaned = re.sub(r'^"(.*)"$', r"\1", cleaned)

    if not cleaned.strip():
        return text.strip()

    return cleaned.strip()


class QuotesRemovalParser(StrOutputParser):
    def parse(self, text):
        return remove_quotes_content(super().parse(text))
