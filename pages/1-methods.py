import streamlit as st

st.header("🧪 Methodology")  # anchor removido
    
st.markdown("<br> ", unsafe_allow_html=True)
    
st.markdown('<div class="legend"> Methodology flowchart according to the systematic review process using the PRISMA protocol.\
                Four main stages are displayed: (1) Identification, (2) Screening, (3) Eligibility, and (4) Inclusion.\
                In stages 2 and 3, the review process is on the right, and the exclusion criteria are on the left side. :',
                unsafe_allow_html=True)  
        
st.markdown("<br><br>", unsafe_allow_html=True)
        
st.image("images/methods.png")