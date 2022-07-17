import pandas_profiling
import streamlit as st
from pydataset import data
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv
import codecs
import streamlit.components.v1 as components

st.set_page_config(page_title="My Data", page_icon=":bar_chart:", layout="wide")

def st_disply_sweetviz(report_html, width=2000, height=1000):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, width=width, height=height, scrolling=True)

def eda():

    st.title("Exploratory Data Analysis(EDA) :chart_with_upwards_trend:")
    st.markdown("---")

    st.subheader("Select Data")
    option = st.selectbox('', ['iris', 'Boston'])
    df = data(option)

    with st.expander("Click! to see Data Summary"):
        st.dataframe(df.describe())

    st.subheader("Select EDA Library")
    option = st.selectbox("",['None','Pandas-Profiling','Sweetviz'])

    if option == "Pandas-Profiling":
        st.header("EDA with Pandas-Profiling")
        pr = df.profile_report()
        st_profile_report(pr)
        st.balloons()

    elif option == "Sweetviz":
        st.header("EDA with Sweetviz")
        df = df
        report = sv.analyze(df)
        report.show_html()
        st_disply_sweetviz("SWEETVIZ_REPORT.html")
        st.balloons()

if __name__ == "__main__":
    eda()