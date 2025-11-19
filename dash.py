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
    

st.markdown(
    """ <div style="text-align:center; font-size:18px; line-height:1.6; margin-top:15px;
    "> <b> <a href="https://orcid.org/0000-0003-1438-7712" target="_blank">P. C. M. Vasconcelos</a><sup>a</sup>,
    <a href="https://orcid.org/0009-0008-8018-5960" target="_blank">L. C. D. Marote</a><sup>a</sup>,
    <a href="ORCID_LINK_AQUI" target="_blank">G. A. J. Bimbatti</a><sup>a</sup>,
    <a href="https://scholar.google.com/citations?user=n9sYorwAAAAJ&hl=pt-BR" target="_blank">G. C. Gesualdo</a><sup>b</sup>,
    <a href="https://orcid.org/0000-0002-7298-0509" target="_blank">N. Vergopolan</a><sup>c</sup>,
    <a href="http://orcid.org/0000-0003-3374-608X" target="_blank">E. Wendland</a><sup>d</sup>,
    <a href="https://orcid.org/0000-0003-2806-0083" target="_blank">P. T. S. Oliveira</a><sup>e</sup>,
    <a href="https://scholar.google.com/citations?user=Xq6iWHUAAAAJ&hl" target="_blank">A. Mishra</a><sup>f</sup>
    & <a href="https://orcid.org/0000-0002-1732-0241" target="_blank">M. C. Lucas</a><sup>a</sup> </b> </div> """, unsafe_allow_html=True )
                
    
    #AFILIAÇÕES
    
st.markdown("<br><br> ", unsafe_allow_html=True)
    
st.markdown("""
<div style="text-align:center; margin-top:20px;">

    <!-- a -->
    <div class="subtitle" style="margin-bottom:10px;">
        <sup>a</sup>
        <a href="https://www.ft.unicamp.br/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/pt/thumb/b/b2/UNICAMP_logo.svg/966px-UNICAMP_logo.svg.png" 
                 style="height:45px; vertical-align:middle; margin-left:6px;">
        </a>
    </div>

    <!-- b -->
    <div class="subtitle" style="margin-bottom:10px;">
        <sup>b</sup>
        <a href="https://www.met.psu.edu/" target="_blank">
            <img src="https://brand.psu.edu/images/backgrounds/veritcal-1-mark_registered.png" 
                 style="height:45px; vertical-align:middle; margin-left:6px;">
        </a>
    </div>

    <!-- c -->
    <div class="subtitle" style="margin-bottom:10px;">
        <sup>c</sup>
        <a href="LINK_RICE_AQUI" target="_blank">
            <img src="CAMINHO_LOGO_RICE_AQUI" 
                 style="height:45px; vertical-align:middle; margin-left:6px;">
        </a>
    </div>

    <!-- d -->
    <div class="subtitle" style="margin-bottom:10px;">
        <sup>d</sup>
        <a href="LINK_USP_AQUI" target="_blank">
            <img src="CAMINHO_LOGO_USP_AQUI" 
                 style="height:45px; vertical-align:middle; margin-left:6px;">
        </a>
    </div>

    <!-- e -->
    <div class="subtitle" style="margin-bottom:10px;">
        <sup>e</sup>
        <a href="LINK_UFMS_AQUI" target="_blank">
            <img src="CAMINHO_LOGO_UFMS_AQUI" 
                 style="height:45px; vertical-align:middle; margin-left:6px;">
        </a>
    </div>

    <!-- f -->
    <div class="subtitle" style="margin-bottom:10px;">
        <sup>f</sup>
        <a href="LINK_TAMU_AQUI" target="_blank">
            <img src="CAMINHO_LOGO_TAMU_AQUI" 
                 style="height:45px; vertical-align:middle; margin-left:6px;">
        </a>
    </div>

</div>
""", unsafe_allow_html=True)

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
        
    











