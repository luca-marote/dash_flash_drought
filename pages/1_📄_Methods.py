import streamlit as st

hsj_logo = 'https://www.tandfonline.com/cms/asset/3e7614cf-7643-4a3d-9bad-f444bd55e5c7/thsj20.v070.i14.cover.jpg'
t_f_logo = 'https://www.informascope.com/views/default/_images/_logos/urunler/taylor_and_francis.png'


st.sidebar.image(t_f_logo, use_column_width=True)
st.sidebar.image(hsj_logo, use_column_width=True)

st.header("🧪 Methodology")  # anchor removido
    
st.markdown("<br> ", unsafe_allow_html=True)
    
st.markdown('<div class="legend"> Methodology flowchart according to the systematic review process using the PRISMA protocol.\
                Four main stages are displayed: (1) Identification, (2) Screening, (3) Eligibility, and (4) Inclusion.\
                In stages 2 and 3, the review process is on the right, and the exclusion criteria are on the left side. :',
                unsafe_allow_html=True)  
        
st.markdown("<br><br>", unsafe_allow_html=True)
        
st.image("images/methods.png")
