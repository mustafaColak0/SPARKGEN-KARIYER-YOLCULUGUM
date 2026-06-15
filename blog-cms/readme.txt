# 🚀 Mini Blog İçerik Yönetim Sistemi (Blog-CMS)

Bu proje, modern bir web uygulamasının temelini oluşturan **CRUD (Create, Read, Update, Delete)** operasyonlarını ve full-stack mimariyi anlamak amacıyla geliştirilmiş dinamik bir İçerik Yönetim Sistemidir (CMS). 

Uygulama; asenkron JavaScript mimarisiyle çalışan hafif bir frontend vitrini ile Python Flask ve SQLite tabanlı güvenli bir backend motorunu bir araya getirir.

---

## 🛠️ Kullanılan Teknolojiler

### Backend (Mutfak)
* **Python 3.12:** Uygulama mantığının kurulması.
* **Flask:** RESTful API endpoint'lerinin tasarlanması.
* **Flask-SQLAlchemy:** SQLite veritabanı için ORM (Object-Relational Mapping) katmanı.
* **Flask-CORS:** Güvenli kökenler arası kaynak paylaşımı (Cross-Origin Resource Sharing) yönetimi.
* **SQLite:** Sunucu kurulumu gerektirmeyen, hafif ve gömülü ilişkisel veritabanı.

### Frontend (Vitrin)
* **HTML5 & CSS3:** Semantik yapı ve modern, responsive (mobil uyumlu) kullanıcı arayüzü tasarımı.
* **Vanilla JavaScript (ES6+):** `fetch` API ile asenkron veri yönetimi, DOM manipülasyonu ve dinamik arayüz güncellemeleri.

---

## 🏗️ Proje Mimarisi ve Özellikleri

1.  **RESTful API Tasarımı:** Ön yüz ve arka yüz birbirine tamamen bağımsız (decoupled) şekilde, standart JSON formatında HTTP istekleri (`GET`, `POST`, `DELETE`) üzerinden haberleşir.
2.  **Otomatik Veritabanı Yönetimi:** Uygulama ilk kez ayağa kalktığında, SQLite tablosu (`blog.db`) backend context'i tarafından otomatik olarak şemaya uygun şekilde oluşturulur.
3.  **Siber Güvenlik (XSS Koruması):** Kullanıcıdan alınan girdiler, frontend tarafında özel bir `escapeHTML` süzgecinden geçirilerek veritabanı kaynaklı Cross-Site Scripting (XSS) saldırılarına karşı proaktif olarak korunur.
4.  **Asenkron UX:** Yeni yazı ekleme veya silme işlemleri sırasında sayfa tamamen yenilenmez; asenkron JavaScript motoru sayesinde sadece ilgili DOM bileşenleri güncellenir.

---

## 📁 Klasör Yapısı

```text
blog-cms/
├── backend/
│   ├── app.py          # Flask API sunucusu ve DB modelleri
│   └── blog.db         # Otomatik oluşan SQLite veritabanı (Git'e yüklenmez)
├── frontend/
│   ├── index.html      # Ana arayüz iskeleti
│   ├── style.css       # Modern UI stilleri
│   └── script.js       # Asenkron API motoru ve DOM yönetimi
└── README.md           # Proje dokümantasyonu

🚀 Kurulum ve Çalıştırma

### 1. Backend Kurulumu
Öncelikle terminal üzerinden backend klasörüne gidin, gerekli kütüphaneleri yükleyin ve sunucuyu ateşleyin:

```bash
cd backend
pip install flask flask-sqlalchemy flask-cors
python app.py

```
Sunucu varsayılan olarak http://127.0.0.1:5000 portunda istekleri dinlemeye başlayacaktır.

### 2. Frontend Çalıştırma
Herhangi bir sunucu kurulumuna gerek yoktur. frontend/index.html dosyasını tarayıcınızda (Chrome, Edge, Firefox vb.) doğrudan çift tıklayarak açabilir veya VS Code Live Server eklentisiyle yerel olarak yayınlayabilirsiniz.

## 🧠 Karşılaşılan Zorluklar ve Çözüm Yolları (Post-Mortem & Debugging)

Proje geliştirme sürecinde karşılaşılan teknik problemler, nedenleri ve uygulanan siber/yazılımsal çözüm stratejileri aşağıda özetlenmiştir:

### 1. Python Sınıf Yapısı ve Case-Sensitivity (Büyük/Küçük Harf) Duyarlılığı
* **Zorluk:** Veritabanı modeli oluşturulurken `AttributeError: model. Did you mean: 'Model'?` hatasıyla karşılaşıldı ve Flask sunucusu çöktü. Ayrıca sınıf içi serileştirme fonksiyonu olan `to_dict` metodunun girinti (indentation) hatasından dolayı sınıf dışında kalması sebebiyle nesne özniteliği bulunamadı hatası alındı.
* **Çözüm:** Python'ın ve ORM (SQLAlchemy) mimarisinin katı nesne yönelimli programlama (OOP) kuralları analiz edildi. `db.model` ifadesi `db.Model` olarak düzeltildi. `to_dict` fonksiyonu doğru girinti seviyesine getirilerek `BlogPost` sınıfının içerisine kapsüllendi (encapsulation).

### 2. Otomatik Tamamlama (Autocomplete) ve DOM API Hataları
* **Zorluk:** Yeni içerik ekleme formundan veriler gönderilirken backend tarafına boş veya `undefined` veri gitmesi sorunu yaşandı. Konsol logları incelendiğinde geliştirme ortamının (IDE) otomatik tamamlama kazası sonucu `.value` yerine `.ariaValueMax` özelliğini atadığı fark edildi. Ayrıca yazıları listelerken `posts.length` ifadesinin yanlışlıkla `posts.Lenght` şeklinde yazılması DOM manipülasyonunu kilitledi.
* **Çözüm:** Tarayıcı geliştirici araçları (Chrome DevTools Console) aktif kullanılarak hata takibi yapıldı. JavaScript'in büyük/küçük harf hassasiyeti gözetilerek `length` property'si düzeltildi. Form elemanlarının ham metin değerlerini yakalamak için erişilebilirlik (accessibility) nitelikleri yerine doğrudan standart `.value` DOM API özelliği entegre edildi.

### 3. DOM Eleman Adlandırma Uyuşmazlığı (Null Pointer Hatası)
* **Zorluk:** Sayfa ilk yüklendiğinde tarayıcı konsolunda `TypeError: Cannot set properties of null (setting 'innerHTML')` ve `ReferenceError: postsList is not defined` hataları alındı ve API'den gelen veriler ekrana basılamadı.
* **Çözüm:** Adli bilişim (forensics) mantığıyla HTML ve JavaScript kodları satır satır karşılaştırıldı. HTML tarafındaki `<div id="postsList">` (çoğul) elementi ile script tarafında tanımlanan `postList` (tekil) değişken adlandırmasındaki yazım hatası (typo) tespit edildi. JavaScript tarafındaki değişken ve seçiciler (selectors) HTML id mimarisiyle tam senkronize hale getirilerek hata kökten çözüldü.
