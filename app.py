import streamlit as st

st.write('welcome to...')

st.title("Anuja Raktate's Portfolio :sunglasses:")
st.write("**:blue[Data Scientist / Data Analyst]**" )
st.write("**_Hello!_**:wave:")
st.markdown("I'm Aspiring to Become Data Scientist with a good knowledge. Eager to Learn New Things and Try My Knowledge to Help to Grow The Technology Field. Moving towards my Goals and to go on top Having good Qualities to Lead a Team. Skilled in Python, Data Analysis and Web Development.")
st.caption("Let's Connect:-")
st.snow()

btn_click = st.button("Click Here To Connect On LinkedIn")

if btn_click == True:
    st.subheader("**:blue[https://www.linkedin.com/in/anuja-raktate-a61413171/]**")
    st.balloons()  

btn_click = st.button("Click Here To Connect On GitHub")

if btn_click == True:
    st.subheader("**:blue[https://github.com/Anujaraktate]**")
    st.balloons() 