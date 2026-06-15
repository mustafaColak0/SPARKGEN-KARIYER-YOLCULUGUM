const API_URL = 'http://127.0.0.1:5000/api';

        document.addEventListener('DOMContentLoaded', () => {
            // Sayfa açıldığında mevcut stokları getir
            urunleriYukle();

            //Form gönderildiğinde tetiklenecek olay
            document.getElementById('urunForm').addEventListener('submit',urunEkle)
        });

        //GET İsteği: Ürünleri API'den Çekip Tabloya Basma
        async function urunleriYukle() {
            const tbody =document.querySelector('#urunTablosu tbody');

            try{

                const response =await fetch(`${API_URL}/urunler`);
                const data = await response.json();

                tbody.innerHTML=''; // Eski verileri temizle

                if(data.length==0){
                    tbody.innerHTML ='<tr><td colspan="5" class="loading">Envanter boş. İlk ürünü ekle!</td></tr>';
                    return;
                }
                // JavaScript Array `.forEach` yapısı ile tablo satırlarını örüyoruz.
                data.forEach(urun => {
                    const row = tbody.insertRow();
                    row.innerHTML=`
                    <td>${urun.id}</td>
                    <td><strong>${escapeHTML(urun.ad)}</strong></td>
                        <td>${urun.miktar} Adet</td>
                        <td>${urun.fiyat.toFixed(2)} TL</td>
                        <td><small>${urun.tarih}</small></td>
                    `;
                });

               } catch (error) {
                console.error('Stoklar yüklenirken hata oluştu:', error);
                tbody.innerHTML = '<tr><td colspan="5" class="loading" style="color: red;">API bağlantısı başarısız! Backend ayakta mı?</td></tr>';
            }
        }
        //POST İsteği: Yeni ürün Gönderme
        async function urunEkle(e){
            e.preventDefault(); // Sayfa yenilemesini engeller.

            const urunAdiİnput =document.getElementById('urunAdi');
            const miktarInput =document.getElementById('miktar');
            const fiyatInput = document.getElementById('fiyat');

            const urunData ={
                ad:urunAdiİnput.value,
                miktar:parseInt(miktarInput.value),
                fiyat: parseFloat(fiyatInput.value)
            };
       
            try{
                const response =await fetch(`${API_URL}/urunler`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(urunData)
                });
                
                const result = await response.json();

                if(response.ok && result.durum=='basarili'){
                    // Formu sıfırla ve listeyi anlık yenile (Asenkron UX)
                    document.getElementById('urunForm').reset();
                    urunleriYukle();
                }else{
                    alert('Hata:' + result.mesaj);
                }

            }catch (error){
                console.error('Ürün eklenirken hata:', error);
                alert('API bağlantı hatası oluştu!');
            }
        }

        // XSS Koruması Güvenlik Filtresi
        function escapeHTML(str) {
            return str.replace(/[&<>'"]/g, 
                tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
            );
        }
            
       
        