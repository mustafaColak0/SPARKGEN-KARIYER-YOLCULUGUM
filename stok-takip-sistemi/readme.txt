# 📦 Gerçek Zamanlı Stok Takip Sistemi (Inventory Management System)

Bu proje; perakende, e-ticaret ve lojistik sektörlerinin en kritik ihtiyaçlarından biri olan envanter ve stok yönetimini simüle etmek amacıyla geliştirilmiş dinamik bir **Full-Stack** uygulamadır. 

Ön yüz ile arka yüzün tamamen bağımsız (decoupled) çalıştığı, asenkron veri akışına dayalı **RESTful API** mimarisiyle inşa edilmiştir.

---

## 🛠️ Kullanılan Teknolojiler

### Backend (Arka Yüz)
* **Python 3.12:** Uygulama mantığının ve veri işleme süreçlerinin kurulması.
* **Flask:** RESTful API endpoint'lerinin tasarlanması ve HTTP metotlarının yönetimi.
* **Flask-CORS:** Frontend ile backend arasındaki kökenler arası kaynak paylaşımı (Cross-Origin Resource Sharing) güvenliğinin lokal mimaride yapılandırılması.

### Frontend (Ön Yüz)
* **HTML5 & CSS3:** Modern, flexbox tabanlı responsive arayüz tasarımı ve gölgelendirmeli kurumsal dashboard görünümü.
* **Vanilla JavaScript (ES6+):** `async/await` mimarisiyle Fetch API yönetimi ve dinamik DOM manipülasyonu.

---

## 🏗️ Mimari ve Öne Çıkan Teknik Özellikler

1. **RESTful Standartları:** Kaynak yönetimi tek bir ortak rota (`/api/urunler`) üzerinden, HTTP verb'lerinin (`GET` ve `POST`) ayrıştırılmasıyla kurumsal standartlara uygun şekilde yapılmıştır.
2. **Dinamik Veri Renderı (DOM Manipülasyonu):** Sayfada statik HTML tabloları yerine, HTML `<tbody>` elementi tamamen boş bırakılmış; JavaScript asenkron motoru backend'den aldığı JSON verilerini gerçek zamanlı olarak döngüye sokarak sayfayı dinamik olarak inşa etmiştir (Client-Side Rendering).
3. **Güvenlik (XSS Filtresi):** Kullanıcının form aracılığıyla envantere gönderdiği veriler, JavaScript tarafında özel bir `escapeHTML` süzgecinden geçirilerek script injeksiyon saldırılarına karşı güvenli hale getirilmiştir.

---

## 📁 Klasör Yapısı

```text
stok-takip-sistemi/
├── backend/
│   └── app.py          # Flask REST API Sunucusu
└── frontend/
    ├── index.html      # UI İskeleti
    ├── style.css       # Kurumsal Dashboard Stilleri
    └── script.js       # Asenkron Veri Motoru ve DOM Yönetimi


### 🧠 Karşılaşılan Zorluklar ve Çözüm Yolları
Projenin geliştirilmesi ve entegrasyonu sürecinde karşılaşılan zorluklar ve uygulanan debugging stratejileri:

1. Template Literals (${}) ve Tırnak İşareti Uyuşmazlığı
Zorluk: API istekleri sırasında fetch fonksiyonunun değişkeni okuyamaması ve var olmayan bir adrese gitmeye çalışması sonucu 404 Not Found ve bağlantı hataları alındı.

Çözüm: JavaScript'te string interpolasyonu (${değişken}) yapılabilmesi için düz tek tırnak (') yerine ters tırnak (backtick - `) işaretinin kullanılması gerektiği analiz edildi ve sözdizimi (syntax) güncellenerek dinamik URL yapısı sağlandı.

2. Nesne Öznitelikleri ve Eksik Veri Paketlemesi (Payload Validation)
Zorluk: Form verileri backend'e gönderilirken veritabanı/RAM listesine eklenemedi ve backend tarafında "Lütfen tüm alanları doldurun!" validasyon hatası tetiklendi. Ayrıca tarayıcı otomatik tamamlama (autocomplete) hatası yüzünden ürün adları undefined olarak gitti.

Çözüm: script.js içindeki veri paketi (payload Object) incelendi. IDE hatası olan .ariaValueMax özelliği kaldırılıp yerine .value DOM API'si entegre edildi. Pakete eklenmesi unutulan fiyat parametresi parseFloat() fonksiyonuyla sayısal tipe dönüştürülerek nesneye eklendi ve backend'in veri şemasıyla tam senkronizasyon sağlandı.

3. Zaman Biçimlendirme ve Format Belirteçleri
Zorluk: Python datetime kütüphanesiyle tarih basılırken biçimlendirme hatası (büyük/küçük harf duyarlılığı) nedeniyle tarihler arasına hatalı eğik çizgiler girdi.

Çözüm: Python'ın strftime dökümantasyonu incelenerek büyük %D karakterinin yerel formatta çakışma yarattığı görüldü; standart gün/ay/yıl nizamı için küçük %d belirteciyle revize edilerek jilet gibi bir kronolojik veri yapısı elde edildi.

### 🚀 Kurulum ve Çalıştırma
Terminalinizden backend klasörüne gidin ve Flask uygulamasını ayağa kaldırın:

```bash

cd backend
python app.py

```

frontend/index.html dosyasını tarayıcınızda doğrudan veya bir yerel sunucu (örn: Live Server) yardımıyla açın. Arayüz, yerel API sunucunuzla otomatik olarak asenkron entegrasyona geçecektir.



## 🗺️ Gelecek Planları ve Yol Haritası (Future Roadmap)

Uygulamanın kurumsal seviyede bir SaaS (Software as a Service) ürününe dönüşebilmesi ve gerçek üretim ortamlarında (production) milyonlarca veriyi işleyebilmesi için planlanan geliştirmeler aşağıda listelenmiştir:

### 1. Veri Katmanının Modernizasyonu (Persistency)
* **Mevcut Durum:** Veriler RAM üzerinde (`stok_listesi` dizisinde) tutulmaktadır. Sunucu kapandığında veya yeniden başladığında veriler kaybolur.
* **Gelecek Planı:** Sisteme kalıcı veri katmanı eklenecektir. İlişkisel veri yapıları ve gelişmiş raporlama (stok hareketleri günlükleri) için **PostgreSQL** veya esnek ürün nitelikleri (renk, boyut, varyant) barındıran esnek şemalar için **MongoDB** entegrasyonu yapılacaktır. ORM aracı olarak **SQLAlchemy** veya **Beanie** kullanılacaktır.

### 2. Güvenlik ve Kimlik Doğrulama (Authentication & Authorization)
* **Mevcut Durum:** API endpoint'leri herkese açıktır ve herhangi bir yetkilendirme katmanı bulunmamaktadır.
* **Gelecek Planı:** Her işletmenin veya depo görevlisinin sadece kendi envanterini görebilmesi için **JWT (JSON Web Token)** tabanlı kullanıcı giriş (Auth) sistemi kurulacaktır. `Role-Based Access Control (RBAC)` ile "Yönetici" (ürün ekleme/silme yetkisi) ve "Personel" (sadece stok görme yetkisi) rolleri ayrıştırılacaktır.

### 3. Kritik Stok Uyarıları & Gerçek Zamanlı Bildirimler (Real-time Alerting)
* **Mevcut Durum:** Stok miktarları sadece tabloda statik olarak izlenmektedir.
* **Gelecek Planı:** Ürünlerin altına bir "Kritik Eşik" (örn: minimum 5 adet) parametresi eklenecektir. Stok miktarı bu eşiğin altına düştüğünde arayüzde kırmızı alarm yanacak, arka planda **WebSockets (Flask-SocketIO)** kullanılarak sayfayı yenilemeye gerek kalmadan anlık pop-up bildirimler fırlatılacaktır. Ayrıca yöneticilere **Celery** ve **Redis** entegrasyonuyla otomatik stok uyarı e-postaları gönderilecektir.

### 4. Gelişmiş Filtreleme, Kategorizasyon ve Raporlama
* **Mevcut Durum:** Tüm ürünler tek bir düz liste halinde listelenmektedir.
* **Gelecek Planı:** Ürünlere `Kategori` (Elektronik, Gıda vb.) mimarisi eklenecektir. Backend tarafında dinamik sorgu parametreleri (`/api/urunler?kategori=elektronik&sirala=fiyat_artan`) yazılarak frontend'de gelişmiş arama ve filtreleme barları kurulacaktır. Envanterin toplam mali değerini ve en çok satan/azalan ürünleri gösteren grafiksel bir **Dashboard (Chart.js)** paneli entegre edilecektir.

### 5. Frontend Mimarisinin Framework Seviyesine Taşınması
* **Mevcut Durum:** Ön yüz Vanilla JavaScript ve manuel DOM enjeksiyonu ile yönetilmektedir. Proje büyüdükçe bu mimariyi yönetmek (state management) zorlaşacaktır.
* **Gelecek Planı:** Kod tabanının bileşen bazlı (component-based) bir yapıya kavuşması, daha hızlı render edilmesi ve profesyonel state yönetimi için ön yüz **React (Vite)** veya **Vue.js** mimarisine taşınacaktır. API istekleri için daha gelişmiş interceptor özelliklerine sahip olan **Axios** kütüphanesine geçiş yapılacaktır.
