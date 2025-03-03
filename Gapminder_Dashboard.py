# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:05:19 2025

@author: admin
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import sys

sys.tracebacklimit = 0  # Disabilita la traceback

df=pd.read_csv("data\gapminder_data_graphs.csv")

try:
    st.set_page_config(layout='wide')
    st.title('Gapminder Dashboard Creation')

    st.sidebar.subheader('Continents')
    
    continents=st.sidebar.multiselect(label='Continents', options=list(df['continent'].unique())+['ALL'],default='ALL',placeholder='Select a continent',
                                      label_visibility='collapsed')
    
    if (not continents):
        
       raise ValueError("⚠️ Please, choose a continents")
       
    if 'ALL' in continents:
        
       continents = list(df['continent'].unique())
      
    st.sidebar.subheader('Country')
    
    country=st.sidebar.multiselect(label='Country', options=list(df.loc[df['continent'].isin(continents),'country'].unique())+['ALL'],default='ALL',placeholder='Select a country',
                                   label_visibility='collapsed')
    
    anno=df['year'].unique()
    
    if (not country):
        
       raise ValueError("⚠️ Please, choose a country")
       
    if 'ALL' in country:
        
       country = list(df.loc[df['continent'].isin(continents),'country'])

    year_selection=st.slider(label='Year selection',min_value=min(anno),max_value=max(anno),value=min(anno))
    
    st.write('Selected year: {}'.format(year_selection))
    
    df_filtred=df.loc[(df['year']==year_selection) & (df['continent'].isin(continents)) & (df['country'].isin(country))]
    
    mean_gdp=df_filtred['gdp'].mean().round(1)
    
    mean_life_exp=df_filtred['life_exp'].mean().round(1)
    
    mean_hdi=df_filtred['hdi_index'].mean().round(1)
    
    mean_services=df_filtred['services'].mean().round(1)
    
    mean_co2=df_filtred['co2_consump'].mean().round(1)
    
    col1,col2,col3=st.columns(3,gap='small',vertical_alignment='top')
    
    col1.metric(label='Average GDP',value=mean_gdp)
    
    col2.metric(label='Average Life Experience',value=mean_life_exp)
    
    col3.metric(label='Average HDI',value=mean_hdi)
    
    col4,middle,col5=st.columns(3,gap='small',vertical_alignment='top')
    
    col4.metric(label='Average Services',value=mean_services)
    
    col5.metric(label='Average CO2',value=mean_co2)
    
    feature_list=['hdi_index', 'co2_consump',
           'gdp', 'services','life_exp']
    
    col1,col2 = st.columns(2,gap='large',vertical_alignment='top') 
        
    
    with col1:
        
        selected_variable_x = st.selectbox(
        label='Selected Features on x axis',
        options=feature_list,
        index=2)
        

    with col2:
        
        selected_variable_y = st.selectbox(
        label='Selected Features on y axis',
        options=feature_list,
        index=4)
    
    left, middle, right = st.columns((2, 5, 2))

    with middle:       
        fig = px.scatter(df_filtred, x=selected_variable_x, y=selected_variable_y, color='continent', 
              title=f'Plot {selected_variable_x}. vs {selected_variable_y} in {year_selection}',hover_name='country')
    
        fig.update_layout(
        width=900,  
        height=600
        )
    
        st.plotly_chart(fig)




    
    selected_variable = st.selectbox(
    label='Selected Features',
    options=feature_list,
    index=0)
    
    left, middle, right = st.columns((2, 5, 2))
    with middle:
        fig = px.choropleth(df_filtred,
             locations="country",  # Colonna contenente i nomi dei paesi
             color=selected_variable,   # Colonna per colorare i paesi per continente
             locationmode ='country names',# Grandezza dei punti in base all'aspettativa di vita
             hover_name="country",  # Nome del paese nei tooltip
               # Dimensione massima dei punti
                   center={"lat": 0, "lon": 0},
             title=f"Map {selected_variable} in {year_selection}",
             # projection="natural earth",  # Proiezione della mappa
             template="plotly", 
             color_continuous_scale='Viridis', # Tema del grafico
             width=900,  
             height=600                     
             )
        st.plotly_chart(fig)
        
        fig=px.violin(df_filtred,
                  color='continent',
                  title=f"Violin plot {selected_variable} in {year_selection}",
                  y=selected_variable,
                  x='continent',
                  points='outliers',
                  box=True)
    
        st.plotly_chart(fig)

        
        
except Exception as e:
       raise ValueError(f"⚠️ Unexpected error: {e}")

