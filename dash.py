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
    """
    <div style="text-align:center; font-size:18px; line-height:1.7; margin-top:15px;">
        <b>

        <!-- P. C. M. Vasconcelos -->
        P. C. M. Vasconcelos<sup>a</sup>
        <a href="https://orcid.org/0000-0003-1438-7712" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>,

        <!-- L. C. D. Marote -->
        L. C. D. Marote<sup>a</sup>
        <a href="https://orcid.org/0009-0008-8018-5960" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>,

        <!-- G. A. J. Bimbatti -->
        G. A. J. Bimbatti<sup>a</sup>
        <a href="ORCID_LINK_AQUI" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px; opacity:0.4;">
        </a>,

        <!-- G. C. Gesualdo -->
        G. C. Gesualdo<sup>b</sup>
        <a href="https://scholar.google.com/citations?user=n9sYorwAAAAJ&hl=pt-BR" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>,

        <!-- N. Vergopolan -->
        N. Vergopolan<sup>c</sup>
        <a href="https://orcid.org/0000-0002-7298-0509" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>,

        <!-- E. Wendland -->
        E. Wendland<sup>d</sup>
        <a href="http://orcid.org/0000-0003-3374-608X" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>,

        <!-- P. T. S. Oliveira -->
        P. T. S. Oliveira<sup>e</sup>
        <a href="https://orcid.org/0000-0003-2806-0083" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>,

        <!-- A. Mishra -->
        A. Mishra<sup>f</sup>
        <a href="https://scholar.google.com/citations?user=Xq6iWHUAAAAJ&hl" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>

        &

        <!-- M. C. Lucas -->
        M. C. Lucas<sup>a</sup>
        <a href="https://orcid.org/0000-0002-1732-0241" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" 
                 style="width:16px; vertical-align:middle; margin-left:4px;">
        </a>

        </b>
    </div>
    """,
    unsafe_allow_html=True
)

                
                
    
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
        
    








