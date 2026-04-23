# PDF Chat CLI

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Claude](https://img.shields.io/badge/AI-Claude-orange)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-60A5FA?logo=poetry)
![Mypy](https://img.shields.io/badge/Type%20Checked-Mypy-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A simple command-line tool that lets you chat with a PDF using Claude.


## Overview

PDFChat CLI allows you to:
- Load a PDF from a file path
- Ask questions about its content
- Get AI-generated answers grounded in the document

This is a lightweight implementation focused on simplicity and speed, using Claude’s context window instead of a full RAG pipeline.


## Features

- Chat with any PDF via terminal
- Minimal setup and fast execution
- Uses `.env` for secure API key management
- Clean, typed Python codebase (mypy-compatible)


## How It Works

1. Extracts text from the PDF
2. Sends the content to Claude
3. Maintains a conversation loop for Q&A

Note: For large PDFs, responses may degrade due to context limits.


## Setup

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_api_key_here
```


## Installation

1. clone project
2. `cd pdfchat-cli`
3. `pip install poetry`
4. `poetry install`


## Usage

```bash
poetry run python -m src.main
```

Then start asking questions in the terminal.


## Example

```bash
> What is the main topic of this document?
> Summarize chapter 2
> Who are the key authors mentioned?
```


## Limitations

* No true retrieval (RAG) — entire document is sent to the model
* Large PDFs may exceed context limits
* No citations or source tracking


## Future Improvements

* Add chunking + retrieval (RAG)
* Support multiple PDFs
* Add citations from source text
* Optional web or UI interface


## Tech Stack

* Python 3.11+
* Claude (Anthropic API)
* PyMuPDF (PDF parsing)
* python-dotenv (env management)
* mypy (type checking)
