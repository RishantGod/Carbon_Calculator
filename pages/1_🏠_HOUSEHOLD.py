import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.form("household_data"):
   add_vertical_space(1)
   st.subheader('🏡 ABOUT YOUR HOUSEHOLD')
   col1, col2, col3 = st.columns(3)
   with col1:
      household_number = st.number_input('No. of people in the household', 1, 10)
   with col2:
      house_size = st.number_input("Size of housing (m2)",50,200)
   with col3:
      house_type = st.selectbox("Type of housing", ['Detached','Semi Detached', 'Attached single family home','Flat'])
   add_vertical_space(3)
   st.subheader('💡 ENERGY CONSUMPTION')
   col1 , col2 = st.columns(2)
   with col1:
      electricity_consumption = st.select_slider('Electricity consumption',['Very Less','Less','Average','High','Very High'], 'Average')
   with col2:
      heating_energy_source = st.selectbox('Heating energy source',['Coal','Natural gas','Heating Oil', 'Wood', 'Vegetable oil', 'Peat', 'Charcoal', 'Electrical'])
      if_heating = st.checkbox("I don't know the source")
   submit = st.form_submit_button('Next')
   if submit:
    switch_page('TRANSPORT')
