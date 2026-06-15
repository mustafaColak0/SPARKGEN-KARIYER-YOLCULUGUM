# 📊 Python ile Dinamik Veri Analizi Dashboard Uygulaması

Bu proje; işletmelerin satış, kullanıcı veya operasyonel ham verilerini işleyerek anlamlı metriklere, grafiklere ve dinamik raporlara dönüştüren bir **Veri Analitiği ve Dashboard** uygulamasıdır. 

Proje kapsamında veri ön işleme (data preprocessing), istatistiksel çıkarımlar ve veri görselleştirme hatları (pipelines) inşa edilmiştir.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

* **Python 3.12:** Veri işleme analitiğinin ana motoru.
* **Pandas:** Ham veri setlerinin okunması, eksik/hatalı verilerin temizlenmesi ve veri manipülasyonu.
* **Matplotlib / Seaborn:** Trend analizi, dağılım grafikleri ve kurumsal renk paletlerine uygun veri görselleştirme süreçleri.
* **Flask (Opsiyonel/Altyapı):** Analiz sonuçlarının ve grafiklerin web tabanlı bir arayüze veri modeli olarak aktarılması.

---

## 🏗️ Mimari ve Öne Çıkan Teknik Özellikler

1. **Veri Ön İşleme & Temizlik (Data Cleaning):** Veri setindeki tekrarlayan (duplicate) kayıtlar elenmiş, eksik veriler istatistiksel yöntemlerle (ortalama/medyan) doldurularak analizin sapması önlenmiştir.
2. **Betimsel İstatistik (Descriptive Statistics):** Şirket yöneticilerinin tek bakışta görebileceği Toplam Satış, Ortalama Sepet Tutarı ve En Çok Satan Kategoriler gibi kritik performans göstergeleri (KPI) dinamik olarak hesaplanmıştır.

---

## ⚙️ Karşılaşılan Zorluklar ve Çözüm Yolları

### 1. Veri Tipi Uyuşmazlıkları ve Tarih Serisi Analizi (Datetime Parsing)
* **Zorluk:** Ham veri setindeki tarih kolonlarının `string (object)` olarak gelmesi sebebiyle kronolojik sıralama, aylık/haftalık kırılımlarda grafik çizdirirken hatalar alındı ve veri eksenleri çakıştı.

* **Çözüm:** Pandas kütüphanesinin `to_datetime()` fonksiyonu kullanılarak ilgili kolonlar gerçek zaman serisi formatına dönüştürüldü. Eksik tarih formatları saptanıp temizlenerek zaman odaklı analizlerin hatasız akması sağlandı.

---

## 🚀 Kurulum ve Çalıştırma Rehberi (Installation Guide)

### 1. Ortamın Hazırlanması
1. Terminalden `veri_dashboard` klasörünün içine girin.
2. Python sanal ortamını aktifleştirin ve analitik kütüphaneleri yükleyin:
   ```bash
   # Windows için
   feedback_env\Scripts\activate
   
   # Gerekli paketlerin yüklenmesi
   pip install pandas matplotlib seaborn flask
```
2. Analizin Başlatılması
Ana analiz betiğini çalıştırarak veri setinin işlenmesini ve grafiklerin üretilmesini sağlayın:

```bash
python main.py
```

Üretilen dashboard grafiklerini ve özet rapor çıktılarını klasör içerisindeki output/ dizininden veya ayağa kalkan yerel web arayüzünden izleyebilirsiniz.


---

## 🗺️ Gelecek Planları ve Yol Haritası (Future Roadmap)

* **Canlı Veri Toplama (Web Scraping):** Sabit veri setleri yerine **BeautifulSoup** veya **Scrapy** kullanılarak e-ticaret sitelerinden anlık fiyat/ürün verisi çeken dinamik bir veri boru hattı (Data Pipeline) kurulacaktır.
* **Tahminleme Modelleri (Machine Learning):** Geçmiş verilere dayanarak gelecekteki satış trendlerini veya stok ihtiyaçlarını tahmin edebilen temel **Scikit-Learn** regresyon modelleri entegre edilecektir.
* **Kurumsal Framework Geçişi:** Dashboard arayüzünün daha interaktif ve filtrelebilir olması amacıyla **Streamlit** veya full-stack **Django** mimarisine geçiş planlanmaktadır.
