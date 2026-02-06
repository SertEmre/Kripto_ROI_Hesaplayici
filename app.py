import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Yatırım Analiz Paneli", layout="wide")

st.sidebar.header(" Yatırım Ayarları")

secilen_kripto = st.sidebar.selectbox(
    "Hangi Kriptoyu Analiz Edeceğiz?", 
    ["BTC-USD", "ETH-USD", "AVAX-USD", "SOL-USD", "DOGE-USD", "XRP-USD"]
)

yatirim_miktari = st.sidebar.number_input("Yatırım Miktarı ($)", min_value=10, value=1000)
alis_fiyati = st.sidebar.number_input("Satın Aldığın Fiyat ($)", min_value=0.1, value=40000.0)

st.title(" Kripto ROI ve Analiz Paneli")
st.markdown("Bu panel, **gerçek zamanlı** verilerle yatırımını analiz eder.")
st.markdown("---")

with st.spinner('Canlı veriler çekiliyor...'):
    ticker = yf.Ticker(secilen_kripto)
    try:
        hist = ticker.history(period="1d")
        guncel_fiyat = hist['Close'].iloc[-1]
    except:
        st.error("Veri çekilemedi. İnternet bağlantını kontrol et.")
        guncel_fiyat = 0

if guncel_fiyat > 0:
    adet = yatirim_miktari / alis_fiyati
    guncel_deger = adet * guncel_fiyat
    kar_zarar = guncel_deger - yatirim_miktari
    roi_yuzdesi = ((guncel_fiyat - alis_fiyati) / alis_fiyati) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Anlık Fiyat", value=f"${guncel_fiyat:,.2f}")

    with col2:
        st.metric(label="Toplam Portföy Değeri", value=f"${guncel_deger:,.2f}")

    with col3:
        st.metric(label="Net Kar/Zarar", value=f"${kar_zarar:,.2f}", delta=f"%{roi_yuzdesi:.2f}")

    st.markdown(f"### {secilen_kripto} - Son 1 Yıllık Performans")
    
    grafik_verisi = ticker.history(period="1y")
    st.line_chart(grafik_verisi['Close'])

    if st.checkbox("Detaylı Fiyat Tablosunu Göster"):
        st.write(grafik_verisi)

else:
    st.warning("Veri bekleniyor...")