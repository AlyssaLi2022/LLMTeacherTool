# LLM Teacher Tool

**Version:** 0.1.0
**Author:** Wenwen Li (wenwenli@bu.edu)

An AI-powered tool using OpenAI's GPT models to assist educators.

## Features

*   **Generate Material:** Creates teaching content on a topic (brief, medium, or detailed).
*   **Provide Feedback:** Analyzes uploaded `.txt` documents for constructive feedback.
*   **Grade Document:** Evaluates uploaded `.txt` documents against provided criteria.

## Technologies

*   Python 3.9+
*   Streamlit
*   OpenAI API
*   NumPy

## Setup

1.  **Prerequisites:**
    *   Python 3.9+
    *   Git
    *   An OpenAI API Key.

2.  **Set API Key:**
    *   Set your OpenAI API Key as an environment variable named `OPENAI_API_KEY`.

3.  **Clone & Install:**
    ```bash
    # Clone the repository (replace with your actual URL)
    git clone https://github.com/[Your_GitHub_Username]/LLMTeacherTool.git
    cd LLMTeacherTool

    # Create and activate virtual environment
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate

    # Install application and dependencies
    pip install .[app]
    ```

## Running the Web App

1.  Ensure virtual environment is active and `OPENAI_API_KEY` is set.
2.  Navigate to the project directory (`LLMTeacherTool`).
3.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4.  Open the local URL (e.g., `http://localhost:8501`) in your browser.

## (Optional) Command Line Usage

A basic CLI is also available (`pip install .` or `pip install .[app]`).

```bash
# Generate material
teacher-tool generate "Topic Name" -l brief

# Provide feedback (CLI uses placeholder text)
teacher-tool feedback dummy.txt

# Grade document (CLI uses placeholder text)
teacher-tool grade dummy.txt "Criteria..."
Project Structure
app.py: Streamlit web application.
src/doc_analyzer/: Core Python package.
pyproject.toml: Package definition.
README.md: This file.
LICENSE: License file.
.gitignore: Git ignore configuration.
Packaging
This project is packaged as llm_teacher_tool using pyproject.toml. Install with pip install .[app] for the web app or pip install . for the core library/CLI. It provides the teacher-tool command.
