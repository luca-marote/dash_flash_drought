# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 11:25:00 2025

@author: User
"""

import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


#%%


st.set_page_config(
    page_title="Flash Droughts in Brazil",
    layout="wide",
    initial_sidebar_state="expanded"
)


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


# Estilo CSS personalizado
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            color: #f5a253;
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
            color: #08a2fc;
        }
        .keypoints {
            font-size: 18px;
            margin-top: 20px;
            margin-left: 30px;
        }
        .legend {
        font-size: 22px;
        margin-top: 20px;
        text-align: center;
        margin-left: 30px;
        }
        
        /* Sidebar: aumentar fontes e tamanho de emojis */
        [data-testid="stSidebar"] .css-1d391kg { 
            font-size: 22px;  /* tamanho dos itens do menu */
        }
        [data-testid="stSidebar"] .css-1d391kg span {
            font-size: 28px;  /* tamanho dos emojis */
        }
        
    </style>
""", unsafe_allow_html=True)


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


# Sidebar com menu
pagina = st.sidebar.radio("📂 Browse:", ["📘 Cover",
                                        "🧪 Method",
                                        "📈 Publication Trends",
                                        "🌡️ Drought Analysis",
                                        "🧠 Scientific Gaps",
                                        "📊 Thematic trends"])



#--------------------------------------------------------------------------------------------------------------------
# Página de Capa
#--------------------------------------------------------------------------------------------------------------------


if pagina == "📘 Cover":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="title">Uncovering Flash Droughts in Brazil through Global and Regional Perspectives: A Systematic Literature Review </div>', unsafe_allow_html=True)
    
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
    
    st.markdown("<br><br> ", unsafe_allow_html=True)
    
    
    #FIGURE 1
    st.markdown('<div class="legend"> Comparison between slow-onset (a) and flash (b) droughts highlighting their key characteristics.\
                On the y-axis, SM is soil moisture, P is precipitation, and ET is evapotranspiration.', unsafe_allow_html=True) 
    
    st.image("images/Sudden decline in soil moisture in a few days.png")
        
    
    
#--------------------------------------------------------------------------------------------------------------------
# Página de Método
#--------------------------------------------------------------------------------------------------------------------


elif pagina == "🧪 Method":
    st.header("🧪 Methodology")  # anchor removido
    
    st.markdown("<br> ", unsafe_allow_html=True)
    
    st.markdown('<div class="legend"> Methodology flowchart according to the systematic review process using the PRISMA protocol.\
                Four main stages are displayed: (1) Identification, (2) Screening, (3) Eligibility, and (4) Inclusion.\
                In stages 2 and 3, the review process is on the right, and the exclusion criteria are on the left side. :',
                unsafe_allow_html=True)  
        
    st.markdown("<br><br>", unsafe_allow_html=True)
        
    st.image("images/methods.png")


#--------------------------------------------------------------------------------------------------------------------
# Tendências de Publicação
#--------------------------------------------------------------------------------------------------------------------


elif pagina == "📈 Publication Trends":
    st.header("📈 Publication Trends")  # anchor removido
    # Criar abas
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Papers per Year", "📚 Journals/Authors", "🌎 Countries", "🧩 Study Area Scales", "🗺️ Interactive distribution of studies" ])

#--------------------------------------------------------------------------------------------------------------------


    with tab1:
        st.subheader("Interactive — Publications overview")
    # -------------------------------
    # Figura 1
    # -------------------------------
    
    # --- Dados principais ---
        anos = list(range(2012, 2025))
        publicacoes_por_ano = [1, 1, 2, 0, 2, 2, 6, 6, 4, 12, 15, 23, 18]
        df = pd.DataFrame({
            'Ano': anos,
            'Artigos_por_ano': publicacoes_por_ano
            })
        df['Total_acumulado'] = df['Artigos_por_ano'].cumsum()

    # --- Controle: range de anos ---
        st.markdown("**Control:** set the year range below")
        ano_min, ano_max = df['Ano'].min(), df['Ano'].max()
        sel_range = st.slider("Year (range)", ano_min, ano_max, (ano_min, ano_max), step=1)
        df_filtered = df[(df['Ano'] >= sel_range[0]) & (df['Ano'] <= sel_range[1])]

    # --- Figura (A): barras + acumulado ---
        fig_a = make_subplots(specs=[[{"secondary_y": True}]])
        fig_a.add_trace(
            go.Bar(
                x=df_filtered['Ano'],
                y=df_filtered['Artigos_por_ano'],
                name='Papers per year',
                marker_color='steelblue',
                hovertemplate='Year: %{x}<br>Papers: %{y}<extra></extra>'
                ),
            secondary_y=False
            )

        fig_a.add_trace(
            go.Scatter(
                x=df_filtered['Ano'],
                y=df_filtered['Total_acumulado'],
                name=f'Cumulative total ({df["Total_acumulado"].iloc[-1]})',
                mode='lines+markers',
                line=dict(color='firebrick', width=3),
                hovertemplate='Year: %{x}<br>Cumulative: %{y}<extra></extra>'
                ),
            secondary_y=True
            )

        fig_a.update_layout(
            title=dict(text="Annual number of articles published per year", font=dict(size=22), x=0.30),
            height=750,
            template="simple_white",
            font=dict(family="Liberation Serif", size=18),
            margin=dict(l=80, r=40, t=80, b=60),
            legend=dict(orientation="v", y=1, x=0.01, font=dict(size=18))
            )
        fig_a.update_xaxes(title="Year", tickmode="linear",title_font=dict(size=22), tickfont=dict(size=18))
        fig_a.update_yaxes(title_text="Absolute number of papers", secondary_y=False, title_font=dict(size=22), tickfont=dict(size=18))
        fig_a.update_yaxes(title_text="Cumulative number of papers", secondary_y=True, title_font=dict(size=22), tickfont=dict(size=18))

        st.plotly_chart(fig_a, use_container_width=True)



    # -------------------------------
    # Figura 2
    # -------------------------------
        anos_str = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", 
             "2019", "2020", "2021", "2022", "2023", "2024"]
        x = np.arange(len(anos_str))

        # Total global de publicações (usado no painel A)
        tot = np.array([1, 1, 2, 0, 2, 2, 6, 6, 4, 12, 15, 23, 18], dtype=float)

        # Séries fornecidas para o Brasil
        br_total = np.minimum(np.array([1,0,0,0,1,2,3,4,0,3,0,4,5], dtype=float), tot)
        br_fd = np.minimum(np.array([0,0,0,0,0,0,0,1,0,0,0,1,3], dtype=float), br_total)

    # -------------------------------
    # CONFIGURAÇÕES DE COR E LARGURA
    # -------------------------------
        COLOR_TOTAL = "steelblue"
        COLOR_BR = "#E69F00"
        COLOR_FD = "#8B0000"
        w = 0.3  # deslocamento entre grupos

    # -------------------------------
    # CRIA FIGURA INTERATIVA
    # -------------------------------
        fig_b = go.Figure()

    # Barras - Total
        fig_b.add_trace(go.Bar(
            x=x - w, y=tot,
            name="Papers per year",
            marker_color=COLOR_TOTAL,
            width=w,
            hovertemplate="Year: %{x}<br>Total papers: %{y}<extra></extra>"
            ))

    # Barras - Brasil
        fig_b.add_trace(go.Bar(
            x=x, y=br_total,
            name="Publications in Brazil (23)",
            marker_color=COLOR_BR,
            width=w,
            hovertemplate="Year: %{x}<br>Brazil papers: %{y}<extra></extra>"
            ))

    # Barras - FD Brasil
        fig_b.add_trace(go.Bar(
            x=x + w, y=br_fd,
            name="Publications of FD in Brazil (5)",
            marker_color=COLOR_FD,
            width=w,
            hovertemplate="Year: %{x}<br>FD Brazil papers: %{y}<extra></extra>"
            ))

    # -------------------------------
    # AJUSTES DE LAYOUT E ESTILO
    # -------------------------------
        fig_b.update_layout(
            height=750,
            barmode='group',
            template="simple_white",
            font=dict(family="Liberation Serif", size=18),
            xaxis=dict(
                tickmode='array',
                tickvals=x,
                ticktext=anos_str,
                tickangle=45,
                title="Year",
                title_font=dict(size=22),
                tickfont=dict(size=18),
                ),
            yaxis=dict(
                title="Absolute number of papers",
                range=[0, 25],
                title_font=dict(size=22),
                tickfont=dict(size=18),
                ),
            legend=dict(
                font=dict(size=20),
                x=0.01, y=1,
                bgcolor="rgba(0,0,0,0)",
                bordercolor="rgba(0,0,0,0)",
                ),
            title=dict(
                text="Publications related to Brazil, highlighting those specifically addressing flash droughts",
                font=dict(size=22),
                x=0.2
                ),
            
            margin=dict(l=80, r=40, t=80, b=60),
            
            
            )


        st.plotly_chart(fig_b, use_container_width=True)

# Para Streamlit:
# st.plotly_chart(fig, use_container_width=True)

#--------------------------------------------------------------------------------------------------------------------

    with tab2:
        st.subheader("Interactive — Journals overview")

        journals = [
                "Journal of Hydrometeorology", "Environmental Research Letters",
                "Geophysical Research Letters", "Atmosphere",
                "Science of the Total Environment", "Water Resources Research",
                "Remote Sensing", "Bulletin of the American Meteorological Society",
                "International Journal of Climatology", "Hydrology and Earth System Sciences"
                ]
        number_of_pub = [9, 7, 4, 4, 4, 3, 3, 3, 3, 3]

        df_journals = pd.DataFrame({
                "Journal": journals,
                "Publications": number_of_pub
                }).sort_values("Publications", ascending=True)

        fig_journals = go.Figure(
                go.Bar(
                    x=df_journals["Publications"],
                    y=df_journals["Journal"],
                    orientation='h',
                    marker_color="#56B4E9",
                    text=df_journals["Publications"],
                    textposition='outside'
                    )
                )

        fig_journals.update_layout(
                title=dict(text="Top journals by number of publications", font=dict(size=22), x=0.35),
                title_font=dict(size=22),
                height=750,
                template="simple_white",
                font=dict(family="Liberation Serif", size=14),
                margin=dict(l=150, r=40, t=80, b=60)
                )
        
        fig_journals.update_xaxes(title="Number of Publications", title_font=dict(size=22), tickfont=dict(size=18))
        fig_journals.update_yaxes(title_text="Journals",title_font=dict(size=22), tickfont=dict(size=20))
        
        st.plotly_chart(fig_journals, use_container_width=True)




    with tab3:
        st.subheader("Interactive — Countries publications overview")

        countries = ["U.S.", "Brazil", "China", "Spain", "India"]
        perc = np.array([36.9, 26.1, 20.0, 3.3, 3.3])

        # Ordenação decrescente + "Others"
        idx = np.argsort(-perc)
        countries_sorted = [countries[i] for i in idx]
        perc_sorted = perc[idx]
        others_perc = 100.0 - perc_sorted.sum()
        countries_sorted.append("Others")
        perc_sorted = np.append(perc_sorted, others_perc)

        cores = {
            "Brazil":"#E69F00", "U.S.":"#56B4E9", "China":"#009E73",
            "Spain":"#F0E442", "India":"#D55E00", "Others":"#9E9E9E"
            }
        bar_colors = [cores[c] for c in countries_sorted]

        fig_b = go.Figure(
           go.Bar(
               x=perc_sorted,
               y=countries_sorted,
               orientation='h',
               marker_color=bar_colors,
               text=[f"{p:.1f}%" for p in perc_sorted],
               textposition=['inside' if p >= 15 else 'outside' for p in perc_sorted],
               hovertemplate='%{y}: %{x:.1f}%<extra></extra>'
               )
           )

        fig_b.update_layout(
            title=dict(text="Countries with the highest number of publications", font=dict(size=22), x=0.35),
            height=750,
            template="simple_white",
            font=dict(family="Liberation Serif", size=18),
            margin=dict(l=100, r=40, t=80, b=60)
            )
        
        fig_b.update_xaxes(title_text="Percentage of articles (%)", title_font=dict(size=22), tickfont=dict(size=18))
        fig_b.update_yaxes(autorange='reversed', title_font=dict(size=22), tickfont=dict(size=18))

        st.plotly_chart(fig_b, use_container_width=True)

   
    
   
    with tab4:
        st.subheader("Interactive — Study area overview")
        
        
        overall = {"Regional": 32.6, "National": 27.2, "Local": 5.4, "Global": 30.4, "Continental": 4.3}
        brazil  = {"Regional": 82.6, "National": 8.7, "Local": 8.7, "Global": 0.0, "Continental": 0.0}
        labels = ["Regional","National","Local","Global","Continental"]
        ov = np.array([overall[k] for k in labels]) 
        br = np.array([brazil[k] for k in labels])
        
        df_br_ov = pd.DataFrame({
            'Overall': overall,
            'Brazil': brazil,
            })
        
        df_long = df_br_ov.reset_index().melt(
            id_vars='index',
            var_name='Fonte',
            value_name='Percentual')
        
        fig_d = go.Figure()
        
        fig_d.add_trace(
            
            go.Bar(
                x=df_long[df_long['Fonte']=='Overall']["Percentual"],
                y=df_long[df_long['Fonte']=='Overall']["index"],
                name="All studies (n = 92)",
                orientation='h',
                marker_color="#B0B0B0",
                text=df_long[df_long["Fonte"]=="Overall"]["Percentual"].round(1).astype(str) + "%",
                textposition='outside'
                )
            )
        
        fig_d.add_trace(
            
            go.Bar(
                x=df_long[df_long['Fonte']=='Brazil']["Percentual"],
                y=df_long[df_long['Fonte']=='Brazil']["index"],
                name="Brazil publications (n = 23)",
                orientation='h',
                marker_color="#E69F00",
                text=df_long[df_long["Fonte"]=="Brazil"]["Percentual"].round(1).astype(str) + "%",
                textposition='outside'
                )
            )

        fig_d.update_layout(
                title=dict(text="Spatial extent of the study area", font=dict(size=22), x=0.35),
                title_font=dict(size=22),
                barmode='group',
                height=750,
                template="simple_white",
                font=dict(family="Liberation Serif", size=14),
                legend=dict(orientation="v", y=1, x=0.7, font=dict(size=18)),
                margin=dict(l=100, r=40, t=80, b=60)
                )
        
        fig_d.update_xaxes(title="Spatial extent of publications (%)", title_font=dict(size=22), tickfont=dict(size=18))
        fig_d.update_yaxes(title_text="Scale",title_font=dict(size=22), tickfont=dict(size=20))
        
        st.plotly_chart(fig_d, use_container_width=True)
        
        
    with tab5:
        link_url = "https://review-fd-map.netlify.app/"
        st.markdown(f"**Acesse o mapa diretamente:** [{link_url}]({link_url})") 
        st.subheader("Distribution of peer-reviewed studies (Mapa Interativo)")
        iframe_html = f'''
        <iframe 
            src="{link_url}" 
            width="100%" 
            height="700" 
            style="border:none;"
            allowfullscreen="true">
        </iframe>'''
        
        st.markdown(iframe_html, unsafe_allow_html=True)



# Flash Drought Analysis
elif pagina == "🌡️ Drought Analysis":
    st.header("🌡️ Drought Analysis")  # anchor removido
    
    tab1, tab2 = st.tabs(["Brazil", "Geographical distribution and typologies of drought events in Brazil"])

    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Geographical distribution events in Brazil")
            st.image("images/FD_Brazil.png")
                        
        

    




