# 🗺️ Dinamik Veri Isı Haritası Uygulaması (Interactive Heatmap Application)

Bu proje; büyük veri kümelerinin, yoğunluk analizlerinin ve coğrafi/konumsal verilerin kullanıcıya anlamlı bir şekilde sunulmasını sağlayan dinamik bir **Full-Stack Veri Görselleştirme (Data Visualization)** uygulamasıdır. 

Kullanıcı etkileşimleri veya harita koordinatları üzerinden gelen yoğunluk verilerini backend katmanında işleyerek ön yüzde görsel bir analitik paneli (dashboard) sunar.

---

## 🛠️ Kullanılan Teknolojiler

### Backend (Arka Yüz)
* **Python 3.12 & Flask:** Yoğunluk matrislerinin, koordinat verilerinin hesaplanması ve RESTful veri akışının sağlanması.
* **Flask-CORS:** Frontend ile backend arasındaki veri transferinin (Cross-Origin) lokal ağda güvenli yönetimi.

### Frontend (Ön Yüz)
* **HTML5 & CSS3:** Analitik dashboard arayüzü, tam ekran harita yerleşimi ve responsive kontrol panelleri.
* **Vanilla JavaScript (ES6+):** Fetch API ile gerçek zamanlı veri çekme süreçleri, veri normalizasyonu ve dinamik Canvas/Grafik render işlemleri.

---

## 🏗️ Mimari ve Öne Çıkan Teknik Özellikler

1. **Veri Görselleştirme Algoritmaları:** Sayısal veriler ve koordinatlar, ön yüz motorunda renk skalalarına (gradient maps) dönüştürülerek kullanıcıya ham sayıların ötesinde "yoğunluk odaklı" bir UX (kullanıcı deneyimi) sunulmuştur.
2. **Performans Odaklı Render (Asenkron Akış):** Büyük veri setleri backend'den sıkıştırılmış JSON formatında çekilir ve JavaScript asenkron yapısı (`async/await`) sayesinde arayüzde donma veya takılma yaratmadan (non-blocking) render edilir.

---

## ⚙️ Karşılaşılan Zorluklar ve Çözüm Yolları

### 1. Eşzamanlı Veri Güncelleme ve Grafik Senkronizasyonu
* **Zorluk:** Backend tarafındaki yoğunluk haritası verileri değiştikçe, ön yüzün eski grafikleri temizleyememesi ve üst üste binerek (flickering) hatalı görsel sonuçlar üretmesi sorunu yaşandı.
* **Çözüm:** JavaScript veri çekme (fetch) döngüsünün başına canvas/grafik temizleme (`clearRect` veya state sıfırlama) katmanı eklendi. Gelen yeni veri paketinin eskileri tamamen ezmesi sağlanarak akıcı ve tutarlı bir görsel akış elde edildi.

---

## 🚀 Kurulum ve Çalıştırma Rehberi (Installation Guide)

### 1. Arka Yüzün Başlatılması
1. Terminalden `heatmap-app` klasörünün içine girin.
 Python sanal ortamını aktif hale getirin:
   ```bash
   # Windows için
   feedback_env\Scripts\activate
   # Mac/Linux için
   source feedback_env/bin/activate
```
3.Flask sunucusunu ayağa kaldırın:

```bash
python app.py
```
2. Ön Yüzün Çalıştırma
index.html dosyasını tarayıcınızda doğrudan açarak veya bir yerel sunucu (Live Server) vasıtasıyla başlatarak backend'den akan ısı haritası verilerini canlı olarak simüle edebilirsiniz.


---

## 🗺️ Gelecek Planları ve Yol Haritası (Future Roadmap)

* **Büyük Veritabanı ve Mekansal Sorgular (GIS):** Binlerce koordinat verisini milisaniyeler içinde işleyebilmek adına veri katmanına mekansal indeksleme (Spatial Indexing) destekli **PostgreSQL (PostGIS)** entegre edilecektir.
* **Canlı Veri Akışı (Streaming):** Isı haritasının saniyelik hareketlerle (örn: bir web sitesindeki anlık fare hareketleri) güncellenebilmesi için **WebSockets** mimarisine geçiş yapılacaktır.
* **Modern Grafik Kütüphaneleri:** Render kalitesini ve harita yeteneklerini artırmak adına frontend mimarisi **Leaflet.js** veya **D3.js** gibi sektörel standart veri görselleştirme kütüphaneleriyle optimize edilecektir.


