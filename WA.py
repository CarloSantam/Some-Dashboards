
import streamlit as st
import plotly.express as px
import streamlit as st

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.sidebar.subheader('Continents')

st.title("Visual App")

# add an uploader file
uploaded_file = st.sidebar.file_uploader("Upload your csv or xlsx file", type=["csv","xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    
    
    except Exception:
        df = pd.read_xlsx(uploaded_file)
    
        # Show your Data Frame
        
    numeric_columns = df.select_dtypes(include=['int','float']).columns
    
    non_numeric_columns = df.select_dtypes(include=['object']).columns
    
    uploaded_file = st.sidebar.checkbox(label="Would you like to see uploaded dataframe")

    if uploaded_file==True:
        st.write(df)
    
    st.sidebar.write("---")

    
    plots_selection = st.sidebar.selectbox(label="Select your favourite plot",
                                           options=['Histogram','Scatter','Line',
                                                    'Violin'])
    
    st.sidebar.write("---")
    color = st.sidebar.checkbox(label="Would you like to see color?")
    
    
    if color==True:
        
        color_c = st.sidebar.selectbox(label="Would you like to see color?",
                                       options=non_numeric_columns)
    else:
        color_c=None

    st.sidebar.write("---")

    if (plots_selection!='Histogram') and  (plots_selection!='Violin'):

        variable_x=st.sidebar.selectbox(label="Select your variable on x-axis",
                                           options=numeric_columns)
        variable_y=st.sidebar.selectbox(label="Select your variable on y-axis",
                                         options=numeric_columns,key='y')    
        if plots_selection=='Scatter':
            
            fig=px.scatter(df,x=variable_x,y=variable_y,color=color_c)
            
            st.plotly_chart(fig)
        
        
        elif plots_selection=='Line':
            
            fig=px.line(df,x=variable_x,y=variable_y,color=color_c)
            
            st.plotly_chart(fig)

    elif plots_selection=='Violin':
        
        variable_x=st.sidebar.selectbox(label="Select your variable on x-axis",
                                           options=non_numeric_columns)
        variable_y=st.sidebar.selectbox(label="Select your variable on y-axis",
                                         options=numeric_columns,key='y')    
        
        fig=px.violin(df,x=variable_x,y=variable_y,color=color_c)
        
        st.plotly_chart(fig)
        
    elif plots_selection=='Histogram':     
        
        variable=st.sidebar.selectbox(label="Select your variable on y-axis",
                                         options=numeric_columns,key='y')    
        
        bins=st.sidebar.slider(label='Bins',min_value=10,max_value=len(df),value=10)
        
        fig=px.histogram(df,x=variable,color=color_c,nbins=bins)
        
        st.plotly_chart(fig)
    
