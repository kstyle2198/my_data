import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from EDA import eda


st.set_page_config(page_title="My Data", page_icon=":bar_chart:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_dews3j6m.json")
with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home", "EDA", "Test1"],
    icons = ["house", "book", "envelop"],
    menu_icon="cast",
    default_index=0
    )


def main():

    col1, col2= st.columns([3,1])
    with col1:
        with st.container():
            st.title(":sunny: My Data Science")
            st.subheader("The best way to learn Data Science is 'Just Do Data Science'")
    with col2:
        with st.container():
            st_lottie(lottie_coding, height=300, key="coding")
    
    st.markdown("---")

    l_col, r_col = st.columns(2)
    with l_col:
        with st.container():
            image = Image.open("./media/what-is-data-science.jpg")
            st.image(image, caption="Data Science", use_column_width=True)
    with r_col:
        with st.container():
            st.markdown("""
            #### ***Data science***  is an essential part of many industries today, given the massive amounts of data that are produced, and is one of the most debated topics in IT circles. Its popularity has grown over the years, and companies have started implementing data science techniques to grow their business and increase customer satisfaction.
            """)



    st.markdown('#### :email: Get in Touch with me')
    contact_form = '''
    <form action="https://formsubmit.co/jongbaekim0710@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name="message" placeholder="Your messages"></textarea>
        <button type="submit">Send</button>
    </form>
    '''
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

if __name__ == "__main__":

        if selected == "Home":
            main()
        elif selected == "EDA":
            eda()

