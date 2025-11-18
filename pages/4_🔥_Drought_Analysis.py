import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from streamlit_folium import st_folium
import folium
import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon

st.header("🌡️ Drought Analysis")  # anchor removido
    
tab1, tab2 = st.tabs(["Brazil", "Global"])
     
with tab2:

    @st.cache_data
    def load_geodata():
        return gpd.read_file('gdf_drought_analysis_2.gpkg')
    gdf = load_geodata()
        
    st.header("🌵 Interactive map of drought distribution")

    # --- Filtros ---
    anos = st.multiselect("Select year:", sorted(gdf['Ano de publicação'].unique()))
    escalas = st.multiselect("Select scale:", sorted(gdf['Escala de abrangência'].unique()))
        
    # --- Aplicar filtros ---
    gdf_filtrado = gdf.copy()
    if anos:
        gdf_filtrado = gdf_filtrado[gdf_filtrado['Ano de publicação'].isin(anos)]
    if escalas:
        gdf_filtrado = gdf_filtrado[gdf_filtrado['Escala de abrangência'].isin(escalas)]

    # --- Criar mapa dinâmico ---
    m = folium.Map(location=[-14, -52], zoom_start=4, tiles='cartodb positron')

    color_map = {
    "FDs": "orange",
    "ADs": "green",
    "EDs": "red",
    "Others": "purple",
    }


    for _, row in gdf_filtrado.iterrows():

        geom = row.geometry

        popup_html = f"""
        <b>Study:</b> {row.get('Class', '—')}<br>
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
                    icon="flame"
                )
            ).add_to(m)

    # -------------------------
    # Se for polígono → GeoJson
    # -------------------------
        elif isinstance(geom, (Polygon, MultiPolygon)):
            folium.GeoJson(
                data=geom,
                style_function=lambda x: {
                    "fillColor": "#ff7800",
                    "color": "#ff7800",
                    "weight": 1,
                    "fillOpacity": 0.25,
                    },
                tooltip=popup_html
            ).add_to(m)

    # --- Exibir mapa no dashboard ---
    st_folium(m, width=1200, height=600)
