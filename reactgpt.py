
import streamlit as st
import langchain
from langchain.llms import OpenAI
from langchain import PromptTemplate
import requests


def run_script(training_question,thought1,action1,observation1,thought2,action2,observation2,thought3,action3,observation3,final_question):
    llm = OpenAI(model_name="text-davinci-003", temperature=0, openai_api_key=st.secrets.openai_api_key)
    
    final_question = final_question
    react = f"""
    Question: {training_question} 

    Thought: {thought1}

    Action: Search [{action1}]

    Observation: {observation1}

    Thought: {thought2}

    Action: Search [{action2}]

    Observation: {observation2}

    Thought: {thought3}

    Action: Search [{action3}]

    Observation: {observation3}

    Question:{final_question}
    """
    
    
      
    output_message = llm(react)


    return output_message

def main():

    st.title("ReACTGPT")
    st.write("Try the ReAct (Reasoning+Action) Model to improve accuracy of your ChatGPT search results")


    training_question = st.text_input("Enter your training question (eg: What type of boating license is required to ride a boat in Hudson Bay of New York City?)")
    thought1 = st.text_input("Enter thought 1 (eg: I need to search if boating is allowed in Hudson Bay of New York City)")
    action1 = st.text_input("Enter action 1 [Search Function] (eg: Hudson Bay in New York City)")
    observation1 = st.text_input("Enter observation 1 (Eg: Hudson Bay in New York City allows both leisure and commercial boats including PWCs, Speed Boats, Cruise Ships, Bargers, etc)")
    thought2 = st.text_input("Enter thought 2 (eg: I need to check if boating license is required to ride a boat in Hudson Bay of New York City)")
    action2 = st.text_input("Enter action 2 [Search Function] (eg: Boating License Requirements)")
    observation2 = st.text_input("Enter observation 2 (eg: The New York City requires valid boating license to operate motor powered boats in the Hudson Bay of New York City)")
    thought3 = st.text_input("Enter thought 3 (eg: What type of boating license is required?)")
    action3 = st.text_input("Enter action 3 [Search Function] (eg: Type of Boating License)")
    observation3 = st.text_input("Enter observation 3 (eg: A New York State Boating Safety Certificate is required to operate a motorized vessel, including personal watercraft, in Hudson Bay of New York City.)")
    final_question = st.text_input("Now enter the question for which you need an accurate answer based on the above ReAct training")


    if st.button("Generate Output"):
        result = run_script(training_question,thought1,action1,observation1,thought2,action2,observation2,thought3,action3,observation3,final_question)

        st.write(result)


# Run the app
if __name__ == "__main__":
    main()
