import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


with st.container():
    st.subheader("Hi! My name is Yoona :wave:")
    st.title("My Dream :star:")
    st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dui nunc mattis enim ut. In vitae turpis massa sed. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Laoreet suspendisse interdum consectetur libero id. Eget duis at tellus at. Sem integer vitae justo eget magna fermentum iaculis. Mauris vitae ultricies leo integer malesuada nunc vel. Nisi est sit amet facilisis magna etiam tempor. Quisque non tellus orci ac auctor augue mauris augue. Nullam eget felis eget nunc. Posuere ac ut consequat semper. Montes nascetur ridiculus mus mauris vitae ultricies leo.
    """)
    st.write("[visit my blog >](https://kstyle7.kr)")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_oc9peor8.json")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa ultricies mi quis hendrerit. Augue interdum velit euismod in pellentesque. Viverra vitae congue eu consequat ac felis donec et. Adipiscing bibendum est ultricies integer quis. Accumsan in nisl nisi scelerisque eu. Scelerisque viverra mauris in aliquam sem. Odio aenean sed adipiscing diam donec adipiscing tristique. Non curabitur gravida arcu ac tortor. Bibendum neque egestas congue quisque egestas diam. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Quis risus sed vulputate odio ut enim. Ullamcorper sit amet risus nullam. Convallis posuere morbi leo urna molestie at elementum. Adipiscing elit pellentesque habitant morbi tristique senectus et netus.\n
        Lobortis elementum nibh tellus molestie nunc non blandit massa enim. Laoreet id donec ultrices tincidunt arcu non sodales neque sodales. Ac turpis egestas integer eget aliquet nibh. Ornare quam viverra orci sagittis eu volutpat. Auctor neque vitae tempus quam pellentesque nec. Sit amet nulla facilisi morbi tempus iaculis urna id. Etiam dignissim diam quis enim. Non pulvinar neque laoreet suspendisse interdum consectetur libero id. Venenatis cras sed felis eget velit aliquet. Congue quisque egestas diam in. Elementum tempus egestas sed sed risus pretium quam vulputate. At elementum eu facilisis sed odio morbi quis. Proin libero nunc consequat interdum varius sit. In est ante in nibh mauris cursus mattis molestie a. Turpis in eu mi bibendum neque egestas congue. Laoreet id donec ultrices tincidunt arcu non sodales.
        """)

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


sample_image = Image.open("image/dog.jpg")

with st.container():
    st.write("---")
    st.header("My dog")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(sample_image)


    with text_column:
        st.subheader("Lorem ipsum dolor sit amet")
        st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """)






