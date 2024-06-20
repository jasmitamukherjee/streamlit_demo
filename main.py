import streamlit as st
st.write("hi its me")
st.selectbox("which prog language do you like?",["python","java","c++"])
st.checkbox("python")
st.checkbox("java")

st.checkbox("c++")

st.checkbox("django")
st.slider("Pick some value between 0-100",0,100)
st.select_slider("select entry",["best",'average','worst'])
st.progress(10)
#sidebar 
st.sidebar.title("about me")
st.sidebar.selectbox("your fav animal",['dog','cat','monkey'])
st.sidebar.markdown("info")
st.sidebar.button("press in")
st.button("press out")