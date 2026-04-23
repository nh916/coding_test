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


client: Anthropic = Anthropic(api_key="YOUR_KEY")


def load_pdf(path: str) -> str:
    doc: fitz.Document = fitz.open(path)
    text: str = "\n".join(page.get_text() for page in doc)
    return text


pdf_text: str = load_pdf("file.pdf")

messages: List[Message] = [
    {
        "role": "user",
        "content": f"Here is a document:\n\n{pdf_text}\n\nYou will answer questions about it.",
    }
]


def ask(question: str) -> str:
    messages.append({"role": "user", "content": question})

    res = client.messages.create(
        model="claude-3-sonnet-20240229",  # faster/cheaper than opus
        max_tokens=500,
        messages=messages,
    )

    answer: str = res.content[0].text  # type: ignore
    messages.append({"role": "assistant", "content": answer})
    return answer


# ---------------------------------------------------------------------------------------------


def load_pdf(pdf_path: str) -> str:
    """
    Load the PDF from the given path and return the contents.
    """
    with open(pdf_path, "rb") as pdf_file:
        return pdf_file.read()


def speak_with_ai(pdf_contents: str) -> str:
    """ """
