from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emoji here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Ligly Technologies", page_icon=':tada:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json')


#  ------- HEADER SECTION -------
with st.container():
    st.subheader('Hi, I am Dheeraj :wave:')
    st.title('Ligly Technologies')
    st.write('We are changing the world with technology')
    #st.write('[Learn More >](https://Ligly_Technologies.com)')


# ---- What I Do ------
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What We Do')
        st.write('##')
        st.write(
            """
            We help you in :
            - Computer assemble
            - Computer repair
            - Camera sales & Service
            - and more...
            """
        )
        st.write('[Youtube Channel >](https://youtube.com/dheeraj)')
    with right_column:
        st_lottie(lottie_coding, height=400, key='coding')




# ----- Contact forum -----
with st.container():
    st.write('---')
    st.header('Get in touch')
    st.write('##')

    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/dheeraj04K09@gmail.com" method="POST" >
    <input type = 'hidden' name='_captcha' value="false">
    <input type = "text" name="name" placeholder="Your name" required>
    <input type = "email" name="email" placeholder="Your email" required>
    <textarea name = "message" placeholder="Your message here" required></textarea>
    <button type = "submit" > Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
