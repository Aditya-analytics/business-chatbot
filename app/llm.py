import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME

# --------------------------------------
# Configure Gemini with API key
# --------------------------------------

genai.configure(api_key=GEMINI_API_KEY)

# Create model instance
model = genai.GenerativeModel(MODEL_NAME)


# --------------------------------------
# Generate Response Function
# --------------------------------------

def generate_response(prompt: str) -> str:
    """
    Sends a prompt to Gemini model
    and returns the generated text response.
    """

    try:
        response = model.generate_content(prompt)

        # Ensure response has text
        if response.text:
            return response.text.strip()
        else:
            return "No response generated."

    except Exception as e:
        return f"Error generating response: {str(e)}"

print(generate_response("Hello who are you ?"))