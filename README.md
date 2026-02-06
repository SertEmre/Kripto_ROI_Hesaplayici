# Kripto Yatırım Analiz Paneli 

Bu proje, terminal tabanlı basit hesaplamalardan; canlı verilerle çalışan, interaktif ve modern bir web uygulamasına dönüştürülmüştür. Python ve Streamlit kullanılarak geliştirilmiştir.

## Özellikler

- **Canlı Veri Takibi:** Yahoo Finance API üzerinden anlık kripto fiyatları.
- **ROI Hesaplama:** Yatırımın anlık değerini ve net kar/zarar oranını hesaplar.
- **Görselleştirme:** Son 1 yıllık fiyat değişimini interaktif grafiklerle sunar.
- **Modern Arayüz:** Terminal yerine kullanıcı dostu Web UI.

## Kullanılan Teknolojiler

- **Python 3.x**
- **Streamlit** (Web Arayüzü için)
- **yfinance** (Finansal Veriler için)
- **Pandas** (Veri Analizi için)

## Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için terminale şu komutları girin:

```bash
# Gerekli kütüphaneleri yükleyin
pip install streamlit yfinance pandas

# Uygulamayı başlatın
python -m streamlit run app.py