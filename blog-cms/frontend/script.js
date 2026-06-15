const API_URL = 'http://127.0.0.1:5000/api/posts';

document.addEventListener('DOMContentLoaded', () => {
    // Sayfa yüklendiği an veritabanındaki yazıları çek
    fetchPosts();

// Form gönderildiğinde tetiklenecek olay
document.getElementById('postForm').addEventListener('submit',createPost);
});

// GET İsteği: Yazıları API'den Çekip Ekrana Basma

async function fetchPosts(){
    const postsList = document.getElementById('postsList');

    try{
        const response =await fetch(API_URL);
        const posts =await response.json();

        if(posts.Lenght==0){
            postsList.innerHTML='<p class="loading">Henüz blog yazısı eklenmemiş. İlk yazıyı sen ekle! ✍️</p>';
            return;
        }

        postsList.innerHTML='';// Eski içeriği temizle

        postsList.innerHTML = posts.map(post => `
            <div class="post-item" style="position: relative;">
                <h3>${escapeHTML(post.title)}</h3>
                <small>📅 Yayınlanma: ${post.date_created}</small>
                <p>${escapeHTML(post.content)}</p>
                <button onclick="deletePost(${post.id})" style="background-color: #dc2626; width: auto; padding: 5px 10px; font-size: 12px; position: absolute; right: 0; top: 15px;">Sil 🗑️</button>
            </div>
        `).join('');

        } catch (error) {
        console.error('Veri çekilirken hata oluştu:', error);
        postsList.innerHTML = '<p class="loading" style="color: red;">API bağlantısı başarısız oldu! Backend çalışıyor mu?</p>';
    }
}
    // POST İsteği: Yeni Yazı Gönderme
async function createPost(e){
    e.preventDefault();// Sayfanın yenilenmesini engelliyoruz

    const titleInput=document.getElementById('title')
    const contentInput=document.getElementById('content');

    const postData={
        title: titleInput.value,
        content: contentInput.value
    };

    try{

        const response =await fetch(API_URL,{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(postData)
            });
        
            if(response.ok){
                //Formu Temizle
                titleInput.value='';
                contentInput.value='';
                // Listeyi anlık olarak güncelle
                fetchPosts();
            }else{
                const errData =await response.json();
                alert('HATA: ' + errData.message);
            }
        }catch(error){
            console.error('Yazı gönderilirken bir hata oluştu:' , error);
            alert('Yazı eklenemedi. Backend sunucunuzu kontrol ediniz');

}
}

// Güvenlik Önlemi: XSS saldırılarını engellemek için input temizleme fonksiyonu
function escapeHTML(str) {
    return str.replace(/[&<>'"]/g, 
        tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
    );
}
// DELETE İsteği: Veritabanından Yazı Silme
async function deletePost(postId) {
    if (!confirm('Bu yazıyı kalıcı olarak silmek istediğinden emin misin kanka?')) return;

    try {
        const response = await fetch(`${API_URL}/${postId}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            // Silme başarılıysa listeyi anlık olarak yenile kanka
            fetchPosts();
        } else {
            alert('Yazı silinirken bir hata oluştu!');
        }
    } catch (error) {
        console.error('Silme işleminde hata:', error);
        alert('Backend bağlantı hatası!');
    }
}




