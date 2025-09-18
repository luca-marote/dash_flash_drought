# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 11:25:00 2025

@author: User
"""

import streamlit as st
import streamlit.components.v1 as components
import folium

#%%

st.title("Flash Drought - Review Dashboard")

st.subheader("Mapa com todas")
components.iframe(r"C:\Users\User\arquivos_dashboard\index.html", height=500)

st.subheader("Mapa com as variáveis")
components.iframe(r"C:\Users\User\arquivos_dashboard\mapa_variaveis_fd.html", height=500)

