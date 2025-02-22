import streamlit as st
st.snow()
st.sidebar.success("Welcome to Streamlit Web App")
st.title("Challenge of Growth Mindset \n ## Web App with Streamlit")

str = "print('Hello World')"
st.code(str)
st.markdown('[learn-modern-ai-python](https://github.com/panaversity/learn-modern-ai-python.git)')
st.metric(label="Win Speed", value='40ms', delta=99.097)

st.markdown("---")

st.header("*Learn Streamlit!*")
st.markdown("We will learn from these resources :")
st.markdown('[A Beginners Guide To Streamlit](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)')
st.markdown('[Streamlit for Data Science: Create interactive data apps in Python 2nd ed. Edition](https://www.amazon.com/Streamlit-Data-Science-Create-interactive/dp/180324822X/ref=sr_1_1)')
str2 = "pip install streamlit"
st.code(str2)
st.markdown('[https://docs.streamlit.io/library/get-started/installation](https://docs.streamlit.io/get-started/installation)')
st.markdown('[https://docs.streamlit.io/library/cheatsheet](https://docs.streamlit.io/library/cheatsheet)')


st.image('images/Heads.jpg',caption='AWARDS SAMINNAR SIR ZIA KHAN')
st.video('mp4/Rose.mp4', loop=True )
