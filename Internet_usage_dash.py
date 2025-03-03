# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:46:53 2025

@author: admin
"""

import streamlit as st

import plotly.express as px

import pandas as pd


df=pd.read_csv("data/share-of-individuals-using-the-internet.csv")

df_filtred=df.loc[(df['Year']>=2000) & (df['Year']<=2016) ]

country=list(df_filtred['Country'].unique())

years=list(df_filtred['Year'].unique())

years.sort()

st.set_page_config(layout='wide')

st.header('Internet Usage Dashboard')

select_year=st.selectbox(
    label='Year',index=0,options=years)

st.sidebar.subheader('Country Level Detail'
    )

form = st.sidebar.form(key='my_form')
country_box = form.selectbox(label='Country', options=list(df['Country'].unique()))
submit_button = form.form_submit_button('Submit')

# select_year=st.selectbox(label='Year',options=years)

col1,col2=st.columns([4,2])

fig = px.choropleth(df_filtred,
      locations="Country",  # Colonna contenente i nomi dei paesi
      color='Individuals using the Internet (% of population)',   # Colonna per colorare i paesi per continente
      locationmode ='country names',# Grandezza dei punti in base all'aspettativa di vita
      hover_name="Country",  # Nome del paese nei tooltip
        # Dimensione massima dei punti
      center={"lat": 0, "lon": 0},
             color_continuous_scale=px.colors.qualitative.Vivid, # Tema del grafico

      title=f"Visual showing internet usage percentage in {select_year}",
      # projection="natural earth",  # Proiezione della mappa
      template="plotly"
      )

col1.plotly_chart(fig)

fig=px.histogram(data_frame=df_filtred,nbins=30,
          x='Individuals using the Internet (% of population)',
          title=f'Individuals using the Internet usage distribution in {select_year}')

col2.plotly_chart(fig)

if submit_button==True:
    st.header(f"Internet usage in {country_box}")
    
    fig=px.line(df.loc[df['Country']==country_box],
                x='Year',
                y='Individuals using the Internet (% of population)',
                title=f'Individuals using the Internet (% of population) in {country_box}'
                )
    
    st.plotly_chart(fig)