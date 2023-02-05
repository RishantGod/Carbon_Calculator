import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



with st.form('Lifestyle_data'):
    st.subheader('🍽️ ABOUT YOUR LIFESTYLE')
    preferred_diet = st.selectbox('Your household preferred diet is',['Meat in most meals','Meat in some meals', 'Meat very rarely', 'Vegetarian','Vegan'])
    local_products = st.selectbox('Do you buy mostly local products?',["I'm not considering this option",'Sometimes','Always'])
    responsible_sources = st.selectbox('Do you buy from environmentally responsible companies?',["I'm not considering this option",'Sometimes','Always'])
    eat_out = st.number_input('How many times a week does your family eat out?',0,25)
    add_vertical_space(3)
    st.subheader('🗑️ HOW DO YOU HANDLE WASTE?')
    recycle_level = st.multiselect('HOW DO YOU HANDLE WASTE?',['Food','Paper','Plastic','Glass','Tin cans'])
    submit = st.form_submit_button('Result!')
    if submit:
        switch_page('RESULTS')
