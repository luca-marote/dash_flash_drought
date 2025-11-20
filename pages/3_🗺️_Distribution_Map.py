import streamlit as st
import streamlit.components.v1 as components

hsj_logo = 'https://www.tandfonline.com/cms/asset/3e7614cf-7643-4a3d-9bad-f444bd55e5c7/thsj20.v070.i14.cover.jpg'
t_f_logo = 'https://www.informascope.com/views/default/_images/_logos/urunler/taylor_and_francis.png'

st.sidebar.image(hsj_logo, use_column_width=True)
st.sidebar.image(t_f_logo, use_column_width=True)

link_url = "https://review-fd-map.netlify.app/"

st.header("Distribution of peer-reviewed studies")
    
st.markdown(f"**Acesse o mapa diretamente:** [{link_url}]({link_url})") 
    
iframe_html = f'''
    <iframe 
        src="{link_url}" 
        width="100%" 
        height="700" 
        style="border:none;"
        allowfullscreen="true">
    </iframe>'''
        
st.markdown(iframe_html, unsafe_allow_html=True)
