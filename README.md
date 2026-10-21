# Python AI Learning Project

A beginner-friendly repository for learning Python and building practical AI projects.

## Project Structure

```text
python-ai/
├── code/
│   ├── lesson_01_intro.py
│   └── project_m1_prompt_kit.py
├── docs/
│   ├── Lesson_02_Python.md
│   ├── image.png
│   ├── project-m1-results.md
│   └── project-m1-run.png
├── notebooks/
├── src/
│   └── python_ai/
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## Setup

This project uses Python 3.13 and [uv](https://docs.astral.sh/uv/) for Python project and dependency management.

Install the project dependencies:

```bash
uv sync
```

Run the starter program:

```bash
uv run python
```

## Module 1 Project: AI Prompt Kit

The **AI Prompt Kit** is a Python command-line tool that collects basic information about a local business and generates three ready-to-use AI prompts.

### What it does

1. **Marketing:** Generates a prompt for a social media post.
2. **Customer Service:** Generates a prompt for replying politely to an unhappy customer whose delivery was late, including an apology and a small discount.
3. **Business Growth:** Generates a prompt requesting three low-cost AI tools or ideas suited to the business, its customers, location, and monthly budget in PKR.

### Technologies

- Python 3.13
- Python `input()` and `print()`
- Variables, comments, and f-strings
- Integer conversion using `int()`
- Ollama with a local language model for testing the generated prompts

### How to run

From the project root directory, run:

```bash
uv run code/project_m1_prompt_kit.py
```

Enter the business name, business type, city, main customers, and monthly budget when prompted.

### Demo

![AI Prompt Kit running in the terminal](docs/project-m1-run.png)

### Prompt Testing and Results

The generated prompts are tested with Ollama. The model's actual responses, usefulness observations, and any hallucinations or unsupported claims are documented here:

[View Prompt Testing Results](docs/project-m1-results.md)

### Who would benefit?

Small business owners who want to use AI for marketing, customer service, and business growth but need help writing effective prompts.

## Learning Goals

- Practise Python fundamentals through practical projects.
- Learn how to write clear, structured prompts for AI models.
- Evaluate AI responses for usefulness and accuracy.
- Build a portfolio of beginner-friendly Python and AI projects.
