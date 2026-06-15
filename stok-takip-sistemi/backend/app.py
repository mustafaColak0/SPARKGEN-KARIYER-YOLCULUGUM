from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app =Flask(__name__)

#Replit yerine lokal çalışacağımız için CORS yönetimini direkt açıyoruz
CORS(app)

# Veritabanı yerine RAM üzerinde tutulacak geçici stok listesi
stok_list =[
    {'id': 1, 'ad': 'Kablosuz Mouse', 'miktar': 45, 'fiyat': 350.0, 'tarih': '2026-06-14 18:30'},
    {'id': 2, 'ad': 'Mekanik Klavye', 'miktar': 12, 'fiyat': 1200.0, 'tarih': '2026-06-14 18:35'}
]

# API ENDPOINT 1: Tüm Ürünleri Listele (GET)
@app.route('/api/urunler',methods=['GET'])
def get_urunler():
    return jsonify(stok_list),200

# API ENDPOINT 1: Yeni Ürün Ekle (POST)
@app.route('/api/urunler',methods=['POST'])
def urun_ekle():
    data=request.get_json()

    #Validosyon kontrolü (Boş veri gitmesin)
    if not data or 'ad' not in data or 'miktar' not in data or 'fiyat' not in data:
        return jsonify({'durum': 'hata', 'mesaj': 'Lütfen tüm alanları doldurun!'}), 400
        
    try:
        # Dinamik ID oluşturma
        yeni_id=stok_list[-1]['id'] + 1 if stok_list else 1

        yeni_urun={
            'id':yeni_id,
            'ad':data['ad'],
            'miktar': int(data['miktar']),
            'fiyat': float(data['fiyat']),
            'tarih':datetime.now().strftime('%Y-%m-%d %H:%M')
        }

        stok_list.append(yeni_urun)
        return jsonify({'durum': 'basarili', 'urun': yeni_urun}), 201
        
    except Exception as e:
        return jsonify({'durum': 'hata', 'mesaj': str(e)}), 500

if __name__ == '__main__':
    # Lokal sunucumuzu 5000 portunda ayağa kaldırıyoruz
    app.run(debug=True, port=5000)