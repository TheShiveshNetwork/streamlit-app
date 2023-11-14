import streamlit as st
import textblob
import pandas as pd
import cleantext

# st.header("Sentiment Analysis")
st.title('Sentiment Analysis')


text = st.text_area("Enter the text", placeholder="This is a sample text")

if text:
    blob = textblob.TextBlob(text)
    text_polarity = round(blob.sentiment.polarity, 2)
    # st.write('Polarity: ', text_polarity)
    text_subjectivity = round(blob.sentiment.subjectivity, 2)
    # st.write('Subjectivity: ', text_subjectivity)

    if text_polarity > 0:
        st.markdown("Sentiment: Positive :smiley: ")
    elif text_polarity < 0:
        st.markdown("Sentiment: Negative :angry: ")
    else:
        st.markdown("Sentiment: Neutral 😐 ")
        
    sentiment_dict = {"polarity": text_polarity, 'subjectivity': text_subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    st.dataframe(sentiment_df)