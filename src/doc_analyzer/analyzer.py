# src/doc_analyzer/analyzer.py
from .llm_core import get_llm_client # Import the function to get the client

# Get the initialized OpenAI client
client = get_llm_client()

def generate_material(topic: str, length: str = "brief") -> str:
    """
    Generates teaching material on a given topic using the LLM.

    Args:
        topic: The subject or topic for the material.
        length: Desired length ('brief', 'medium', 'detailed').

    Returns:
        The generated teaching material as a string, or an error message.
    """
    print(f"--- Received request to generate {length} material for topic: {topic} ---")

    # --- Define LLM instruction based on length ---
    length_instruction = ""
    if length == "medium":
        length_instruction = "Provide a medium amount of detail."
    elif length == "detailed":
        length_instruction = "Provide comprehensive and detailed information."
    else: # Default to brief
        length_instruction = "Keep it concise and brief."

    # --- Construct the prompt for the LLM ---
    system_prompt = "You are an AI assistant designed to help teachers create educational content."
    user_prompt = f"Generate teaching material about the topic: '{topic}'. {length_instruction} Focus on clarity and accuracy suitable for a classroom setting."

    try:
        print("--- Sending request to LLM for material generation... ---")
        # --- Actual LLM API Call ---
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo", # Or gpt-4o-mini for potentially better quality/cost balance
          messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
          ],
          temperature=0.7, # Adjust creativity (0.0=deterministic, 1.0=more creative)
          max_tokens=1000  # Limit response length (adjust as needed)
        )

        # Extract the response content
        result = completion.choices[0].message.content
        print("--- LLM response received successfully ---")

    except Exception as e:
        print(f"--- Error during LLM call for material generation: {e} ---")
        result = f"Error generating material: {e}"

    return result.strip() # Return the result, removing leading/trailing whitespace

# In src/doc_analyzer/analyzer.py

def provide_feedback(document_text: str) -> str:
    """
    Provides feedback on the provided document text using the LLM.

    Args:
        document_text: The text of the document (e.g., student essay).

    Returns:
        The generated feedback as a string, or an error message.
    """
    print("--- Received request to provide feedback ---")

    # --- Construct the prompt for the LLM ---
    system_prompt = "You are an AI assistant providing constructive feedback on written work, like a helpful teacher."
    # Ensure the document text is clearly delineated in the prompt
    user_prompt = f"Please provide constructive feedback on the following document:\n\n---\n{document_text}\n---\n\nFocus on clarity, organization, and potential areas for improvement."

    try:
        print("--- Sending request to LLM for feedback... ---")
        # --- Actual LLM API Call ---
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo", # Or gpt-4o-mini
          messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
          ],
          temperature=0.5, # Lower temperature for more focused feedback
          max_tokens=500   # Adjust token limit based on expected feedback length
        )

        # Extract the response content
        result = completion.choices[0].message.content
        print("--- LLM response received successfully ---")

    except Exception as e:
        print(f"--- Error during LLM call for feedback: {e} ---")
        result = f"Error generating feedback: {e}"

    return result.strip()

# In src/doc_analyzer/analyzer.py

def grade_document(document_text: str, criteria: str) -> str:
    """
    Grades the document based on given criteria using the LLM.

    Args:
        document_text: The text of the document.
        criteria: The grading criteria or rubric.

    Returns:
        The generated grade and comments as a string, or an error message.
    """
    print(f"--- Received request to grade document based on criteria: {criteria} ---")

    # --- Construct the prompt for the LLM ---
    system_prompt = "You are an AI assistant evaluating a document based on specific criteria, acting as a fair and objective grader."
    # Clearly separate the document and criteria in the prompt
    user_prompt = f"Please grade the following document based *only* on these criteria:\n\n[Criteria]:\n{criteria}\n\n[Document]:\n{document_text}\n\nProvide a score (e.g., out of 10) and specific comments explaining the score based on the criteria."

    try:
        print("--- Sending request to LLM for grading... ---")
        # --- Actual LLM API Call ---
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo", # Or gpt-4o-mini
          messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
          ],
          temperature=0.3, # Lower temperature for more objective grading
          max_tokens=400   # Adjust token limit
        )

        # Extract the response content
        result = completion.choices[0].message.content
        print("--- LLM response received successfully ---")

    except Exception as e:
        print(f"--- Error during LLM call for grading: {e} ---")
        result = f"Error grading document: {e}"

    return result.strip()