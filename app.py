import streamlit as st


# Settings:
## Extra CSS:
st.set_page_config(page_title='Sayan Karmakar', page_icon=':computer:', layout='wide')
hide_st_style = '''
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)
st.write('##')

st.subheader('Hey Guys :wave:')
st.title('Sayan Karmakar Portfolio')
st.write('A beginner who knows merely 1% of coding...')
st.write('[Read More](https://www.linkedin.com/in/sayankarmakar007/)')

