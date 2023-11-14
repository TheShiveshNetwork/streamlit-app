import streamlit as st
import textblob
import pandas as pd
import cleantext

# st.header("Sentiment Analysis")
st.title('Sentiment Analysis')


text = st.text_area("Enter the text", placeholder="This is a sample text")

if text:
    blob = textblob.TextBlob(text)
    st.write('Polarity: ', round(blob.sentiment.polarity, 2))
    st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))