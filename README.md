# Gelişmiş Kripto Yatırım Analiz Platformu v1.2

Bu platform, basit bir ROI hesaplayıcısından öte, canlı piyasa verileriyle çalışan, modüler mimariye sahip ve interaktif grafiklerle donatılmış profesyonel bir finansal takip aracıdır.

---

##  Öne Çıkan Özellikler

- **Profesyonel Görselleştirme:** Plotly motoru ile interaktif Mum (Candlestick), Pasta (Varlık Dağılımı) ve Kar/Zarar bar grafikleri.
- **Canlı Veri Entegrasyonu:** `yfinance` API aracılığıyla 7/24 güncel kripto para fiyatları.
- **Modüler Mimari:** Temiz kod prensiplerine uygun (Core/Pages/Data) klasör yapısı ile sürdürülebilir geliştirme.
- **Veritabanı Yönetimi:** Yatırımların `CSV` formatında kalıcı olarak saklanması ve otomatik veri bütünlüğü kontrolü.
- **Teknik Analiz:** Seçilen varlıklar için geçmişe dönük (1 aylıktan 5 yıla kadar) detaylı fiyat analizi.

---

## Proje Yapısı

Proje, yönetilebilirliği artırmak adına modüler bir yapıda kurgulanmıştır:

- `core/`: Veri yönetimi (`data_manager.py`) ve API entegrasyonu (`market_api.py`) gibi ana mantık işlemleri.
- `pages/`: Uygulamanın farklı ekranları (Portföy Analizi ve Yatırım Ekleme).
- `data/`: Kullanıcı portföy verilerinin saklandığı güvenli alan.
- `app.py`: Uygulamanın ana giriş noktası ve karşılama ekranı.

---

## Kurulum ve Kullanım

### 1. Gereksinimler
Sisteminizde Python 3.8+ yüklü olmalıdır. Gerekli kütüphaneleri aşağıdaki komutla yükleyebilirsiniz:

```bash
pip install streamlit yfinance pandas plotly