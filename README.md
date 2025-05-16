Kripto ROI Hesaplayıcı

Bu Python programı, kripto para yatırımlarınızın kazanç ve ROI oranlarını hesaplamanızı sağlar.  
Geçmiş yatırımlarınızı CSV dosyasında saklar, yeni yatırımlar eklemenize izin verir ve genel yatırım özetinizi gösterir.

Özellikler
- Kullanıcıdan yatırım verilerini güvenli şekilde alır (sadece sayısal değer kabul eder).
- Geçmiş yatırımları dosyadan okuyup yükler.
- Yeni yatırımlar eklenebilir ve kaydedilir.
- Toplam yatırım, toplam kazanç ve genel ROI hesaplar.
- Verileri `yatirim_ozeti.csv` dosyasına kaydeder.

Sorun Çözümleri
Rebase ile Commit Temizliği yaptım
- Problemi: Yinelenen commit'ler (808b761 ve f8cfe0d)
- Çözüm: `git rebase -i` ile interaktif düzenlemede bulundum ve sonuç olarak daha temiz bir commint geçmişi görünümü kazandırdım.
