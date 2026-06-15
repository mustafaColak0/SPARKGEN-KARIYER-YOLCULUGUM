let clickData = [];
let mouseData = [];
let totalClick = 0;
let totalDistance = 0;
let lastMousePosition = { x: 0, y: 0 };

document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("heatmap-container");
    const clickCounter = document.getElementById("click-counter");
    const distanceCounter = document.getElementById("mouse-distance"); 

    //  1. TIKLAMA KOORDİNATLARINI YAKALAMA
    container.addEventListener("click", function(e) {
        const rect = container.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        clickData.push({ x: x, y: y, timestamp: Date.now() });
        totalClick++; 

        // Arayüzü güncelleme
        clickCounter.textContent = "Toplam Tık: " + totalClick;

        CreateHeatPoint(x, y);
    }); 

    // 🖱️ 2. MOUSE HAREKETLERİNİ VE MESAFEYİ ÖLÇME
    container.addEventListener("mousemove", function(e) {
        const rect = container.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        if (lastMousePosition.x !== 0) {
            
            const distance = Math.sqrt(Math.pow(x - lastMousePosition.x, 2) + Math.pow(y - lastMousePosition.y, 2));
            totalDistance += distance;
            
            distanceCounter.textContent = "Mouse Mesafesi: " + Math.round(totalDistance) + "px";
        }

        lastMousePosition = { x: x, y: y };
        mouseData.push({ x: x, y: y, timestamp: Date.now() });
    });

    // 📊 3. DOCK BUTONLARINI AKTİF ETME (
    document.getElementById("show-heatmap").addEventListener("click", showHeatmap);
    document.getElementById('clear-data').addEventListener('click', clearData);
}); 

// Ekranda ısı efekti oluşturma fonksiyonu
function CreateHeatPoint(x, y) {
    const overlay = document.getElementById("heatmap-overlay");
    const point = document.createElement("div");
    point.classList.add("heat-point");
    point.style.left = x + "px";
    point.style.top = y + "px";
    point.style.width = '30px';
    point.style.height = '30px';

    point.style.background = 'radial-gradient(circle, rgba(255,0,0,0.9) 0%, rgba(255,255,0,0.5) 60%, transparent 100%)';
    
    overlay.appendChild(point);
    setTimeout(() => point.remove(), 1200);
}

// Analiz Özetini Gösteren Fonksiyon
function showHeatmap() {
    if (clickData.length === 0) {
        alert("Henüz tıklama verisi yok! Lütfen sayfada tıklayın.");
        return;
    }
    const lastClick = clickData[clickData.length - 1];
    alert("[📊] Analiz Özeti:\n\n" + 
          '• Toplam Tıklama Sayısı: ' + clickData.length + '\n' +
          '• Toplam Mouse Gezinme Mesafesi: ' + Math.round(totalDistance) + ' px\n' +
          '• En Son Tıklanan Lokasyon: X: ' + Math.round(lastClick.x) + ' | Y: ' + Math.round(lastClick.y));
}

// Verileri sıfırlama fonksiyonu
function clearData() {
    clickData = [];
    mouseData = [];
    totalClick = 0;
    totalDistance = 0;
    lastMousePosition = { x: 0, y: 0 };
    
    document.getElementById("click-counter").textContent = "Toplam Tık: 0";
    document.getElementById("mouse-distance").textContent = "Mouse Mesafesi: 0px";
    document.getElementById('heatmap-overlay').innerHTML = '';

    alert("Tüm veriler sıfırlandı!");
}