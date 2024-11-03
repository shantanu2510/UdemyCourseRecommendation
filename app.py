import streamlit as st
import google.generativeai as genai
import os


os.environ['API_KEY'] = "AIzaSyAlzvE1sWUf_Ivlr3pfaEMW6wV_7PIRCVA"
# genai.configure(api_key=os.environ["API_KEY"])

def call_gemini_api(user_input):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Extract topics from the following user input to query Udemy search and display only the topics. the format should be query: (all the topics) : " + user_input
    response = model.generate_content(prompt)
    
    if response and response.text:
        st.write(response.text)
    else:
        st.write("No content generated from Gemini LLM.")
    
    return response


st.title("Udemy Course Finder with Gemini LLM")


course_requirements = st.text_area(
    "Enter your course requirements:",
    placeholder="Example: I want to learn Machine Learning, Generative AI, and Azure technologies. I prefer courses with practical projects."
)


if st.button("Find Courses"):
    st.write("Your course requirements are:")
    st.write(course_requirements)
    
   
    st.write("Processing your request with Gemini LLM...")
    response = call_gemini_api(course_requirements)
    
    
    st.write("Searching for courses... (Udemy integration pending)")