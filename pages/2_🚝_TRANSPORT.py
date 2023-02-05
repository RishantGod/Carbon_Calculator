import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space

st.pyplot


st.header('Transport')


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.form("transport_data"):
    st.subheader('🚌 HOW DO YOU GET AROUND?')
    col1, col2, col3 = st.columns(3)
    st.write('Average hours per week traveled by:')
    with col1:
        car = st.number_input('Car', 0, 10)
    with col2:
        city_bus = st.number_input('Intercity Train', 0, 10)
    with col3:
        bike_walk = st.number_input('Bike/walk', 0, 10)
    add_vertical_space(3)
    st.subheader('🛩️ PRIVATE FLIGHTS PER YEAR FOR ALL HOUSEHOLD MEMBERS:')
    very_long_range = st.number_input('Very long range round-trip flights (>12000 km or >14 hours one way) per year',0,50)
    long_range = st.number_input('Long range round-trip flights (<12000 km or <14 hours one way) per year',0,50)
    med_range = st.number_input('Medium range round-trip flights (<6000 km or <8 hours one way) per year',0,50)
    short_range = st.number_input('Short range round-trip flights (<3000 km or <6 hours one way) per year',0,50)
    submit = st.form_submit_button('Next')
    if submit:
        switch_page('LIFESTYLE')