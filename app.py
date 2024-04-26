import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from st_social_media_links import SocialMediaIcons


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


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottier_icon = load_lottieur('https://lottie.host/90a6f7a7-36ce-4768-bc5e-d469d7a620ed/qhZaWE5nuU.json')


st.subheader('Hey Guys :wave:')
st.title('Sayan Karmakar Portfolio')
st.write('A beginner who knows merely 1% of coding...')
st.write('[Read More](https://www.linkedin.com/in/sayankarmakar007/)')
st.write('---')


with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Background', 'Projects', 'Contacts'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )

if selected == 'Background':
    col1, col2 = st.columns(2)
    with col1:
        st.write('##')
        st.subheader('I am Sayan Karmakar')
        st.title('Undergrad at IIIT')

        social_media_links1 = [
            'https://github.com/ProPython007/',
            'https://www.linkedin.com/in/sayankarmakar007/'
        ]
        social_media_links2 = [
            'https://www.instagram.com/diode002/',
            'https://www.facebook.com/ProPythonn',
            'https://www.youtube.com/@ProPython',
        ]

        social_media_icons = SocialMediaIcons(social_media_links1)
        social_media_icons.render()
        social_media_icons = SocialMediaIcons(social_media_links2)
        social_media_icons.render()

    with col2:
        st_lottie(lottier_icon)

    st.write('---')

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader('''
            Education
            - IIIT
                - Bachelor of Technology -Computer Science
                - Grade: 9.2
                        
            - Kendriya Vidyalaya No.1 Ishapore
                - CBSE class 12th
                - Grade: 8.4
                         
            - Kendriya Vidyalaya Kankinara
                - CBSE class 10th
                - Grade: 8.88
            ''')
        with col4:
            st.subheader('''
            Experience
            - Freelancer @[profile](https://www.freelancer.com/u/propython007)
                - May 2022 - Present
                - Remote
                - Description: Executed diverse projects leveraging my expertise, ensuring on-time and quality delivery. Accomplished 40+ projects across industries, earning a top 5/5 rating from satisfied clients.
            ''')




