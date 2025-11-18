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
        /* Aumenta o tamanho da fonte para todos os links de navegação (que incluem os ícones/emojis) */
        /* Seletores usados pelo Streamlit para os links de navegação na sidebar nativa */
        .st-emotion-cache-1ae80r8 div a {
            font-size: 20px; /* Altere este valor para o tamanho desejado (ex: 20px, 24px) */
            color: white; /* Mantém o texto/ícone branco, supondo um fundo escuro */
            padding: 10px 20px;
        }

        /* Seletor específico para o texto do link na sidebar (dependente da versão do Streamlit) */
        [data-testid="stSidebarNavItems"] li a {
            font-size: 20px;
        }
        
        /* Aumenta o tamanho da fonte da página selecionada (ativa) */
        .st-emotion-cache-1ae80r8 div a[aria-current="page"] {
            font-size: 20px; /* Garante que a página ativa também tenha o mesmo tamanho */
            /* Se você quiser o fundo branco para a página ativa, adicione: */
            /* background-color: white !important; */
            /* color: black !important; */
        }
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
        
    




