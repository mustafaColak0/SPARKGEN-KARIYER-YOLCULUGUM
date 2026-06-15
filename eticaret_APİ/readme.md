# 🛒 E-Ticaret Katalog Yönetim Sistemi (API Integration & Data Processing)

Bu proje, uzak bir RESTful API üzerinden canlı e-ticaret verilerini çekip, terminal üzerinde interaktif, optimize edilmiş ve kullanıcı dostu bir katalog yönetim paneli sunan bir **Fullstack / Backend** geliştirme çalışmasıdır.

---

## 🚀 Proje Özellikleri

* **Canlı API Entegrasyonu:** `FakeStoreAPI` servisinin `/products` uç noktasına (endpoint) dinamik HTTP istekleri atılarak gerçek zamanlı veriler tüketilmiştir.
* **Pandas ile Veri Analizi:** API'den dönen JSON verisi Pandas DataFrame yapısına dönüştürülerek toplam ürün sayısı ve benzersiz kategoriler otomatik analiz edilir.
* **Gelişmiş Filtreleme ve Sıralama:** * Kategori bazlı filtreleme (Büyük/küçük harf duyarlılığı filtrelenmiştir).
    * Minimum ve maksimum limitlere göre fiyat aralığı filtrelemesi.
    * Pahalıdan ucuza veya ucuzdan pahalıya dinamik fiyat sıralaması.
* **UX & Terminal Optimizasyonu:** `os` modülü kullanılarak ekran karmaşası engellenmiş, kullanıcı onaylı (`input()` frenli) akıllı ekran temizleme (`cls`) mekanizması entegre edilmiştir.
* **Hata Yönetimi (Exception Handling):** Ağ kopmaları, geçersiz URL istekleri veya kullanıcı taraflı hatalı veri girişlerine (`ValueError`) karşı sistem çökmesi engellenmiştir.

---

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Kütüphaneler:**
    * `requests` -> HTTP GET istekleri ve API tünel yönetimi için.
    * `pandas` -> Verilerin tablo formatında işlenmesi ve analitik raporlama için.
    * `json` -> Ham JSON verisinin `indent` ve `ensure_ascii` parametreleriyle görselleştirilmesi için.
    * `os` -> Terminal arayüzü ve ekran temizleme operasyonları için.

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın veya İndirin
```bash
git clone [https://github.com/KULLANICI_ADIN/eticaret-api-proje.git](https://github.com/KULLANICI_ADIN/eticaret-api-proje.git)
cd eticaret-api-proje
```
### 2. Sanal Ortamı (.venv) Aktif Edin ve Kütüphaneleri Kurun

```bash
# Bağımlılıkların yüklenmesi
pip install requests pandas
```
### 3. Projeyi Ateşleyin

```bash
python main.py
```

Karşılaşılan Zorluklar ve Siber Çözümler
1. Sanal Ortam (.venv) ve Global Kütüphane Çakışması
Sorun: pip install komutuyla kütüphaneler bilgisayara yüklenmesine rağmen IDE'nin (VS Code) yanlış Python Interpreter görmesinden kaynaklı ModuleNotFoundError: No module named 'requests' hatası alındı.

Çözüm: Ctrl + Shift + P kombinasyonuyla doğru Python Interpreter (global / Recommended) seçildi ve bağımlılıklar direkt aktif sanal ortamın kalbine izole edilerek sorun çözüldü.

2. Sonsuz Döngü İçinde Hızlı Ekran Temizleme İllüzyonu
Sorun: while True: döngüsünün en başına eklenen os.system('cls') komutu, Python'ın milisaniyeler seviyesindeki işlem hızı nedeniyle ekrana basılan ürün verilerini kullanıcının okumasına fırsat kalmadan siliyordu.

Çözüm: Her işlem bloğunun sonuna koşullu bir input("Devam etmek için ENTER'a basın...") fren mekanizması eklendi. Böylece kullanıcının veriyi rahatça okuması sağlandı ve ancak kullanıcı onay verdiğinde cls tetiklenerek arayüz taze bir menüyle başa döndürüldü.

📈 Gelecek Yol Haritası (Next Steps)
[ ] API Key ve Bearer Token kullanan, Authentication gerektiren güvenli API mimarilerine geçiş.

[ ] DDoS korumalı sunucular için Rate Limiting (İstek Sınırı) kontrollerinin entegre edilmesi.

[ ] Büyük veri setlerinde ağ gecikmesini (latency) sıfıra indirmek için async/await (Asenkron) optimizasyonu.

[ ] Bu backend mimarisini, React/Vue tabanlı bir frontend arayüzüne veya kişisel e-ticaret veri tabanına bağlamak.


