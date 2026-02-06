import streamlit as st
import pandas as pd
from core.data_manager import verileri_yukle, verileri_sifirla
from core.market_api import anlik_fiyatlari_getir

st.set_page_config(page_title="Portföy Analizi", page_icon="📈", layout="wide")

st.title("📊 Portföy Durumu")

df = verileri_yukle()

if not df.empty:
    with st.spinner('Piyasa verileri güncelleniyor...'):
        unique_semboller = df['Sembol'].unique().tolist()
        guncel_fiyatlar = anlik_fiyatlari_getir(unique_semboller)

    df['Guncel_Birim_Fiyat'] = df['Sembol'].map(guncel_fiyatlar)
    df['Toplam_Deger'] = df['Miktar'] * df['Guncel_Birim_Fiyat']
    df['Maliyet_Tutari'] = df['Miktar'] * df['Maliyet']
    df['Kar_Zarar'] = df['Toplam_Deger'] - df['Maliyet_Tutari']
    df['ROI_Yuzde'] = (df['Kar_Zarar'] / df['Maliyet_Tutari']) * 100

    toplam_portfoy = df['Toplam_Deger'].sum()
    toplam_maliyet = df['Maliyet_Tutari'].sum()
    toplam_kar = toplam_portfoy - toplam_maliyet
    genel_roi = (toplam_kar / toplam_maliyet) * 100 if toplam_maliyet > 0 else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Toplam Varlık", f"${toplam_portfoy:,.2f}")
    c2.metric("Toplam Maliyet", f"${toplam_maliyet:,.2f}")
    c3.metric("Net Kar/Zarar", f"${toplam_kar:,.2f}", delta_color="normal")
    c4.metric("Genel ROI", f"%{genel_roi:.2f}", delta=f"{genel_roi:.2f}%")

    st.divider()

    st.subheader("Varlık Bazlı Detaylar")
    st.dataframe(df.style.format({
        "Guncel_Birim_Fiyat": "${:.2f}",
        "Toplam_Deger": "${:.2f}",
        "Maliyet_Tutari": "${:.2f}",
        "Kar_Zarar": "${:.2f}",
        "ROI_Yuzde": "%{:.2f}"
    }), use_container_width=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.subheader(" Varlık Dağılımı")
        st.bar_chart(df, x="Sembol", y="Toplam_Deger")
    
    with col_g2:
        st.subheader(" Kar/Zarar Durumu")
        st.bar_chart(df, x="Sembol", y="Kar_Zarar")

    with st.expander("Portföyü Sıfırla"):
        if st.button("Tüm Portföyü Sıfırla (Sil)"):
            verileri_sifirla()
            st.rerun()

else:
    st.info("Henüz portföyünde kayıtlı varlık yok. Soldaki menüden 'Ekle' sayfasına git.")