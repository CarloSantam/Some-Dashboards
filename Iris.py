# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 07:54:24 2025

@author: admin
"""

import plotly.express as px
import streamlit as st

# Carica il dataset iris
df = px.data.iris()
st.set_page_config(layout='wide')

st.title("Iris Dashboard")


col1,col2=st.columns(2,gap='small',vertical_alignment='top')

species_list=col1.selectbox(label='Continents', options=list(df['species'].unique())+['ALL'],index=0,placeholder='Select a continent',
                                  label_visibility='collapsed')

check_b=col2.checkbox(label='Show_histogram',key='checkb')

if species_list=='ALL':
    
   # species_list = list(df['species'].unique())
   df_filtred=df
else:
    df_filtred=df.loc[df['species']==((species_list))]


num_variables=list(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

col1,col2,col3,col4=st.columns(4)

k=0

columns = [col1, col2, col3, col4]


for var in num_variables:
        
    df[var+'mean']=df_filtred[var].mean().round(1)
    
    columns[k].metric(label=var+' mean', value=df[var+'mean'].unique())
    
    k+=1

color_map={'setosa':'gray',
           'versicolor':'gray',
           'virginica':'gray'
    }

if (species_list=='ALL'):
    
    
    color_map={'setosa':'blue',
           'versicolor':'green',
           'virginica':'red'
    }
    
    fig=px.scatter(data_frame=df,
                    color_discrete_map=color_map,
                    x='sepal_length',
                    y='petal_width',
                    color='species',
                    size='petal_length',
                    title=f'Sepal Length vs Petal width for {species_list}')

    
elif species_list=='setosa':
    color_map[species_list]='blue'
        
    fig=px.scatter(data_frame=df,
                    color_discrete_map=color_map,
                    x='sepal_length',
                    y='petal_width',
                    color='species',
                    size='petal_length',
                    title=f'Sepal Length vs Petal width for {species_list}')


elif species_list=='virginica':
    color_map[species_list]='red'
        
    fig=px.scatter(data_frame=df,
                    color_discrete_map=color_map,
                    x='sepal_length',
                    y='petal_width',
                    color='species',
                    size='petal_length',
                    title=f'Sepal Length vs Petal width for {species_list}')


elif species_list=='versicolor':
    color_map[species_list]='green'
        
    fig=px.scatter(data_frame=df,
                    color_discrete_map=color_map,
                    x='sepal_length',
                    y='petal_width',
                    color='species',
                    size='petal_length',
                    title=f'Sepal Length vs Petal width for {species_list}')

    

st.plotly_chart(fig)


col1,col2,col3,col4=st.columns(4)

columns = [col1, col2, col3, col4]

k=0

if check_b==True:
    for var in num_variables:
          fig=px.histogram(df_filtred,nbins=30,
                    color_discrete_map=color_map,
                    x=var,
                    title=f'{var} histogram',color='species')

          columns[k].plotly_chart(fig)
          
          fig=px.violin(df_filtred,
                        color_discrete_map=color_map,
                    y=var,
                    title=f'{var} violin',box=True, color='species')

          columns[k].plotly_chart(fig)
          k+=1

# b=1
# import os
# if b==1: os.system('streamlit run Iris.py')

# b==2
