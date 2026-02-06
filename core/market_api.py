import yfinance as yf
import streamlit as st

@st.cache_data(ttl=60) # 60 saniyede bir veriyi önbelleğe alır (Hız için)
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