from model import create_chat_groq
import prompts as prompt

def generate_code(language, problem):
    """
    Function to generate code for a specific problem and language.
    Args:
        language (str): The programming language.
        problem (str): The problem description.
    Returns:
        str: Generated code.
    """
    # Fetch the prompt template
    prompt_template = prompt.code_generator_prompt_from_hub()
    
    # Create the model
    llm = create_chat_groq()
    
    # Combine prompt and model
    chain = prompt_template | llm
    
    # Invoke the chain with inputs
    response = chain.invoke({"language": language, "problem": problem})
    return response.content
