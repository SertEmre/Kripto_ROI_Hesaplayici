import pandas as pd
import os

DATA_FILE = "data/portfoy.csv"

def verileri_yukle():
    """CSV dosyasını okur. Dosya yoksa veya BOŞSA boş DataFrame döndürür."""
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        try:
            return pd.read_csv(DATA_FILE)
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=["Sembol", "Miktar", "Maliyet", "Tarih"])
    else:
        return pd.DataFrame(columns=["Sembol", "Miktar", "Maliyet", "Tarih"])

def veri_ekle(sembol, miktar, maliyet, tarih):
    """Yeni bir yatırımı kaydeder."""
    df = verileri_yukle()
    yeni_veri = pd.DataFrame({
        "Sembol": [sembol],
        "Miktar": [miktar],
        "Maliyet": [maliyet],
        "Tarih": [tarih]
    })
    if not df.empty:
        df = pd.concat([df, yeni_veri], ignore_index=True)
    else:
        df = yeni_veri
        
    df.to_csv(DATA_FILE, index=False)
    return True

def verileri_sifirla():
    """Tüm portföyü siler."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        return True
    return False