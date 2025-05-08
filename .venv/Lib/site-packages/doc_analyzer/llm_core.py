# src/doc_analyzer/llm_core.py
import os
from openai import OpenAI

# --- Load API Key ---
# Get API key directly from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key was found in the environment
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found. Please ensure it is set.")

# --- Initialize OpenAI Client ---
# Use the loaded API key to initialize the client
try:
    client = OpenAI(api_key=api_key)
    print("OpenAI client initialized successfully.") # Confirmation message
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    raise # Stop execution if client fails

# --- Client Accessor ---
def get_llm_client():
    """Returns the initialized OpenAI client."""
    if 'client' not in globals() or not isinstance(client, OpenAI):
         raise RuntimeError("OpenAI client is not initialized.")
    return client

# --- Test Function ---
def test_llm_connection():
    """Sends a simple test request to the LLM."""
    print("Attempting LLM connection test...")
    local_client = get_llm_client() # Get client via function
    try:
        completion = local_client.chat.completions.create(
          model="gpt-3.5-turbo", # Or another model like gpt-4o-mini
          messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'Hello, World!'"}
          ]
        )
        message_content = completion.choices[0].message.content
        print("LLM Connection Test Successful!")
        print(f"LLM Response: {message_content}")
        return message_content
    except Exception as e:
        print(f"Error during LLM connection test: {e}")
        return None

# --- Placeholder for future functions ---
# def generate_material(topic):
#     pass
# def provide_feedback(document_text):
#     pass
# def grade_document(document_text, criteria):
#     pass

