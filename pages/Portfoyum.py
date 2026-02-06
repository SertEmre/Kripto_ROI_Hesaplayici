import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from core.data_manager import verileri_yukle, verileri_sifirla
from core.market_api import anlik_fiyatlari_getir, gecmis_verileri_getir

st.set_page_config(page_title="Portföy Analizi", page_icon="📈", layout="wide")

st.title("📊 Profesyonel Portföy Analizi")

df = verileri_yukle()

if not df.empty:
    with st.spinner('Piyasa verileri işleniyor...'):
        unique_semboller = df['Sembol'].unique().tolist()
        guncel_fiyatlar = anlik_fiyatlari_getir(unique_semboller)

    df['Guncel_Birim_Fiyat'] = df['Sembol'].map(guncel_fiyatlar)
    df['Toplam_Deger'] = df['Miktar'] * df['Guncel_Birim_Fiyat']
    df['Maliyet_Tutari'] = df['Miktar'] * df['Maliyet']
    df['Kar_Zarar'] = df['Toplam_Deger'] - df['Maliyet_Tutari']
    
    df['ROI_Yuzde'] = df.apply(lambda x: (x['Kar_Zarar'] / x['Maliyet_Tutari'] * 100) if x['Maliyet_Tutari'] > 0 else 0, axis=1)

    toplam_portfoy = df['Toplam_Deger'].sum()
    toplam_maliyet = df['Maliyet_Tutari'].sum()
    toplam_kar = toplam_portfoy - toplam_maliyet
    genel_roi = (toplam_kar / toplam_maliyet) * 100 if toplam_maliyet > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Toplam Varlık", f"${toplam_portfoy:,.2f}", help="Cüzdanındaki toplam para")
    col2.metric("Toplam Maliyet", f"${toplam_maliyet:,.2f}", help="Cebinden çıkan para")
    col3.metric("Net Kar/Zarar", f"${toplam_kar:,.2f}", delta_color="normal")
    col4.metric("Genel ROI", f"%{genel_roi:.2f}", delta=f"{genel_roi:.2f}%")

    st.markdown("---")

    c1, c2 = st.columns([2, 1]) 

    with c1:
        st.subheader("📈 Varlık Bazlı Kâr/Zarar Durumu")
        fig_bar = px.bar(
            df, 
            x="Sembol", 
            y="Kar_Zarar",
            color="Kar_Zarar",
            color_continuous_scale=["red", "green"], # Zarar kırmızı, kar yeşil
            title="Hangi Coinden Ne Kadar Kâr/Zarardasın?",
            text_auto='.2s'
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        st.subheader(" Portföy Dağılımı")
        # Plotly Pie Chart (Pasta Grafik)
        fig_pie = px.pie(
            df, 
            values="Toplam_Deger", 
            names="Sembol", 
            title="Cüzdanın Hangi Coinlerden Oluşuyor?",
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    st.subheader(" Detaylı Teknik Analiz")
    
    secilen_coin_analiz = st.selectbox("Grafiğini incelemek istediğin coini seç:", unique_semboller)
    
    if secilen_coin_analiz:
        zaman_araligi = st.select_slider("Zaman Aralığı:", options=["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], value="1y")
        
        with st.spinner(f"{secilen_coin_analiz} verileri getiriliyor..."):
            tarihsel_veri = gecmis_verileri_getir(secilen_coin_analiz, zaman_araligi)
        
        if tarihsel_veri is not None and not tarihsel_veri.empty:
            fig_candle = go.Figure(data=[go.Candlestick(
                x=tarihsel_veri.index,
                open=tarihsel_veri['Open'],
                high=tarihsel_veri['High'],
                low=tarihsel_veri['Low'],
                close=tarihsel_veri['Close'],
                name=secilen_coin_analiz
            )])
            
            fig_candle.update_layout(
                title=f"{secilen_coin_analiz} Fiyat Grafiği ({zaman_araligi})",
                yaxis_title="Fiyat ($)",
                xaxis_rangeslider_visible=False,
                template="plotly_dark"
            )
            
            st.plotly_chart(fig_candle, use_container_width=True)

    with st.expander("📄 İşlem Geçmişi"):
        st.dataframe(df.style.format({
            "Guncel_Birim_Fiyat": "${:.2f}",
            "Toplam_Deger": "${:.2f}",
            "Maliyet_Tutari": "${:.2f}",
            "Kar_Zarar": "${:.2f}",
            "ROI_Yuzde": "%{:.2f}"
        }), use_container_width=True)
        
        if st.button("Tüm Portföyü Sıfırla (Dikkat!)"):
            verileri_sifirla()
            st.rerun()

else:
    st.info("⚠️ Henüz portföyünde coin yok. Sol menüden 'Ekle' sayfasına gidip ilk yatırımını ekle!")