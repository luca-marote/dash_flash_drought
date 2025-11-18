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