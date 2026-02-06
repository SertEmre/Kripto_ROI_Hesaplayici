import yfinance as yf
import streamlit as st

@st.cache_data(ttl=60)
def anlik_fiyatlari_getir(sembol_listesi):
    """Listelenen coinlerin anlık fiyatını sözlük olarak döner."""
    if not sembol_listesi:
        return {}
    
    fiyatlar = {}
    sembol_str = " ".join(sembol_listesi)
    
    try:
        tickers = yf.Tickers(sembol_str)
        for sembol in sembol_listesi:
            try:
                data = tickers.tickers[sembol].history(period="1d")
                if not data.empty:
                    fiyatlar[sembol] = data['Close'].iloc[-1]
                else:
                    fiyatlar[sembol] = 0
            except:
                fiyatlar[sembol] = 0
    except Exception as e:
        st.error(f"API Hatası: {e}")
    
    return fiyatlar

@st.cache_data(ttl=3600) 
def gecmis_verileri_getir(sembol, periyot="1y"):
    """Seçilen coinin geçmiş OHLC (Open, High, Low, Close) verilerini getirir."""
    try:
        ticker = yf.Ticker(sembol)
        history = ticker.history(period=periyot)
        return history
    except Exception as e:
        st.error(f"Geçmiş veri hatası: {e}")
        return None