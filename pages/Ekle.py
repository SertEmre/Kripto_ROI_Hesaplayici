import streamlit as st
import datetime
from core.data_manager import veri_ekle

st.set_page_config(page_title="Yatırım Ekle", page_icon="➕")

st.header("➕ Yeni Yatırım Ekle")

with st.form("ekle_formu"):
    col1, col2 = st.columns(2)
    with col1:
        sembol = st.selectbox("Kripto Para", ["BTC-USD", "ETH-USD", "SOL-USD", "AVAX-USD", "XRP-USD", "DOGE-USD"])
        tarih = st.date_input("Alım Tarihi", datetime.date.today())
    
    with col2:
        miktar = st.number_input("Adet", min_value=0.00001, format="%.5f")
        maliyet = st.number_input("Birim Maliyet ($)", min_value=0.0, format="%.2f")
    
    submit = st.form_submit_button("Portföye Kaydet")

    if submit:
        if miktar > 0:
            veri_ekle(sembol, miktar, maliyet, tarih)
            st.success(f"{miktar} adet {sembol} başarıyla eklendi!")
        else:
            st.warning("Lütfen miktarı giriniz.")