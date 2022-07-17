import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

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
col1, col2, col3 = st.columns(3)
with col1:

    st.subheader("요도가와 불꽃놀이의 윤아")
    with st.container():
        st.markdown('''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Neque volutpat ac tincidunt vitae semper quis lectus nulla. Sed risus ultricies tristique nulla aliquet enim tortor at.
        ''')
    with st.container():
        image = Image.open("./src/불꽃놀이.jpg")
        st.image(image, caption="오사카 윤아", use_column_width=True)    

with col2:
    st.subheader("윤지와 미니언즈")
    st.empty()
    with st.container():
        st.markdown('''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Neque volutpat ac tincidunt vitae semper quis lectus nulla. Sed risus ultricies tristique nulla aliquet enim tortor at.
        ''')
    with st.container():
        image = Image.open("./src/미니언즈.jpg")
  
        st.image(image, caption="윤지와 미니언즈", use_column_width=True)    

with col3:

    st.subheader("롤러코스터는 재밌어!")
    st.empty()
    with st.container():
        st.markdown('''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Neque volutpat ac tincidunt vitae semper quis lectus nulla. Sed risus ultricies tristique nulla aliquet enim tortor at.
        ''')
    with st.container():
    ## insert video
        video_file = open('./src/롤러코스터.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)


st.markdown("---")

# add gif image
import base64

col4, col5 = st.columns(2)

with col4:
    with st.container():
        file_ = open("./src/test6.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True
        )

with col5:
    with st.container():
        st.markdown("""
        #### 풀이 패, 때 불러 밤이 이름을 속의 있습니다. 별빛이 같이 하늘에는 슬퍼하는 내 책상을 가득 있습니다. 나는 하나에 다하지 벌레는 까닭이요, 별에도 묻힌 별 있습니다. 별 가슴속에 하나에 못 속의 쉬이 새워 사람들의 계십니다. 겨울이 시와 나는 봄이 밤이 너무나 별빛이 무성할 많은 까닭입니다. 당신은 위에도 된 이국 있습니다. 계집애들의 하나에 노새, 옥 위에 한 애기 동경과 피어나듯이 버리었습니다.
        #### 강아지, 가슴속에 라이너 내린 나는 멀리 하나에 된 있습니다. 패, 추억과 지나고 별들을 이름자 버리었습니다. 별 벌레는 남은 파란 옥 듯합니다. 헤일 애기 것은 계절이 나는 있습니다. 어머니, 가난한 별 가을 하나의 추억과 버리었습니다.
        """)

st.markdown("---")



with st.container():
    image = Image.open("./src/김제나들이.jpg") 
    image = image.convert("1")
    st.image(image, caption="ddd", use_column_width=True)    


st.markdown("---")


# add Expander Area
with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.bar_chart(np.random.randn(50, 3))

st.markdown("---")

# add Plotly chart
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# adjust heght of column

import streamlit as st
empty1,content1,empty2,content2,empty3=st.columns([0.3,1.2,0.3,1.2,0.3])
with empty1:
        st.empty()
with content1:
        st.write("here is the first column of content.")
with empty2:
        st.empty()
with content2:
        st.write("here is the second column of content.")
with empty3:
        st.empty()

# st.empty test
import time

with st.empty():
# with st.container():

     for seconds in range(60):
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ 1 minute over!")

