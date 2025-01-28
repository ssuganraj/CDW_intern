from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def code_generator_prompt():
    """
    Generates a prompt template for code generation.
    Returns:
        ChatPromptTemplate: Configured prompt template.
    """
    system_msg = """
    You are an AI assistant specialized in generating code for various programming languages. 
    Your task is to provide precise and efficient code solutions for the given language and problem.
    Always respond with just the code and necessary comments about coding.
    """
    user_msg = """
    Generate code in {language} for the following task:
    {problem}
    """
    return ChatPromptTemplate([("system", system_msg), ("user", user_msg)])

def code_generator_prompt_from_hub():
    """
    Fetches the prompt template from the LangChain Hub.
    Returns:
        ChatPromptTemplate: Configured prompt template from the hub.
    """
    prompt_template = hub.pull("suganraj/code_generator_prompt")
    return prompt_template
