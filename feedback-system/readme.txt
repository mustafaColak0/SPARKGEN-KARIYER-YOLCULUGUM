# 💬 Kullanıcı Geri Bildirim Sistemi (User Feedback & Management System)

Bu proje; modern SaaS uygulamaları, e-ticaret platformları ve müşteri ilişkileri yönetimi (CRM) sistemlerinin en kritik bileşeni olan kullanıcı etkileşimi ve veri işleme süreçlerini simüle etmek amacıyla geliştirilmiştir. 

Ön yüzde kullanıcı deneyimini (UX) üst seviyede tutan dinamik yapılar kurulurken, arka yüzde siber güvenlik odaklı veri doğrulama (validation) ve kalıcı dosya kaydı (data persistence) mimarisi uygulanmıştır.

---

## 🛠️ Kullanılan Teknolojiler

### Backend (Arka Yüz)
* **Python 3.12 & Flask:** RESTful API endpoint tasarımı ve HTTP istek yönetimi.
* **Flask-CORS:** Güvenli yerel kökenler arası kaynak paylaşımı (Cross-Origin Resource Sharing) yapılandırması.
* **JSON/OS Modülleri:** Veritabanı bağımsız kalıcı veri yönetimi ve I/O işlemleri.

### Frontend (Ön Yüz)
* **HTML5 & CSS3:** Kurumsal SaaS arayüz tasarımı, responsive (mobil uyumlu) grid/flexbox yapısı ve CSS ön ek (vendor prefix) standardizasyonu.
* **Vanilla JavaScript (ES6+):** `async/await` tabanlı Fetch API mimarisi, gelişmiş Regex e-posta validasyonu ve anlık DOM güncellemeleri.

---

## 🏗️ Mimari ve Öne Çıkan Teknik Özellikler

1. **Çift Katmanlı Validasyon (Double-Gate Validation):** Sistem güvenliğini maksimuma çıkarmak adına veri doğrulaması hem kullanıcı tarafında (JavaScript Regex & uzunluk kontrolleri) hem de sunucu tarafında (Python Flask parametre kontrolleri) bağımsız olarak iki kez yapılmaktadır.
2. **Kalıcı Veri Katmanı (Data Persistence):** Gelen geri bildirimler geçici RAM yerine, backend üzerinde yapılandırılmış bir `feedback_data.json` dosyasına asenkron olarak yazılır ve sunucu kapansa dahi veri kaybı önlenir.
3. **Unicode Standardizasyonu:** Türkçe karakter uyumluluğu ve veri transferi güvenliği için JSON serileştirme süreçleri evrensel standartlara uygun olarak yönetilmiştir.

---

## 🚀 Kurulum ve Çalıştırma Rehberi (Installation Guide)

Projenin yerel ortamınızda (local) çalıştırılabilmesi için aşağıdaki adımları sırasıyla uygulayınız:

### 1. Backend (Arka Yüz) Kurulumu
1. Bir terminal (Git Bash, CMD veya terminal) açarak `feedback-system` klasörünün içine girin.
2. Python sanal ortamını (virtual environment) oluşturun ve aktifleştirin:
   ```bash
   # Sanal ortam oluşturma
   python -m venv feedback_env

   # Aktifleştirme (Windows için)
   feedback_env\Scripts\activate

   # Aktifleştirme (Mac/Linux için)
   source feedback_env/bin/activate
```
3. Gerekli kütüphaneleri yükleyin:
	
 ```bash
pip install flask flask-cors
```

4. API sunucusunu başlatın:

 ```bash
python app.py
```

python app.py
Sunucu varsayılan olarak http://127.0.0.1:5000 portunda çalışmaya başlayacaktır.

### 2. Frontend (Ön Yüz) Çalıştırma
Arka yüz sunucusu açıkken, frontend/index.html dosyasını tarayıcınızda (Chrome, Edge, Safari vb.) doğrudan çift tıklayarak açın veya VS Code üzerinden Live Server eklentisiyle çalıştırın.

Form üzerinden veri gönderdiğinizde, sistem otomatik olarak asenkron şekilde lokal API'nize bağlanacak ve verileri feedback_data.json dosyasına işleyecektir.

Gönderilen verileri ham bir veritabanı logu gibi izlemek için tarayıcınızdan http://127.0.0.1:5000/admin/feedbacks adresine gidin.



## ⚙️ Karşılaşılan Zorluklar ve Çözüm Yolları

### 1. CSS Tarayıcı Ön Ekleri ve Standart Uyumluluğu (Vendor Prefixes)
* **Zorluk:** Özel `input[type="range"]` slider tasarımlarında `-webkit-appearance: none;` kullanımı esnasında geliştirme editöründe tarayıcı uyumluluk uyarıları alındı.
* **Çözüm:** Sadece Webkit (Chrome/Safari) motorlarına değil, tüm modern standart tarayıcılara (Firefox vb.) uyum sağlaması için kod tabanına ön eksiz standart **`appearance: none;`** parametresi eklenerek tarayıcılar arası görsel bütünlük sağlandı.

### 2. JSON Dosya Okuma ve Bozulma Yönetimi (File I/O Parsing)
* **Zorluk:** JSON dosyası ilk kez oluşturulurken veya dosya içi veriler manuel silindiğinde `json.JSONDecodeError` hataları tetiklendi ve sunucu çöktü.
* **Çözüm:** Dosya okuma süreçleri `try-except` blokları içerisine alınarak `os.path.exists` kontrolleri entegre edildi. Dosyanın bozuk veya boş olması durumunda uygulamanın çökmesi engellenerek otomatik olarak yeni bir veri şeması (boş liste) başlatılması sağlandı.

---

## 🗺️ Gelecek Planları ve Yol Haritası (Future Roadmap)

Uygulamanın büyük ölçekli kurumsal projelere ve üretim ortamlarına (production) entegre edilebilmesi için planlanan ileri düzey geliştirmeler:

### 1. Gelişmiş Veri Tabanı Entegrasyonu
* **Mevcut Durum:** Veriler yerel bir JSON dosyasında tutulmaktadır ve eşzamanlı binlerce istek geldiğinde dosya kilitleme sorunları yaratabilir.
* **Gelecek Planı:** İlişkisel veri analizleri ve hızlı sorgulamalar için **PostgreSQL** veya **SQLite** entegrasyonu yapılacaktır.

### 2. Gerçek Zamanlı Bildirimler (Real-Time Alerting)
* **Mevcut Durum:** Admin paneline düşen geri bildirimler sadece sayfa yenilendiğinde listelenmektedir.
* **Gelecek Planı:** **WebSockets (Flask-SocketIO)** teknolojisi kullanılarak, kullanıcı formu gönderdiği an admin ekranına sayfayı yenilemeye gerek kalmadan gerçek zamanlı anlık bildirim (push notification) düşmesi sağlanacaktır.

### 3. API Güvenliği ve Kimlik Doğrulama (Auth & Tokenization)
* **Mevcut Durum:** `/admin/feedbacks` endpoint'i herkese açık olup herhangi bir güvenlik katmanına sahip değildir.
* **Gelecek Planı:** Admin paneline yetkisiz erişimi engellemek amacıyla **JWT (JSON Web Token)** tabanlı kimlik doğrulama sistemi kurulacak ve rol tabanlı erişim kontrolü (`RBAC`) uygulanacaktır.

### 4. Otomatize Test Süreçleri (Automated Testing)
* **Mevcut Durum:** Testler tarayıcı üzerinden manuel veriler girilerek gerçekleştirilmektedir.
* **Gelecek Planı:** Backend tarafında API rotalarının yük testleri ve fonksiyonel testleri için **Pytest**, frontend validasyon motoru için ise **Jest** test senaryoları koda dahil edilecektir.