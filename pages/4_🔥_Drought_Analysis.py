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


st.header("🌡️ Drought Analysis")  # anchor removido
    
tab1, tab2 = st.tabs(["Brazil", "Global"])
     
with tab2:

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
    escalas = st.selectbox(
        "Select scale:",
        options=sorted(gdf['Escala de abrangência'].unique())
    )
        
    gdf_filtrado = gdf[
    (gdf['Ano de publicação'] >= anos[0]) & 
    (gdf['Ano de publicação'] <= anos[1])
    ]

    if escalas:
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
        <p style="font-weight: bold; margin-bottom: 5px;">Tipos de Seca</p>
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

# Adiciona linha para a cor padrão ("gray")
    legend_html += f"""
        <div style="margin-bottom: 5px;">
            <i style="background: gray; 
                      width: 15px; height: 15px; 
                      display: inline-block; 
                      margin-right: 5px; 
                      border: 1px solid #333;"></i> 
            Não Classificado
        </div>
    """

    legend_html += "</div>"

# Injeta o HTML no objeto do mapa Folium (m)
    m.get_root().html.add_child(Element(legend_html))
    # --- Exibir mapa no dashboard ---
    st_folium(m, width=1200, height=600)
