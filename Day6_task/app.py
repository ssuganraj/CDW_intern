from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

# Initialize the memory store in the session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # A list to store chat context

def code_generator_app():
    """Streamlit app for code generation"""
    st.title("Code Generator App")
    st.write("Generate code for a specific programming language and problem.")
    
    # Display chat history
    st.subheader("Chat History")
    if st.session_state.chat_history:
        for entry in st.session_state.chat_history:
            st.markdown(f"**User:** {entry['user_input']}")
            st.code(entry['response'], language=entry['language'])

    # User input form
    with st.form("code_generator_form"):
        language = st.text_input("Enter the programming language (e.g., Python, Java):")
        problem = st.text_area("Describe the problem or task:")
        submitted = st.form_submit_button("Generate Code")

        if submitted:
            if not language or not problem:
                st.error("Both language and problem are required!")
            else:
                try:
                    # Generate code
                    response = chain.generate_code(language, problem)

                    # Save the interaction to chat history
                    st.session_state.chat_history.append({
                        "user_input": f"Language: {language}, Problem: {problem}",
                        "response": response,
                        "language": language.lower()
                    })

                    # Display the response
                    st.code(response, language=language.lower())
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    # Option to clear chat history
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")

if __name__ == "__main__":
    code_generator_app()
