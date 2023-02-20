import streamlit as st

import home
import data
import plots
import predict
import about

from prepro import load_data
#configure the webpage
st.set_page_config(
    page_title = 'Car Price Prediction',
    page_icon = 'car',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

# create a dict for pages

pages_dict = {
    "Home":home,
    "View Data":data,
    "Visualize Data":plots,
    "Predict":predict,
    "About Me":about
}

#Load the dataset

df = load_data()
#create navbar

st.sidebar.title("Navigation")
user_choice = st.sidebar.radio('Go to',('Home','View Data','Visualize Data','Predict','About Me'))


if user_choice == 'Home':
    selected_page = pages_dict[user_choice]
    selected_page.home_app()
if user_choice == 'View Data':
    selected_page = pages_dict[user_choice]
    selected_page.data_app(df)
if user_choice == 'Visualize Data':
    selected_page = pages_dict[user_choice]
    selected_page.plot_app(df)
if user_choice == 'Predict':
    selected_page = pages_dict[user_choice]
    selected_page.model_app(df)
if user_choice == 'About Me':
    selected_page = pages_dict[user_choice]
    selected_page.about_app()

