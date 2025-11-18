# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 11:25:00 2025

@author: User
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Flash Droughts in Brazil",
    layout="wide",
     )

st.markdown("""
    <style>
    /* 1. COR DE FUNDO DO CONTAINER (de "container": {"background-color": "#382626"}) */
    [data-testid="stSidebar"] {
        background-color: #382626;
    }
    
    /* 2. TÍTULO/Menu-Title (de "menu-title": {...}) */
    /* Este seletor afeta o título do aplicativo que aparece na sidebar */
    [data-testid="stSidebarNav"] > div:first-child h1 {
        font-size: 22px;
        font-family: 'Arial, sans-serif';
        color: white;
        font-weight: bold;
        text-align: center;
        padding: 20px 0; /* Adicionar padding para espaçamento */
    }

    /* 3. LINKS DE NAVEGAÇÃO ("nav-link" e "icon") */
    /* Este seletor afeta todos os itens de navegação (os nomes das páginas) */
    .st-emotion-cache-1ae80r8 div a {
        font-size: 15px; /* Tamanho da fonte dos links */
        color: white; /* Cor do texto e ícones */
        margin: 0px; 
        padding: 10px 20px; /* Padding dos links */
    }
    
    /* 4. LINK SELECIONADO ("nav-link-selected") */
    /* Este seletor é crucial: ele identifica o link de página ativo */
    .st-emotion-cache-1ae80r8 div a[aria-current="page"] {
        background-color: white !important; /* Fundo branco forçado */
        color: black !important; /* Texto preto forçado */
    }
    
    /* Para replicar o 'icon' se ele for texto */
    /* O Streamlit nativo usa emojis no nome do arquivo (e.g., 🧪 01_Method.py)
       para os ícones, o tamanho é geralmente controlado pelo tamanho do link. */
    </style>
""", unsafe_allow_html=True)


# Estilo CSS personalizado
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            color: #382626;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 20px;
            font-weight: 400;
            text-align: left;
            margin-bottom: 5px;
        }
        .authors {
            font-size: 20px;
            text-align: center;
            color: #382626;
        }
        .keypoints {
            font-size: 18px;
            margin-top: 20px;
            margin-left: 30px;
        }
        .legend {
        font-size: 16px;
        margin-top: 20px;
        text-align: center;
        margin-left: 30px;
        }
        
    </style>
""", unsafe_allow_html=True)



st.markdown(
    '<div class="title">Uncovering Flash Droughts in Brazil through Global and Regional Perspectives: A Systematic Literature Review </div>', unsafe_allow_html=True)
    
st.markdown('<div class="authors"> P. C. M. Vasconcelos<sup>a</sup>,\
            L. C. D. Marote<sup>a</sup>, \
            G. A. J. Bimbatti<sup>a</sup>,\
            G. C. Gesualdo<sup>b</sup>, \
            N. Vergopolan<sup>c</sup>, \
            E. Wendland<sup>d</sup>, \
            P. T. S. Oliveira<sup>e</sup>, A. Mishra<sup>f</sup> &  M. C. Lucas<sup>a</sup> </div>', unsafe_allow_html=True)
                
                
    
    #AFILIAÇÕES
    
st.markdown("<br><br> ", unsafe_allow_html=True)
    
st.markdown('<div class="subtitle">a: School of Technology at Universidade Estadual de Campinas, Limeira, Brazil</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">b: Department of Meteorology and Atmospheric Science, Pennsylvania State University, Pennsylvania, United States</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">c: Department of Earth, Environmental and Planetary Sciences Department, Rice University, Houston, United States </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">d: School of Engineering, Universidade de São Paulo, São Carlos, Brazil</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">e: School of Engineering, Universidade Federal de Mato Grosso do Sul, Campo Grande, Brazil</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">f: Zachry Department of Civil and Environmental Engineering; Texas A&M University, College Station, United States</div>', unsafe_allow_html=True)  
    
st.markdown("<br> ", unsafe_allow_html=True)
    
    
st.markdown('<div class="subtitle"><b>Corresponding author:</b> Priscila Vasconcelos (priscila.costa91@hotmail.com)</div>', unsafe_allow_html=True)
    
    
    #KEYPOINTS
st.markdown('<h4 style="margin-top:40px;">🔑 Key Points:</h4>', unsafe_allow_html=True)
    
st.markdown("""
    <div class="keypoints">
    • Recognized by a sudden reduction in soil moisture at the beginning of a drought event, flash droughts challenge food, energy, and water security.<br>
    • Lack of a clear definition limits comparisons, early warning efforts, and the ability to create policies for flash droughts.<br>
    • Recent projected climate change indicates growing vulnerability in Brazil, reinforcing its status as a global hotspot and underscoring the need for region-specific flash droughts detection criteria.
    </div>
    """, unsafe_allow_html=True)
    

    
    
    #FIGURE 1
st.markdown('<div class="legend"> Comparison between slow-onset (a) and flash (b) droughts highlighting their key characteristics.\
                On the y-axis, SM is soil moisture, P is precipitation, and ET is evapotranspiration.', unsafe_allow_html=True) 
    
st.image("images/Sudden decline in soil moisture in a few days.png")
        
    



