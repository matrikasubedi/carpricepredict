import streamlit as st

def data_app(df):
    st.title('View data')

    #create expander to show dataset data
    with st.expander('View data'):
        st.table(df)
    
    #create a section to show infor about dataset
    st.header('Columns Summary')

    #Show the description of dataset
    if st.checkbox('show summary'):
        st.table(df.describe())

    #create a row with three columns to show infor about columns
    beta_col1,beta_col2,beta_cols3 = st.columns(3)

    #Add checkbox to show the columns name
    with beta_col1:
        if st.checkbox('show columns name'):
            st.table(df.columns)

    #Add checkbox to show the columns datatype
    with beta_col2:
        if st.checkbox('View columns datatype'):
            dtype_df = df.dtypes.apply(lambda x:x.name)
            st.table(dtype_df)
    
    #Add checkbox to show the columns data
    with beta_cols3:
        if st.checkbox('view column data'):
            column_data = st.selectbox('select column',tuple(df.columns))
            st.write(df[column_data])