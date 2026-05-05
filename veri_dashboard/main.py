import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import plotly.express as px

# 1. Veri Okuma

df=pd.read_csv("data.csv")
print("Veriler Başariyla Okundu!")

#Veri Analizi
print("---Veri Seti Hakkinda Bilgi---")
print(df.head())
print("\n---Veri Seti İstatistikleri---")
print(df.describe())

# 2. Grafik: Matplotlib ile Sütun Grafiği oluşturma
plt.figure(figsize=(10,6))
df.groupby("Ürün")["Satiş"].sum().plot(kind="bar")
plt.title("Ürün Bazinda Toplam Satişlar")
plt.xlabel("Ürün")
plt.ylabel("Toplam Satiş")
plt.show()

# 3. Grafik: Günlük Satış Trendi (Line)
#Tarih bazında trend analizi 
df["Tarih"]=pd.to_datetime(df["Tarih"])
gunluk_satis=df.groupby("Tarih")["Satiş"].sum()
plt.figure(figsize=(12,5))
gunluk_satis.plot()
plt.title("Günlük Satiş Trendi")
plt.show()

# 4. Grafik: Bölge Bazında Pasta Grafiği Oluşturma
bolge_satis=df.groupby("Bölge")["Satiş"].sum()
plt.figure(figsize=(8,8))
plt.pie(bolge_satis.values, labels=bolge_satis.index, autopct="%1.1f%%")
plt.title("Bölge Bazinda Satiş Oranlari")
plt.show()

# TÜM GRAFİKLERİ AYNI ANDA GÖSTER
print("Grafikler hazirlaniyor... Lütfen pencereleri kontrol et.")
plt.show()

# Bu dashboard satış verilerini analiz eder
# 3 farklı grafik türü kullanır
# Pandas ile veri işleme yapar

