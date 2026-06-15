🌤️ Canlı Hava Durumu Uygulaması (Asenkron API Entegrasyonu)
Bu proje; üçüncü parti bir RESTful API (OpenWeatherMap) üzerinden küresel canlı hava durumu verilerini asenkron olarak çekip, dinamik ve modern bir kullanıcı arayüzü (UI) üzerinden anlık sunan bir Frontend / Web Geliştirme çalışmasıdır.

Uygulama, modern JavaScript mimarilerini ve web standartlarını optimize ederek kullanıcıya minimum gecikmeyle veri sunmayı hedefler.

🚀 Proje Özellikleri
Canlı Veri Tüketimi: OpenWeatherMap API'sine dinamik şehir parametreleri gönderilerek sıcaklık, nem, rüzgar hızı ve hava durumu açıklamaları anlık olarak çekilir.

Asenkron Programlama (Async/Await): Ağ istekleri sırasında arayüzün donmasını engellemek ve tarayıcı performansını maksimumda tutmak için modern JavaScript async/await ve fetch mimarisi kullanılmıştır.

Dinamik DOM Manipülasyonu: Gelen JSON verileri, JavaScript aracılığıyla HTML elementlerine anlık olarak enjekte edilir ve başlangıçta gizli olan sonuç paneli (display: block) animasyonlu bir şekilde görünür kılınır.

UX & Erişebilirlik: Kullanıcının sadece "Ara" butonuna tıklaması değil, input alanındayken Enter tuşuna basması da (keypress event listener) akıllıca dinlenerek kullanıcı deneyimi (UX) optimize edilmiştir.

Hata Yönetimi (Exception Handling): Geçersiz şehir isimleri veya ağ kopmaları gibi durumlarda uygulamanın çökmesi try-catch bloklarıyla engellenmiş, kullanıcıya zarif uyarılar sunulmuştur.

🛠️ Kullanılan Teknolojiler
Frontend: HTML5, CSS3 (Modern Linear Gradient & CSS Animations)

Programlama Dili: JavaScript (ES6+, Fetch API, Asynchronous JS)

Veri Sağlayıcı: OpenWeatherMap API

⚙️ Kurulum ve Çalıştırma Rehberi (Installation Guide)

### 1. Klasör Yapısı
Projenin lokalinizde kararlı çalışabilmesi için aşağıdaki dosya yapısının korunması gerekir:
```
weather-app/
├── index.html
├── style.css
└── script.js
```
### 2. Çalıştırma Talimatı
⚠️ Önemli Not: Tarayıcıların güvenlik politikaları (CORS) gereği, index.html dosyası doğrudan çift tıklanarak açılmamalıdır. Lokal bir sunucu simülasyonu şarttır.

Projeyi Visual Studio Code ile açın.

Live Server eklentisini başlatarak uygulamayı lokal bir sunucu ([http://127.0.0.1:5500](http://127.0.0.1:5500)) üzerinden canlıya alın.

Alternatif olarak, projeyi anında dünya çapında erişime açmak ve canlı demoyu sunmak için Netlify veya Vercel platformları üzerinde deploy edebilirsiniz.

🛡️ Karşılaşılan Zorluklar ve Siber Çözümler (Debugging)
1. Scope (Kapsam) ve Süslü Parantez {} Tuzağı
Sorun: Projenin ilk aşamalarında buton tıklama ve tuş dinleme olayları (addEventListener), handleSearch fonksiyonunun kapanış parantezinin içine yazıldığı için tarayıcı butonları algılayamamış ve fonksiyonlar birbirini kilitlemiştir.

Çözüm: Fonksiyon parantezleri milimetrik olarak incelenmiş, tetikleyiciler fonksiyonun içinden kurtarılarak küresel (global) alana taşınmış ve kodun siber tüneli (veri akışı) başarıyla aktif edilmiştir.

2. ID Eşleşme Uyuşmazlığı (DOM Eleman Yakalama Hatası)
Sorun: HTML tarafında id="searchBtn" olarak tanımlanan buton elementinin JavaScript tarafında kebab-case (search-btn) olarak çağrılmasından dolayı eleman yakalanamamış ve konsolda "silent error" (sessiz hata) oluşmuştur.

Çözüm: DOM isimlendirmeleri camelCase standardına (searchBtn) göre eşitlenerek elementlerin birbiriyle eksiksiz konuşması sağlanmıştır.

🗺️ Gelecek Planları ve Yol Haritası (Future Roadmap)
Gelişmiş Meteoroloji Tahminleri: Sadece anlık hava durumu değil, OpenWeather 5 Days / 3 Hours Forecast API entegrasyonu yapılarak 5 günlük geleceğe yönelik hava tahmin grafikleri eklenecektir.

Kullanıcı Kişiselleştirme (Favori Şehirler): Tarayıcının LocalStorage API'si kullanılarak kullanıcının sık arattığı şehirler hafızada tutulacak ve uygulama her açıldığında favori şehirlerin hava durumu otomatik yüklenecektir.

Farklı API Sektörlerine Genişleme: Bu projede kazanılan asenkron API entegrasyon tecrübesi; ilerleyen aşamalarda Fintech ve E-Ticaret sektörlerindeki fırsatlara hazırlık olması amacıyla Haber API'leri, Kripto Para/Borsa Canlı API'leri ve Film Veritabanı API'leri (OMDb) entegrasyonlarıyla genişletilecektir.


