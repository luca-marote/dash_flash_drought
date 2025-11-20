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

hsj_logo = 'images/default_cover.jpg'
st.sidebar.image(hsj_logo, use_column_width=True)

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
            font-size: 32px;
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

IMG_SIZE = 70       
INDEX_SIZE = 16     

st.markdown("""
<div style="text-align:center; margin-top:20px; display:flex; justify-content:center; gap:22px; align-items:center; flex-wrap:wrap;">

  <div style="text-align:center;">
    <div style="font-size:20px;"><sup>a</sup></div>
    <a href="https://www.ft.unicamp.br/" target="_blank" rel="noopener noreferrer">
      <img src="https://upload.wikimedia.org/wikipedia/pt/thumb/b/b2/UNICAMP_logo.svg/966px-UNICAMP_logo.svg.png" style="height:100px; display:block; margin:4px auto;">
    </a>
  </div>

  <div style="text-align:center;">
    <div style="font-size:20px;"><sup>b</sup></div>
    <a href="https://www.met.psu.edu/" target="_blank" rel="noopener noreferrer">
      <img src="https://brand.psu.edu/images/backgrounds/veritcal-1-mark_registered.png" style="height:100px; display:block; margin:4px auto;">
    </a>
  </div>

  <div style="text-align:center;">
    <div style="font-size:20px;"><sup>c</sup></div>
    <a href="https://eeps.rice.edu/" target="_blank" rel="noopener noreferrer">
      <img src="https://logos-world.net/wp-content/uploads/2023/08/Rice-University-Symbol.png" style="height:100px; display:block; margin:4px auto;">
    </a>
  </div>

  <div style="text-align:center;">
    <div style="font-size:20px;"><sup>d</sup></div>
    <a href="https://eesc.usp.br/" target="_blank" rel="noopener noreferrer">
      <img src="https://scs.usp.br/identidadevisual/wp-content/uploads/2022/08/usp-logo-png-1.png" style="height:100px; display:block; margin:4px auto;">
    </a>
  </div>

  <div style="text-align:center;">
    <div style="font-size:20px;"><sup>e</sup></div>
    <a href="https://www.ufms.br/" target="_blank" rel="noopener noreferrer">
      <img src="https://www.fundect.ms.gov.br/wp-content/uploads/2019/06/ufms_logo_positivo_assinatura_vertical_rgb.png" style="height:100px; display:block; margin:4px auto;">
    </a>
  </div>

  <div style="text-align:center;">
    <div style="font-size:20px;"><sup>f</sup></div>
    <a href="https://engineering.tamu.edu/civil/index.html" target="_blank" rel="noopener noreferrer">
      <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/Texas_A%26M_University_seal.svg/1200px-Texas_A%26M_University_seal.svg.png" style="height:100px; display:block; margin:4px auto;">
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
        
    





















