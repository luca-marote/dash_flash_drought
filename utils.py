import streamlit as st
import geopandas as gpd

@st.cache_data
def load_geodata():
    return gpd.read_file('gdf_drought_analysis_2.gpkg')