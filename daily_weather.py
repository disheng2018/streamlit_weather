import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://tianqi.moji.com/weather/china", height=450,scrolling=True)

if st.button('获取'):
    st.write("最新网址：")
else:
    st.write('最新网址')