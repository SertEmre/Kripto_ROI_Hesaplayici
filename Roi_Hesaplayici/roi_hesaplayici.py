import pandas as pd
import os 
import matplotlib.pyplot as plt

dosya_ismi = "yatirim_ozeti.csv"

veriler = {
    "Kripto ismi": [],
    "Toplam yatırım": [],
    "Giriş fiyatı": [],
    "Çıkış fiyatı": [],
    "Kazanç": [],
    "ROI ": [],
    "Yatırım tarihi": []
}

def sayi_kontrol(istek_giris):
    while True:
        try:
            return float(input(istek_giris))
        except ValueError:
            print("Lütfen sadece sayı giriniz!")

def veri_al():
    tarih = input("Yatırım tarihinizi giriniz (GG/AA/YYYY): ")
    kripto_ismi = input("Kripto ismi: ")
    yatirim = sayi_kontrol("Toplam yatırımınız ne kadar?: ")
    giris_fiyati = sayi_kontrol("Giriş fiyatınızı giriniz: ")
    cikis_fiyati = sayi_kontrol("Çıkış fiyatınızı giriniz: ")

    kazanc = ((cikis_fiyati - giris_fiyati) / giris_fiyati) * yatirim
    roi = (kazanc / yatirim) * 100

    veriler["Kripto ismi"].append(kripto_ismi)
    veriler["Toplam yatırım"].append(yatirim)
    veriler["Giriş fiyatı"].append(giris_fiyati)
    veriler["Çıkış fiyatı"].append(cikis_fiyati)
    veriler["Kazanç"].append(round(kazanc, 2))
    veriler["ROI "].append(round(roi, 2))
    veriler["Yatırım tarihi"].append(tarih)
    print("Verileriniz eklendi!\n")

# Hali hazırda dosya varsa yüklemek için
if os.path.exists(dosya_ismi) and os.path.getsize(dosya_ismi) > 0:
    df = pd.read_csv(dosya_ismi)

    for col in veriler.keys():
        veriler[col].extend(df[col].tolist())

    print("Geçmiş yatırım verileri yüklendi:")
    print(df)
else:
    print("Geçmiş yatırım verisi bulunamadı veya dosya içeriği boş.")

while True:
    devam = input("Yeni bir kripto girişi eklemek ister misiniz? (Evet:'e'/Hayır:'h'): ").lower()
    if devam == 'e':
        veri_al()
    else:
        break

df = pd.DataFrame(veriler)
print(df)

toplam_yatirim = df["Toplam yatırım"].sum()
toplam_kazanc = df["Kazanç"].sum()

print(f"\nToplam Yatırım: {toplam_yatirim} ")
print(f"Toplam Kazanç: {toplam_kazanc} ")
print(f"Genel ROI: {round((toplam_kazanc / toplam_yatirim) * 100, 2)} %")

df.to_csv("yatirim_ozeti.csv", index=False)
print("\nVeriler 'yatirim_ozeti.csv' dosyasına kaydedildi.")

#Yatırıma göre grafik
plt.plot(df["Yatırım tarihi"], df["ROI "], marker='o', color='gold')
plt.title("Kasa ROI Değişim Grafiği")
plt.xlabel("Yatırım Tarihi")
plt.ylabel("ROI")
plt.xticks(rotation=15) 
plt.grid(True)
plt.tight_layout()
plt.show()

#Yatırım başına kar/zarar yüzdesi
plt.bar(df["Kripto ismi"], df["ROI "], color=['green' if roi >= 0 else 'red' for roi in df["ROI "]])
plt.title("Yatırım Başına Kar/Zarar Yüzdesi")
plt.xlabel("Kripto İsmi")
plt.ylabel("Kar/Zarar (%)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
