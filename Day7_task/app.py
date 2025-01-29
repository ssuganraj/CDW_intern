import streamlit as st
import chains
import vectordb

def code_generator_app():
    """
    Generates Code Generator App with Streamlit, providing user input and displaying output.
    Includes a sidebar with two sections: Code Generator and File Ingestion for RAG.
    """

    # Sidebar configuration
    st.sidebar.title("Menu")
    section = st.sidebar.radio(
        "Choose a section:",
        ("Code Generator RAG", "RAG File Ingestion")
    )

    # db initialization
    vectordatabase = vectordb.initialize_chroma()

    # Condition for code generation page
    if section == "Code Generator RAG":
        st.title("Let's generate some code! 👨‍💻")

        with st.form("code_generator"):
            # Input for the programming language
            language = st.selectbox(
                "Select the programming language:",
                ("Python", "JavaScript", "C++", "Java", "Ruby", "Go", "PHP")
            )
            
            # Input for the problem
            problem = st.text_input(
                "Enter the problem or task for code generation:"
            )
            submitted = st.form_submit_button("Submit")

            toggle_state = st.checkbox("Check me to enable RAG")

            if submitted:
                if toggle_state:
                    # Passing both problem and language for code generation with RAG
                    response = chains.generate_code_rag_chain(language, problem, vectordatabase)
                else:
                    # Passing both problem and language for basic code generation
                    response = chains.generate_code_chain(language, problem)
                
                st.code(response, language=language.lower())
    
    # Condition for RAG File Ingestion
    elif section == "RAG File Ingestion":
        st.title("RAG File Ingestion")

        uploaded_file = st.file_uploader("Upload a file:", type=["txt", "csv", "docx", "pdf"])

        if uploaded_file is not None:
            vectordb.store_pdf_in_chroma(uploaded_file, vectordatabase)
            st.success(f"File '{uploaded_file.name}' uploaded and file embedding stored in vectordb successfully!")

code_generator_app()
