import streamlit as st
from PIL import Image
import numpy as np

# page setting
st.set_page_config(page_title="My Side Project", page_icon=":dolphin:", layout="wide")

# heading part
st.subheader("new Challenge")
st.title("My Side Project1")
st.markdown("---")
st.write('''
얼음이 트고, 눈에 내려온 그들은 청춘은 이것이야말로 스며들어 부패뿐이다. 생명을 위하여서 많이 열락의 그들의 사막이다. 거친 위하여, 뜨거운지라, 끓는 청춘을 유소년에게서 것이다. 넣는 품고 인생을 이상의 가치를 밥을 것이다.보라, 우는 사막이다. 미묘한 눈에 두손을 그들은 그리하였는가? 아름답고 위하여 부패를 우리의 불러 보라. 곳으로 트고, 없는 얼음과 있으랴? 미묘한 살 청춘의 속에서 듣기만 운다. 청춘은 가슴이 그들은 끓는 노년에게서 그들은 끝까지 피가 황금시대의 칼이다. 하는 목숨을 피고 약동하다.
''')

# sider bar

with st.sidebar:
    st.title("Siderbar")
    st.markdown("이성은 **인간**에 끓는 청춘에서만 보라. 얼마나 우는 꽃이 속에서 청춘의 평화스러운 위하여, 뿐이다. 그들에게 그와 인간에 피에 같은 인생에 목숨이 날카로우나 우리 사막이다. 얼음에 있음으로써 뼈 있는 없는 물방아 이상의 운다.")
    st.markdown("---")
    st.write("Manu1")
    st.write("Manu2")
    st.write("Manu3")
    st.write("Manu4")


# Main body

## divide columns
left_col, right_col = st.columns(2)
with left_col:

    st.subheader("Left Column")

    with st.container():
        st.markdown('''
        |a|b|c|
        |-|-|-|
        |1|2|3|
        ''')

    with st.container():
        dog_image = Image.open("./src/dog.jpg")
        st.image(dog_image, caption="My Dog")    

with right_col:

    st.subheader("Right Column")

    with st.container():
        st.markdown('''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Neque volutpat ac tincidunt vitae semper quis lectus nulla. Sed risus ultricies tristique nulla aliquet enim tortor at.
        ''')
    with st.container():
    ## insert video
        video_file = open('./src/20200721_124548.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)


st.markdown("---")

# add Expander Area
with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.bar_chart(np.random.randn(50, 3))