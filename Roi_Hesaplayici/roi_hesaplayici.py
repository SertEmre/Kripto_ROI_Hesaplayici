import pandas as pd

kripto_ismi = input("Kripto ismi: ")
yatirim = float(input("Toplam yatırımınız ne kadar?: "))
giris_fiyati = float(input("Giriş fiyatınızı giriniz: "))
cikis_fiyati = float(input("Çıkış fiyatınızı giriniz: "))


kazanc = ((cikis_fiyati - giris_fiyati) / giris_fiyati) * yatirim
roi = (kazanc / yatirim) * 100

veriler = {
    "Kripto ismi": [kripto_ismi],
    "Toplam yatırım": [yatirim],
    "Giriş fiyatı": [giris_fiyati],
    "Çıkış fiyatı": [cikis_fiyati],
    "Kazanç": [round(kazanc, 2)],
    "ROI ": [round(roi, 2)]
}

df = pd.DataFrame(veriler)
print(df)
