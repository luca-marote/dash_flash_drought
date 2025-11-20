import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from streamlit_folium import st_folium
import folium
from folium.elements import Element
import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon
from folium.plugins import MarkerCluster
import plotly.graph_objects as go
import plotly.express as px

st.header("🌡️ Drought Analysis")  # anchor removido
    
tab1, tab2 = st.tabs(["Geographic Distribution", "Indicators/Variables"])
     
with tab1:

    @st.cache_data
    def load_geodata():
        return gpd.read_file('gdf_drought_analysis_2.gpkg')
    gdf = load_geodata()
        
    st.header("🌵 Interactive map of drought distribution")

    # --- Filtros ---
    ano_min = int(gdf['Ano de publicação'].min())
    ano_max = int(gdf['Ano de publicação'].max())
    anos = st.slider(
        "Select year range:",
        min_value=ano_min,
        max_value=ano_max,
        value=(ano_min, ano_max)  # valores iniciais
        )
    
    opcoes_escalas = ['All'] + sorted(gdf['Escala de abrangência'].unique()) 

    escalas = st.selectbox(
        "Select scale:",
        options=opcoes_escalas, # Usa a nova lista com 'All'
        index=0 # Garante que 'All' (o índice 0) seja o valor inicial
        )
        
    gdf_filtrado = gdf[
    (gdf['Ano de publicação'] >= anos[0]) & 
    (gdf['Ano de publicação'] <= anos[1])
        ]

    
    escalas = st.selectbox(
        "Select scale:",
        options=sorted(gdf['Escala de abrangência'].unique())
        )

    # 2. Modifica a lógica de filtragem para ignorar o filtro se 'All' for selecionado.
    if escalas != 'All': 
        gdf_filtrado = gdf_filtrado[gdf_filtrado['Escala de abrangência'] == escalas]
    

    # --- Criar mapa dinâmico ---
    m = folium.Map(location=[-14, -52], zoom_start=4, tiles='cartodb positron')

    color_map = {
        "FDs": "orange",
        "ADs": "green",
        "EDs": "red",
        "Others": "purple",
        }

    # Caso apareça um tipo que não esteja no dicionário → usa cinza
    def get_color(class_name):
        return color_map.get(class_name, "gray")
        
    marker_cluster = MarkerCluster().add_to(m)
    
    for _, row in gdf_filtrado.iterrows():
        
        geom = row.geometry

        popup_html = f"""
        <b>Scale:</b> {row.get('Escala de abrangência', '—')}<br>
        <b>Year:</b> {row.get('Ano de publicação', '—')}
        """

        # -------------------------
        # Se for ponto → Marker
        # -------------------------
        if isinstance(geom, Point):
            folium.Marker(
                location=[geom.y, geom.x],
                popup=popup_html,
                icon=folium.Icon(
                    color=get_color(row.get("Class")),
                    icon="fire"
                )
            ).add_to((marker_cluster))

        # -------------------------
        # Se for polígono → GeoJson
        # -------------------------
        elif isinstance(geom, (Polygon, MultiPolygon)):
            geojson_dict = {
                "type": "Feature",
                "geometry": geom.__geo_interface__,
                "properties": {"Class": row.get("Class")}
                }

            folium.GeoJson(
            data=geojson_dict,
            style_function=lambda feature: {
                "fillColor": get_color(feature["properties"]["Class"]),
                "color": get_color(feature["properties"]["Class"]),
                "weight": 1,
                "fillOpacity": 0.25,
            },
            tooltip=popup_html
        ).add_to(m)

        legend_html = """
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 180px; height: auto; 
                    border: 2px solid gray; z-index:9999; font-size:14px;
                    background-color: white; opacity: 0.95; padding: 10px;">
            <p style="font-weight: bold; margin-bottom: 5px;">Drought Categories</p>
        """

        display_names = {
            "FDs": "Flash Drought",
            "ADs": "Agricultural Drought",
            "EDs": "Extreme Drought",
            "Others": "Others",
            }

        for class_name, color in color_map.items():
            name = display_names.get(class_name, class_name)
            legend_html += f"""
                <div style="margin-bottom: 5px;">
                    <i style="background: {color}; 
                              width: 15px; height: 15px; 
                              display: inline-block; 
                              margin-right: 5px; 
                              border: 1px solid #333;"></i> 
                    {name}
                </div>
            """

        legend_html += "</div>"

# Injeta o HTML no objeto do mapa Folium (m)
        m.get_root().html.add_child(Element(legend_html))
    # --- Exibir mapa no dashboard ---
        st_folium(m, width=1200, height=600)



PADRAO_LAYOUT = dict(
    showlegend=False,
    # Remova width, e use apenas a altura desejada
    height=500,  # ⬅️ Reduza a altura se 1000px for muito alto para a coluna
    margin=dict(t=40, b=40, l=40, r=40),
    uniformtext_minsize=12, 
    uniformtext_mode='hide'
)

# 2. Configuração padrão de legenda (baseada em fig_a)
PADRAO_LEGENDA = dict(
    title_text="Indicators",
    orientation="v",
    x=0.3, 
    y=0.25,
    bordercolor="white",
    borderwidth=2,
    font=dict(
        family="Source Sans",
        size=18,
        color="DarkSlateGrey"
    )
)

valores_a = [66, 41, 36, 25, 15, 3]
cores   = ['#1f77b4', '#8c564b', '#ff7f0e', '#2ca02c', '#969696', '#756bb1']

rotulos = ['Vegetation and Productivity Index', 'Vegetation Stress Indicators',
            'Indicators based on Soil Moisture', 'Indicators based on Precipitation and Evapotranspiration',
            'Hydrological', 'Others']

fig_a = go.Figure(data=[
    go.Pie(
        values=valores_a,
        labels=rotulos,
        marker=dict(colors=cores),
        direction='counterclockwise',
        sort=False,
        hovertemplate="Number of papers: %{value}<extra></extra>", 
        textinfo='percent',  
        insidetextorientation='horizontal',
        textfont=dict(
            family="Source Sans", 
            size=22,                    
            color="black"        
        )
    )
])
    
fig_a.update_layout(**PADRAO_LAYOUT)


valores_b = [46, 40, 20, 19, 9, 0]

fig_b = go.Figure(data=[
    go.Pie(
        values=valores_b,
        labels=rotulos,
        marker=dict(colors=cores),
        direction='counterclockwise',
        sort=False,
        hovertemplate="Number of papers: %{value}<extra></extra>", 
        textinfo='percent',      
        insidetextorientation='horizontal',
        textfont=dict(
            family="Source Sans", 
            size=22,                    
            color="black"              
        )
    )
])

fig_b.update_layout(**PADRAO_LAYOUT)

valores_c = [23, 8, 15, 11, 3, 0]

fig_c = go.Figure(data=[
    go.Pie(
        values=valores_c,
        labels=rotulos,
        marker=dict(colors=cores),
        direction='counterclockwise',
        sort=False,
        hovertemplate="Number of papers: %{value}<extra></extra>", 
        textinfo='percent',        
        insidetextorientation='horizontal',
        textfont=dict(
            family="Source Sans", 
            size=22,                     
            color="black"                
        )
    )
])

fig_c.update_layout(**PADRAO_LAYOUT)

valores_d = [4, 3, 2, 0, 0, 0]

fig_d = go.Figure(data=[
    go.Pie(
        values=valores_d,
        labels=rotulos,
        marker=dict(colors=cores),
        direction='counterclockwise',
        sort=False,
        hovertemplate="Number of papers: %{value}<extra></extra>", # Mostra rótulo, % e valor
        textinfo='percent',        # Informação visível no slice
        insidetextorientation='horizontal',
        textfont=dict(
            family="Source Sans", # Nome da fonte e fallback
            size=22,                     # Tamanho da fonte
            color="black"                # Cor da fonte
        )
    )
])

fig_d.update_layout(**PADRAO_LAYOUT)

master_legend_figure = go.Figure(data=[
    go.Pie(
        values=valores_a, 
        labels=rotulos,
        marker=dict(colors=cores),
        hovertemplate="<extra></extra>",
        domain={'x': [0, 0.0001], 'y': [0, 0.0001]}
    )
])

master_legend_figure.update_layout(
    showlegend=True, 
    legend=PADRAO_LEGENDA,
    height=200,      
    margin=dict(t=0, b=0, l=0, r=0),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.markdown("""
    <style>
        .title {
            font-size: 28px;
            font-weight: 700;
            text-align: center;
            color: #1a1a1a;
            margin-bottom: 20px;
        <style>
        """, unsafe_allow_html=True)


with tab2:
    options = ['Global dataset', 'Brazilian subset']

    select_option = st.selectbox("Select option:", options=options, index=0)
    
    col1, col2 = st.columns(2)
    
    with col1:
        

        st.markdown('<div class="title">Drought and Flash Drought Indicators </div>', unsafe_allow_html=True)
       
        if select_option=='Global dataset':
            st.plotly_chart(fig_a, use_container_width=True)
                 
        elif select_option=='Brazilian subset':
            st.plotly_chart(fig_c, use_container_width=True)


    with col2:

        st.markdown('<div class="title">Flash Drought Indicators </div>', unsafe_allow_html=True)

        if select_option=='Global dataset':
            st.plotly_chart(fig_b, use_container_width=True)

        elif select_option=='Brazilian subset':
            st.plotly_chart(fig_d, use_container_width=True)


    st.plotly_chart(master_legend_figure, use_container_width=True)
