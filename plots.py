""" This create visualize data page"""

# Import necessary module
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_app(df):
    #st.set_option("deprecation.showpyplt",False)

    st.title("Visualize Data")

    st.header('Scatterplot')

    feature_list = st.multiselect("Select x-axis",('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))


    for feature in feature_list:
        fig =plt.figure(figsize=(12,5))
        st.subheader(f'Scatter plot between {feature} and price')
        sns.scatterplot(x='price',y=feature,data=df)
        st.pyplot(fig)
   
    #create a section for visualization Selecter
    st.header('Visuization')


    # create a multiset

    plot_type = st.multiselect('select charts or plots',('Histogram','Box Plot','Correlation Heatmap'))


    if("Histogram" in plot_type):
        st.subheader("Histogram")
        hist_columns = st.selectbox("Selection the columns to create",('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
        fig = plt.figure(figsize = (12,5))
        plt.title(f"Histogram for {hist_columns}")
        plt.hist(x=df[hist_columns],bins = 'sturges',edgecolor='black')
        st.pyplot(fig)

    if("Box plot" in plot_type):
        st.subheader("Box plot")
        box_column = st.selectbox("Select the column to create its boxplot",('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
        fig = plt.figure(figsize=(12,2))
        plt.title(f"Box plot for {box_column}")
        sns.boxplot(df[box_column])
        st.pyplot(fig)

    #create plot for corrreleation heatmap

    if ('Correlation Heatmap' in plot_type):
        st.subheader('Correlation Heatmap')
        fig = plt.figure(figsize=(12,10))
        ax = sns.heatmap(df.corr(),annot=True)
        bottom,top = ax.get_ylim()
        ax.set_ylim(bottom+0.5,top-0.5)
        st.pyplot(fig)
    



  