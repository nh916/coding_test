"""
Entry point for the application.
"""

import os

from ai.ai_pdf_reader import PDFChat


def main() -> None:
    """
    Entry point for the application.
    """
    pdf_chat: PDFChat = PDFChat(api_key=os.getenv("ANTHROPIC_API_KEY"))

    pdf_path: str = input("Enter the path to the PDF file: ")
    pdf_chat.load_pdf(pdf_path=pdf_path)

    while True:
        user_question: str = input("Enter your question: ")
        print(pdf_chat.ask(question=user_question))
