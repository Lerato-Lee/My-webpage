import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

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
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_wqypnpu5.json")
img_kindpng_1280357 = Image.open("images/kindpng_1280357.png")
img_Lee_in_tech = Image.open("images/Lee_in_tech.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Lerato! :wave:")
    st.title("A Software Engineer From Durban, South Africa")
    st.write("I have interests in solving real life problems through technology, because technology rules- society follows!")
    st.write("Learn More >](https://Leecodes.com)")

   # ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            My interests range from software engineering ,administration, customer service, IT in general.
            I am front-end passionate, backend curious with interests in solving real life problems through technology and dependable leadership.
            An avid reader exploring Information Technology advancements and personal development through books.
            Technology leads, society follows.
            The move towards increasing diversity and inclusivity through representation is of importance to me.
            I am excited to take the leap and continue refining my skills with the right company!
            """
        )
        st.write("[Github Profile >](https://github.com/Lerato-Lee)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_kindpng_1280357)
    with text_column:
        st.subheader("Learn how to track phone number location using Python!")
        st.write(
            """
            Learn how to track phone number location using Python 
            with just 6 lines of code!
            This also enables you to check which carrier the caller is using.
            Please click link below for source code
            """
        )
        st.markdown("Click Link For Source code...](https://github.com/Lerato-Lee/Track-Number)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_Lee_in_tech)
        with text_column:
            st.subheader("A simple Mad-Libs-Game Using Python.")
            st.write(
                """
                A simple, but creative and funny  Mad-Libs-Game.
                It consists of one player prompting others for a list of words to substitute 
                for blanks in a story before reading aloud.
                """
            )
            st.markdown("Link available..](https://github.com/Lerato-Lee/Mad-Libs-Game)")

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESSS TO YOURS !!!
        contact_form = """
        <form action="https://formsubmit.co/mthimkhululerato72@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()