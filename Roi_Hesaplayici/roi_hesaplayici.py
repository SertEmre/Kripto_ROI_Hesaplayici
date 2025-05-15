import pandas as pd

veriler = {
    "Kripto ismi": [],
    "Toplam yatırım": [],
    "Giriş fiyatı": [],
    "Çıkış fiyatı": [],
    "Kazanç": [],
    "ROI ": []
}

def veri_al():
    kripto_ismi = input("Kripto ismi: ")
    yatirim = float(input("Toplam yatırımınız ne kadar?: "))
    giris_fiyati = float(input("Giriş fiyatınızı giriniz: "))
    cikis_fiyati = float(input("Çıkış fiyatınızı giriniz: "))

    kazanc = ((cikis_fiyati - giris_fiyati) / giris_fiyati) * yatirim
    roi = (kazanc / yatirim) * 100

    veriler["Kripto ismi"].append(kripto_ismi)
    veriler["Toplam yatırım"].append(yatirim)
    veriler["Giriş fiyatı"].append(giris_fiyati)
    veriler["Çıkış fiyatı"].append(cikis_fiyati)
    veriler["Kazanç"].append(round(kazanc, 2))
    veriler["ROI "].append(round(roi, 2))
    print("Verileriniz eklendi!\n")

veri_al()

while True:
    devam = input("Yeni bir kripto girişi eklemek ister misiniz? (e/h): ").lower()
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