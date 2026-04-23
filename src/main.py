"""
Entry point for the application.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from src.ai_pdf_reader import PDFChat


def main() -> None:
    """
    Entry point for the application.
    """

    # get the API key from the environment variables `.env`
    load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY")

    # exception handling for missing API key
    if not anthropic_api_key:
        raise ValueError("ANTHROPIC_API_KEY is not set")

    pdf_chat: PDFChat = PDFChat(api_key=anthropic_api_key)

    pdf_path: str = input("Enter the path to the PDF file: ")
    pdf_chat.load_pdf(path=pdf_path)

    while True:
        user_question: str = input("Enter your question: ")
        print(pdf_chat.ask(question=user_question))


if __name__ == "__main__":
    main()
