# 🌤️ Canlı Hava Durumu Uygulaması (Asenkron API Entegrasyonu)

Bu proje, üçüncü parti bir RESTful API (`OpenWeatherMap`) üzerinden küresel canlı hava durumu verilerini asenkron olarak çekip, dinamik ve modern bir kullanıcı arayüzü (UI) üzerinden anlık sunan bir **Frontend / Web Geliştirme** çalışmasıdır.

---

## 🚀 Proje Özellikleri

* **Canlı Veri Tüketimi:** OpenWeatherMap API'sine dinamik şehir parametreleri gönderilerek sıcaklık, nem, rüzgar hızı ve hava durumu açıklamaları anlık olarak çekilir.
* **Asenkron Programlama (Async/Await):** Ağ istekleri sırasında arayüzün donmasını engellemek ve performansı maksimumda tutmak için modern JavaScript `async/await` ve `fetch` mimarisi kullanılmıştır.
* **Dinamik DOM Manipülasyonu:** Gelen JSON verileri, JavaScript aracılığıyla HTML elementlerine anlık olarak enjekte edilir ve başlangıçta gizli olan sonuç paneli (`display: block`) animasyonlu bir şekilde görünür kılınır.
* **UX & Erişebilirlik:** Kullanıcının sadece "Ara" butonuna tıklaması değil, input alanındayken `Enter` tuşuna basması da (`keypress` event listener) akıllıca dinlenerek kullanıcı deneyimi optimize edilmiştir.
* **Hata Yönetimi (Exception Handling):** Geçersiz şehir isimleri veya ağ kopmaları gibi durumlarda uygulamanın çökmesi `try-catch` bloklarıyla engellenmiş, kullanıcıya zarif uyarılar (`alert`) sunulmuştur.

---

## 🛠️ Kullanılan Teknolojiler

* **Frontend:** HTML5, CSS3 (Modern Linear Gradient & CSS Animations)
* **Programlama Dili:** JavaScript (ES6+, Fetch API, Asynchronous JS)
* **Veri Sağlayıcı:** OpenWeatherMap API

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Klasör Yapısı
Projenin lokalinizde çalışabilmesi için aşağıdaki dosya yapısının korunması gerekir:
```text
weather-app/
├── index.html
├── style.css
└── script.js

2. Çalıştırma Talimatı
Tarayıcıların güvenlik politikaları (CORS) gereği, index.html dosyası doğrudan çift tıklanarak açılmamalıdır.

Projeyi Visual Studio Code ile açın.

Live Server eklentisini başlatarak uygulamayı lokal bir sunucu (http://127.0.0.1:5500) üzerinden canlıya alın.

🛡️ Karşılaşılan Zorluklar ve Siber Çözümler
1. Scope (Kapsam) ve Süslü Parantez {} Tuzağı
Sorun: Projenin ilk aşamalarında buton tıklama ve tuş dinleme olayları (addEventListener), handleSearch fonksiyonunun kapanış parantezinin içine yazıldığı için tarayıcı butonları algılayamamış ve fonksiyonlar birbirini kilitlemiştir.

Çözüm: Fonksiyon parantezleri milimetrik olarak incelenmiş, tetikleyiciler fonksiyonun içinden kurtarılarak küresel (global) alana taşınmış ve siber tünel başarıyla aktif edilmiştir.

2. ID Eşleşme Uyuşmazlığı
Sorun: HTML tarafında id="searchBtn" olarak tanımlanan buton elementinin JavaScript tarafında kebab-case (search-btn) olarak çağrılmasından dolayı eleman yakalanamamış ve sessiz bir hata oluşmuştur.

Çözüm: DOM isimlendirmeleri camelCase standardına (searchBtn) göre eşitlenerek elementlerin birbiriyle eksiksiz konuşması sağlanmıştır.