import streamlit as st


st.set_page_config(page_title="Yatırım Pro", layout="wide", initial_sidebar_state="collapsed")

if 'kullanici' not in st.session_state:
    st.session_state['kullanici'] = None

login_page = st.Page("views/login.py", title="Giriş Yap")
ekle_page = st.Page("views/Ekle.py", title="Ekle")
portfoy_page = st.Page("views/Portfoyum.py", title="Portföyüm")

if st.session_state['kullanici'] is None:
    pg = st.navigation([login_page])
else:
    pg = st.navigation([ekle_page, portfoy_page])

pg.run()