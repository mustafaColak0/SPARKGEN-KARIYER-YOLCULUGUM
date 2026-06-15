document.addEventListener('DOMContentLoaded', () => {
    const feedbackForm=document.getElementById('feedbackForm');
    const responseMessage=document.getElementById('responseMessage');
    const satisfactionLevel=document.getElementById('satisfactionLevel');
    const satisfactionValue=document.getElementById('satisfactionValue');

    // 1. Dinamik Etkileşim: Slider kaydırıldıkça ekrandaki sayıyı anlık güncelle
    satisfactionLevel.addEventListener('input', (e) => {
        satisfactionValue.textContent = e.target.value;
    });

    // 2. Form Gönderilme Olayı (Submit Event)
    feedbackForm.addEventListener('submit', async (e) => {
        e.preventDefault(); // Sayfa yenilenmesini engelle

    //Elementleri ve butons durumunu yakala
    const submitBtn = document.getElementById('submitBtn');
    const nameInput = document.getElementById('userName');
    const emailInput = document.getElementById('userEmail');
    const typeSelect = document.getElementById('feedbackType');
    const messageInput = document.getElementById('feedbackMessage');

    // Regex: Temel E-posta kontrol şablonu
    const emailRegex=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    // 3. Katman: Frontend Validasyon Kontrolleri (Kullanıcı Deneyimi UX)
        if (nameInput.value.trim().length < 2) {
            showResponse('Ad Soyad alanı en az 2 karakter olmalıdır!', 'error');
            return;
        }

        if (!emailRegex.test(emailInput.value.trim())) {
            showResponse('Lütfen geçerli bir e-posta adresi giriniz!', 'error');
            return;
        }

        if (messageInput.value.trim().length < 10) {
            showResponse('Mesajınız çok kısa! Lütfen en az 10 karakter yazın.', 'error');
            return;
        }

        // Gönderiliyor Durumu (Butonu kilitle ve yazıyı değiştir)
        submitBtn.disabled = true;
        submitBtn.textContent = 'Gönderiliyor... ⏳';

        // Backend'e paketlenecek veri objesi
        const formData = {
            ad: nameInput.value.trim(),
            email: emailInput.value.trim(),
            tur: typeSelect.value,
            mesaj: messageInput.value.trim(),
            memnuniyet: parseInt(satisfactionLevel.value)
        };

        // 4. Katman: HTTP POST İsteği (Fetch API)
        try {
            const response = await fetch('http://127.0.0.1:5000/submit-feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok && result.status === 'success') {
                // Başarılı senaryo
                showResponse(result.message, 'success');
                feedbackForm.reset(); // Formu temizle
                satisfactionValue.textContent = '3'; // Slider değerini sıfırla
            } else {
                // Sunucudan dönen validasyon hatası senaryosu
                showResponse(result.message || 'Bir hata oluştu!', 'error');
            }

        } catch (error) {
            console.error('Bağlantı Hatası:', error);
            showResponse('Backend sunucusuna bağlanılamadı! Sunucu ayakta mı?', 'error');
        } finally {
            // Her halükarda butonu eski haline getir
            submitBtn.disabled = false;
            submitBtn.textContent = 'Geri Bildirim Gönder 🚀';
        }
    });

    // Mesaj gösterme fonksiyonu
    function showResponse(text, type) {
        responseMessage.textContent = text;
        responseMessage.className = ''; // Eski sınıfları temizle
        
        if (type === 'success') {
            responseMessage.classList.add('success-msg');
        } else {
            responseMessage.classList.add('error-msg');
        }
        
        // Gizlilik sınıfını kaldırarak ekranda göster
        responseMessage.classList.remove('hidden');
    }
});
