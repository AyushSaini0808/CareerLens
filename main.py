import streamlit as st
import time
from ui import css_setup
from dotenv import load_dotenv
from PyPDF2 import PdfReader 
from groq import Groq 
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate


#Initialising session state variables
if "messages" not in st.session_state:
    st.session_state.messages=[]
if "resume_text" not in st.session_state:
    st.session_state.resume_text=""
if "job_role" not in st.session_state:
    st.session_state.job_role=""
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete=False


def check_api_key(api_key):
    '''Validate the Groq API key by running a simple test.'''
    
    try:
        client = Groq(api_key=api_key)
        response=client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role":"user","content":"Hello"}],
            max_tokens=20
        )
        return True if response is not None else False
    except Exception as e:
        st.error("Invalid API key. Please check your credentials.")


def sidebar_content():
    '''Function for generating sidebar content.'''
    
    # Only show sidebar content when API key is validated
    if "api_key_validated" in st.session_state and st.session_state.api_key_validated:
        st.sidebar.title("Resume Analyzer")
        st.sidebar.write("Upload your resume to obtain insights.")
        uploaded_file = st.sidebar.file_uploader("Ensure your resume is in PDF format only", type=["pdf"])
        job_role = st.sidebar.text_input("Enter the job role you are applying for", placeholder="Enter the job role")
        
        if uploaded_file and job_role:
            if st.sidebar.button("Analyze Resume"):
                resume_text = extract_text_from_pdf(uploaded_file)
                st.session_state.resume_text = resume_text
                st.session_state.job_role = job_role
                st.session_state.analysis_complete = True
                    
                    # Generate initial analysis
                initial_analysis = analyse_resume(resume_text, job_role)
                st.session_state.resume_analysis = initial_analysis
                    
                    # Add a welcome message to the chat
                system_prompt = f"Resume analysis for {job_role} position is complete. You can now ask questions about your resume or prepare for interviews."
                st.session_state.messages = [AIMessage(content=system_prompt)]
        
        # Display analysis in sidebar if available
        if "resume_analysis" in st.session_state and st.session_state.resume_analysis:
            st.sidebar.divider()
            st.sidebar.subheader("Resume Analysis")
            with st.sidebar.expander("View Analysis", expanded=True):
                st.sidebar.markdown(st.session_state.resume_analysis)
        
        return uploaded_file, job_role
    
    # Return None if API key is not validated
    return None, None

def extract_text_from_pdf(uploaded_file):    
    ''' Function for extracting text from the uploaded pdf file.'''
    pdf_reader=PdfReader(uploaded_file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
    return text

def analyse_resume(resume_text,job_role):
    ''' Analyse the resume content against the job role provided. '''
    client = Groq(api_key=st.session_state.api_key)
    prompt=f'''
    Your task is to analyse the given resume for {job_role} position. Here is the reume text:
    {resume_text}
    Focus on the following aspects:
    1) Content clarity and impact
    2) Skill presentation
    3) Experience description
    4) Specific improvements for {job_role if job_role else "general job applications"}.
    5) Overall impression
    6) 3-5 suggested talking points for the interview
    
    Focus your response in a clear, organised manner.
    '''
    response=client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role":"user","content":prompt}],
        max_tokens=1000,
        temperature=0.3
    )
    
    return response.choices[0].message.content
               
        
def get_interview_questions(resume_text,job_role,question_type="general"):
    ''' Function for generating interview questions based upon resume and job role description.'''
    client=Groq(st.session_state.api_key)
    prompt_mapping={
        'general':f"Generate a challenging but common interview question for {job_role} position based upon this resume :{resume_text[:500]}",
        'technical':f"Generate a technical interview question specifically related to the skills mention in the resume for {job_role} position :{resume_text[:500]}",
        "behavioral": f"Generate a behavioral interview question for a {job_role} position that would help assess soft skills based on this resume: {resume_text[:500]}"    
    }
    prompt=prompt_mapping.get(question_type,prompt_mapping["general"])
    response=client.chat.completions.create(
        model="meta-llama/llama-guard-4-12b",
        messages=[{"role":"user","content":prompt}],
        max_tokens=200,
        temperature=0.6
    )
    return response.choices[0].message.content

def process_user_message(user_message):
    ''' Processes user messages and obtains response from Groq '''
    
    client=Groq(api_key=st.session_state.api_key)
    conversation_history=""
    for msg in st.session_state.messages[-5:]:
        role="User" if isinstance(msg,HumanMessage) else "Assistant"
        conversation_history+=f"{role}:{msg.content}\n"
        
    prompt=f'''
    You are an AI Career Coach and interview preparation assistant. The user has uploaded their resume for {st.session_state.job_role} position.
    Resume : {st.session_state.resume_text[:500]}
    Recent conversation : {conversation_history}
    User's message : {user_message}
    
    Provide a helpful response that assists the user in improving their resume content, skills and interview preparation.
    Be specific, actionable and supportive. If they ask about specific skills or experience from their resume , refer to the content.
    Don't answer questions outside the scope of this application.
    '''

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        max_tokens=1000,
        temperature = 0.3,
        messages=[{"role":"user","content":prompt}]   
    )
    
    return response.choices[0].message.content

def main():
    # Setting up page configurations and API key
    st.set_page_config(page_title="CareerLens - Your AI-powered Resume Analyser and Interview Coach", page_icon="👨🏻‍💻", layout="centered")
    st.markdown(css_setup, unsafe_allow_html=True)
    st.title("Prepify - Your AI Assistant for Interview Preparation")
    st.write("Developed by Ayush Saini")
    
    if "api_key_validated" not in st.session_state:
        st.session_state.api_key_validated=False
        
    if not st.session_state.api_key_validated:
        st.divider()
        st.markdown("This streamlit application is designed to allow users gain insights about their resume against a job position or for any general job application. You can also chat with the assistant to prepare for technical or behavioral interviews.")
        st.markdown("Before you start with the interview preparation process, we would request you to upload the API key for the Groq API. You can obtain the API key from [here](https://groq.com/).")
        st.divider()
        api_key = st.text_input("Please enter your credentials", type="password", placeholder="Enter your Groq API Key")
        if api_key:
            with st.spinner("Validating API Key ... "):
                if check_api_key(api_key):
                    st.session_state.api_key=api_key
                    st.session_state.api_key_validated=True
                    time.sleep(1)
                    st.success("API Key validated successfully.")
                    st.rerun()
                else:
                    st.error("API key failed. Please check your credentials.")
    else:
        # Display the sidebar for resume analysis
        uploaded_file,job_role=sidebar_content()
        
        ## Display chat messages
        for msg in st.session_state.messages:
            if isinstance(msg,HumanMessage):
                with st.chat_message("human"):
                    st.markdown(msg.content)
            else:
                with st.chat_message("ai"):
                    st.markdown(msg.content)
        # Chat input 
        user_input=st.chat_input("Ask anything about your resume or interview preparation ...")
        if user_input:
            # Add the user input to state and display 
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.chat_message("human"):
                st.markdown(user_input)
            # Generating response from Groq
            with st.chat_message("ai"):
                with st.spinner("Thinking ..."):
                    response=process_user_message(user_message=user_input)
                    st.markdown(response)
                    st.session_state.messages.append(AIMessage(content=response))
                
if __name__=="__main__":
    main()
