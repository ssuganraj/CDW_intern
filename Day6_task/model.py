from langchain_groq import ChatGroq

def create_chat_groq():
    """
    Function to initialize the Groq model.
    Returns:
        ChatGroq: The initialized Groq model.
    """
    return ChatGroq(
        model="mixtral-8x7b-32768",  # Replace with the appropriate model
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3
    )
