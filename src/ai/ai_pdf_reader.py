"""
The package essentially contains everything needed to speak to the AI model.

The AI model will read the PDF given by the path and then hold in memory the contents so the user can speak with it.

Notes:
There might be a constraint on how big the PDF can be.
If so, we should handle it gracefully.
"""

from typing import List, TypedDict

import fitz  # PyMuPDF
from anthropic import Anthropic


class Message(TypedDict):
    role: str
    content: str


class PDFChat:
    """
    Simple PDF chat interface using Claude
    """

    def __init__(self, api_key: str, model: str = "claude-3-sonnet-20240229") -> None:
        """
        Initialize the PDFChat client.

        Args:
            api_key: Anthropic API key.
            model: Claude model to use.
        """
        self.client: Anthropic = Anthropic(api_key=api_key)
        self.model: str = model
        self.messages: List[Message] = []
        self.pdf_text: str = ""

    def load_pdf(self, path: str) -> None:
        """
        Load and extract text from a PDF file.

        Args:
            path: File path to the PDF.
        """
        doc: fitz.Document = fitz.open(path)
        self.pdf_text = "\n".join(page.get_text() for page in doc)

        self.messages = [
            {
                "role": "user",
                "content": f"Here is a document:\n\n{self.pdf_text}\n\nYou will answer questions about it.",
            }
        ]

    def ask(self, question: str) -> str:
        """
        Ask a question about the loaded PDF.

        Args:
            question: User question.

        Returns:
            Model-generated answer.
        """
        self.messages.append({"role": "user", "content": question})

        res = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            messages=self.messages,
        )

        answer: str = res.content[0].text  # type: ignore
        self.messages.append({"role": "assistant", "content": answer})
        return answer
