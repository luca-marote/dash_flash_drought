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


# Tema customizado
theme = {
    "primaryColor": "#0B3954",           # cor principal (botões, seletores)
    "backgroundColor": "#FFFFFF",        # fundo branco da página
    "secondaryBackgroundColor": "#F0F2F6", # fundo de widgets / sidebar
    "textColor": "#000000",              # texto preto
    "font": "sans serif"
}

st.set_page_config(
    page_title="Flash Droughts in Brazil",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplica o tema
st.set_theme(theme=theme)

# Estilo CSS personalizado
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            color: #0B3954;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 20px;
            font-weight: 400;
            text-align: center;
            margin-bottom: 5px;
        }
        .authors {
            font-size: 16px;
            text-align: center;
            color: #333;
        }
        .keypoints {
            font-size: 16px;
            margin-top: 20px;
            margin-left: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar com menu
pagina = st.sidebar.radio("📂 Navegue pelo conteúdo:", ["📘 Cover", "🧪 Method", "📈 Publication Trends", "🗺️ Interactive Maps"])

# Página de Capa
if pagina == "📘 Cover":
    st.markdown('<div class="title">Uncovering Flash Droughts in Brazil: A Comprehensive Review</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="authors">Author1, Author2, Author3, Author4</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">1: School of Technology at Universidade Estadual de Campinas, Limeira, São Paulo State, Brazil</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Affiliation author 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Affiliation author 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Affiliation author 4</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subtitle"><b>Corresponding author:</b> Priscila Vasconcelos (priscila.costa91@hotmail.com)</div>', unsafe_allow_html=True)
    
    st.markdown('<h4 style="margin-top:40px;">🔑 Key Points:</h4>', unsafe_allow_html=True)
    st.markdown("""
    <div class="keypoints">
    • Recognized by a sudden reduction in soil moisture at the beginning of a drought event, flash droughts challenge food, energy, and water security.<br>
    • Lack of a clear definition limits comparisons, early warning efforts, and the ability to create policies for flash droughts.<br>
    • Recent projected climate change indicates growing vulnerability in Brazil, reinforcing its status as a global hotspot and underscoring the need for region-specific flash droughts detection criteria.
    </div>
    """, unsafe_allow_html=True)

# Página de Método
elif pagina == "🧪 Method":
    st.header("🧪 Methodology")  # anchor removido
    col1, col2 = st.columns(2)
    with col1:
        st.image(r"C:\Users\User\arquivos_dashboard\methods.png", caption="Flowchart of the methodology according to PRISMA protocol.")

# Tendências de Publicação
elif pagina == "📈 Publication Trends":
    st.header("📈 Publication Trends")  # anchor removido
    # Criar abas
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Papers per Year", "📚 Journals", "🌎 Countries", "🧠 Authors", "🧩 Study Area Scales"])

    with tab1:
        st.subheader("Interactive — Publications overview")

    # --- seus dados (copiados do script matplotlib que você mostrou) ---
        anos = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
        publicacoes_por_ano = [1, 1, 2, 0, 2, 2, 6, 6, 4, 12, 15, 23, 18]
        anos_str = list(map(str, anos))
        df = pd.DataFrame({'Ano': anos_str, 'Artigos_por_ano': publicacoes_por_ano})
        df['Total_acumulado'] = df['Artigos_por_ano'].cumsum()
        
    # convertendo ano para número para rangeslider funcionar
        df['Ano_num'] = [int(a) for a in anos]

        countries = ["U.S.", "Brazil", "China", "Spain", "India"]
        perc = np.array([36.9, 26.1, 20.0, 3.3, 3.3])

    # Ordena por % decrescente e adiciona "Others" (igual ao seu código)
        idx = np.argsort(-perc)
        countries_sorted = [countries[i] for i in idx]
        perc_sorted = perc[idx]
        others_perc = max(0.0, 100.0 - float(perc_sorted.sum()))
        countries_sorted = countries_sorted + ["Others"]
        perc_sorted = np.concatenate([perc_sorted, [others_perc]])

        cores = {
        "Brazil":"#E69F00", "U.S.":"#56B4E9", "China":"#009E73",
        "Spain":"#F0E442", "India":"#D55E00", "Others":"#9E9E9E"
        }
        bar_colors = [cores.get(c, "#9E9E9E") for c in countries_sorted]

    # --- controles simples dentro da aba (opcional) ---
        st.markdown("**Controles:** ajuste o intervalo de anos abaixo")
        ano_min, ano_max = int(df['Ano_num'].min()), int(df['Ano_num'].max())
        sel_range = st.slider("Ano (range)", ano_min, ano_max, (ano_min, ano_max), step=1)

        df_filtered = df[(df['Ano_num'] >= sel_range[0]) & (df['Ano_num'] <= sel_range[1])]

    # --- construir figura Plotly com 2 subplots (A: barras + acumulado, B: barras horizontais) ---
        fig_a = make_subplots(
            rows=1, cols=1,
            specs=[[{"secondary_y": True}]],
            subplot_titles=["(A) Number of publications per year"])
        
        
        fig_b = make_subplots(
            rows=1, cols=2,
            specs=[[{"secondary_y": True}, {}]],
            column_widths=[0.62, 0.38],
            horizontal_spacing=0.08,
            subplot_titles=["(B) Countries with most publications"])

    # (A) barras (por ano) - usamos Ano_num para eixos numéricos mas exibimos ticktext com strings
        fig_a.add_trace(
            go.Bar(
                x=df_filtered['Ano_num'],
                y=df_filtered['Artigos_por_ano'],
                name='Papers per year',
                marker_color='steelblue',
                hovertemplate='Year: %{x}<br>Papers: %{y}<extra></extra>'
                ),
            row=1, col=1, secondary_y=False
            )

    # (A) linha acumulada (eixo direito)
    # note: se você filtrou anos, recompute o acumulado relativo ao filtro (a seguir calculamos cumulativo do df original e reindexamos)
    # Para manter o mesmo comportamento do seu matplotlib (acumulado global), usamos o cumulativo da série completa recortada:
        df_cum = df.copy()
        df_cum = df_cum[(df_cum['Ano_num'] >= sel_range[0]) & (df_cum['Ano_num'] <= sel_range[1])]
        fig_a.add_trace(
            go.Scatter(
                x=df_cum['Ano_num'],
                y=df_cum['Total_acumulado'],
                name=f'Cumulative total ({df["Total_acumulado"].iloc[-1]})',
                mode='lines+markers',
                line=dict(color='firebrick', width=3),
                hovertemplate='Year: %{x}<br>Cumulative: %{y}<extra></extra>'
                ),
            row=1, col=1, secondary_y=True
            )

    # eixo X: mostrar ticks como strings (anos)
        fig_a.update_xaxes(
            tickmode='array',
            tickvals=df['Ano_num'],
            ticktext=df['Ano'],
            row=1, col=1,
           title_text='Year',
           rangeslider_visible=True
           )

     # ajustar detalhes dos eixos e fontes 
     
        fig_a.update_yaxes(title_text='Absolute number of papers', row=1, col=1)
        fig_a.update_yaxes(title_text='Cumulative number of papers', row=1, col=1, secondary_y=True)
        fig_a.update_layout(
            height=600,   # <<< AQUI você controla a altura
            margin=dict(l=80, r=40, t=80, b=60),
            template="simple_white"
        )
        
        fig_a.update_layout(
            font=dict(size=18),  # afeta legendas e texto em geral
            xaxis=dict(title_font=dict(size=20), tickfont=dict(size=16)),
            yaxis=dict(title_font=dict(size=20), tickfont=dict(size=16))
            )
        
    # (B) barras horizontais de países
        fig_b.add_trace(
            go.Bar(
                x=perc_sorted,
                y=countries_sorted,
                orientation='h',
                name='Percentage',
                marker_color=bar_colors,
                text=[f"{p:.1f}%" for p in perc_sorted],
                textposition=['inside' if p >= 15 else 'outside' for p in perc_sorted],
                hovertemplate='%{y}: %{x:.1f}%<extra></extra>'
                ),
            row=1, col=2
            )

        # Mostrar fig_a
        st.plotly_chart(fig_a, use_container_width=True)



# Mostrar fig_b (corrigido)
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

        fig_b.update_yaxes(title_text='Countries with most publications', autorange='reversed')
        fig_b.update_xaxes(title_text="Percentage (%)")
        fig_b.update_layout(
            height=500,
            margin=dict(l=80, r=40, t=80, b=60),
            template='simple_white',
            font=dict(family='Liberation Serif', size=18)
            )

        fig_b.update_layout(
            font=dict(size=18),  # afeta legendas e texto em geral
            xaxis=dict(title_font=dict(size=20), tickfont=dict(size=16)),
            yaxis=dict(title_font=dict(size=20), tickfont=dict(size=16))
        )
        
        st.plotly_chart(fig_b, use_container_width=True)


    with tab2:        
        col1, col2 = st.columns(2)        
        with col1:
            st.image(r"C:\Users\User\arquivos_dashboard\journals_number_pub.png", caption="Number of journals")
        with col2:
            st.write("Dá pra colcoar textos, figuras ou qualquer outra coisa")

    with tab3:        
        col1, col2 = st.columns(2)        
        with col1:
            st.image(r"C:\Users\User\arquivos_dashboard\percentage_of_published_countries.png", caption="Percentage of published countries")
        with col2:
            st.write("Dá pra colcoar textos, figuras ou qualquer outra coisa")

    with tab4:        
        col1, col2 = st.columns(2)        
        with col1:
            st.image(r"C:\Users\User\arquivos_dashboard\authors_number_pub.png", caption="Number of publications per author")
        with col2:
            st.write("Dá pra colcoar textos, figuras ou qualquer outra coisa neste espaço.")
   
    with tab5:    
        col1, col2 = st.columns(2)    
        with col1:
            st.image(r"C:\Users\User\arquivos_dashboard\study_area_spatial_scale.png", caption="Study area scale")
        with col2:
            st.write("Dá pra colcoar textos, figuras ou qualquer outra coisa neste espaço.")

# Mapas Interativos
elif pagina == "🗺️ Interactive Maps":
    st.header("🗺️ Interactive Maps")  # anchor removido

    with open(r"C:\Users\User\arquivos_dashboard\index.html", "r", encoding="utf-8") as f:
        html_data2 = f.read()
    st.subheader("Distribution of peer-reviewed studies")
    st.components.v1.html(html_data2, height=700, scrolling=True)

    with open(r"C:\Users\User\arquivos_dashboard\mapa_final_seca_.html", "r", encoding="utf-8") as f:
        html_data1 = f.read()
    st.subheader("Geographical distribution and typologies of drought events in Brazil")
    st.components.v1.html(html_data1, height=700, scrolling=True)
