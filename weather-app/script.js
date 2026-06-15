const API_KEY ="7be09c52567b58f11cbf918cf8ecc4f6";

const searchBtn=document.getElementById("searchBtn");
const cityInput=document.getElementById("cityInput");
const weatherInfo=document.getElementById("weatherInfo");

async function getWeather(city){
// units=metric -> Dereceyi Celsius cinsinden getirir
    // lang=tr -> Hava durumu açıklamasını Türkçe getirir ("parçalı bulutlu" vs.)
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric&lang=tr`;

try{

    const response =await fetch(url);
    
    //Eğer sunucu 200 ok dönmediyse (şehir bulunamadıysa vs.) direkt catch bloğuna fırlat

    if(!response.ok){
        throw new Error("Şehir bulunamadı");
    }

    const data=await response.json();
    displayWeather(data);

}catch(error)
{
    alert('[-] Hata: Şehir bulunamadı veya API anahtarı henüz aktif değil!');
    weatherInfo.style.display="none";
}
}

function displayWeather(data){
   // DOM manipülasyonu ile HTML elemanlarının içini API'den gelen verilerle dolduruyoruz.
   document.getElementById("cityName").textContent=data.name + ',' + data.sys.country;
   document.getElementById('temperature').textContent = Math.round(data.main.temp) + '°C';
    document.getElementById('description').textContent = data.weather[0].description;
    document.getElementById('humidity').textContent = data.main.humidity + '%';
    document.getElementById('windSpeed').textContent = data.wind.speed + ' m/s';
    // Veriler başarıyla yüklendiği için gizli olan paneli görünür yapıyoruz
    weatherInfo.style.display = 'block';
}

function handleSearch(){
    const city = cityInput.value.trim();
    if(city){
        getWeather(city);
    }
    else{
        alert('[-] Hata: Lütfen bir şehir adı girin!');
    }
}
    // Butona tıklayınca aramayı tetikler
    searchBtn.addEventListener('click', handleSearch);

    //input alanında enter tuşuna basıldığında da aramayı tetikler
    cityInput.addEventListener('keypress', function(e){
        if(e.key === 'Enter'){
            handleSearch();
        }
    });
    