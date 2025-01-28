from model import create_chat_groq
import prompts as prompt

def generate_poem(topic):
    '''
    Function to generate a poem
    Args:
        topic(str): The topic of the poem
    Returns:
        response.content(str): 
    '''
    prompt_template = prompt.poem_generator_prompt_from_hub()
    llm = create_chat_groq()

    chain = prompt_template | llm

    response = chain.invoke({"topic": topic})
    return response.content