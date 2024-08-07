# this is a streamlit app that allows use the llm for assessment design
import streamlit as st
from openai import OpenAI
import os

# add your openAI key as environment varialbe
os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]
# create a client to make the call
client = OpenAI()


#st.set_page_config(layout="wide")
# define functions ----------

def spanish_translate(sentence,target_language='spanish'):
    response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0,
    messages = [
        {"role": "system", "content": f"You are a translator who can translate english into {target_language}."},
        {"role": "user", "content": f"Translate the following English text to {target_language}:{sentence}"}
        ])
    return response.choices[0].message.content


def text_analysis(sentence):
    response = client.chat.completions.create(

      model="gpt-4o",
      temperature=0,
      messages = [

        {"role": "system", "content": "You are an expert of grammars of English and Spanish."},

        {"role": "user", "content": f"Please check if the following texts have grammar and spelling errors. Here is the texts: {sentence}"}

      ])
    return response.choices[0].message.content

def age_analysis(sentence,age_group):
    response = client.chat.completions.create(

      model="gpt-4o",
      temperature=0,
      messages = [

        {"role": "system", "content": "You are an expert who can tell whether some text is appropriate for an age group"},

        {"role": "user", "content": f"Please check if the following texts is appropriate for the following age group:{age_group} and provide a brief reason. Here is the texts: {sentence}"}

      ])
    return response.choices[0].message.content


st.title("Item Evaluation")
st.markdown('This is a simple app to evaluate items by using ChatGPT API. For questions, please contact: <jingchenhao@gmali.com>')
st.markdown('---')

st.markdown("### Please enter your item to start:")
item = st.text_area("",height=400)

st.markdown('### 1. Check language usage of the item')
if st.button('Click to check the language'):
    text_analysis_result = text_analysis(item)
    st.write(text_analysis_result)

st.markdown('### 2. Check age appropriateness')
age = st.selectbox('Please select an age group',options=["Elementary School",'Middle School','High School','College and above'])
if st.button('Click to check'):
    result = age_analysis(item,age)
    st.write(result)

st.markdown('### 3. Get a Spanish version')
if st.button('Click to translate the item into Spanish'):
    spanish_translation = spanish_translate(item,"spanish")
    st.write(spanish_translation)