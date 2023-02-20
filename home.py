"""This modle creates the home app"""""

# Import necessary modules

import streamlit as st

def home_app():
    st.title("Car prediction app")
    st.image("./welcome.jpg")
    st.text(
        """
        This web app allows a user t0 predict the price of a car based on engine size,horse power,dimensions ahd the drive wheel tyoe parameters.
        """
    )
