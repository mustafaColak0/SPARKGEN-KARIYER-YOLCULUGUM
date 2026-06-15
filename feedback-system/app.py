from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)

# Ön yüzün (Frontend) lokalden istek atabilmesi için CORS'u açıyoruz
CORS(app)

DATA_FILE ='feedback_data.json'

# API ENDPOINT: Geri Bildirim Al ve JSON Dosyasına Yaz (POST)
@app.route('/submit-feedback', methods=['POST'])

def submit_feedback():
    try:
        data =request.get_json()
        # 1. Katman: Backend Validasyon Kontrolü (Siber Güvenlik Duvarı)
        if not data or 'ad' not in data or 'email' not in data or 'mesaj' not in data:
            return jsonify({'status': 'error', 'message': 'Eksik veri gönderildi!'}), 400
            
        if len(data['ad'].strip()) < 2:
            return jsonify({'status': 'error', 'message': 'Ad Soyad en az 2 karakter olmalıdır!'}), 400
            
        if len(data['mesaj'].strip()) < 10:
            return jsonify({'status': 'error', 'message': 'Mesaj alanı en az 10 karakter olmalıdır!'}), 400
            
         # Veriye zaman damgası (Timestamp) ekliyoruz
        data['tarih'] =datetime.now().strftime('%y-%m-%d %H:%M')

        # 2. Katman: Dosya Okuma/Yazma Yönetimi (Persistence Layer)
        feedback_list= []

        # Eğer dosya zaten varsa eski verileri oku
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                try:
                    feedback_list =json.load(file)
                except json.jsonDecodeError:
                # Dosya bozuk veya boşsa boş liste ile devam et
                    feedback_list = []
        
        # Yeni geri bildirimi listeye ekle
        feedback_list.append(data)

        ## Listeyi tekrar JSON dosyasına yaz (Kalıcı hale getir)
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(feedback_list, file, ensure_ascii=False, indent=4)
            
        return jsonify({'status': 'success', 'message': 'Geri bildiriminiz başarıyla sisteme kaydedildi! 🎉'}), 201

    except Exception as e:
        # Sunucu tarafında beklenmeyen bir hata oluşursa yakala
        return jsonify({'status': 'error', 'message': f'Sunucu Hatası: {str(e)}'}), 500

# BONUS ENDPOINT: Yönetici Paneli İçin Tüm Geri Bildirimleri Listele (GET)
@app.route('/admin/feedbacks', methods=['GET'])
def get_feedbacks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            try:
                data=json.load(file)
                return jsonify(data), 200
            except:
                    return jsonify([]), 200
    return jsonify([]), 200

# ADMIN ROTASI: Gelen Tüm Geri Bildirimleri JSON Olarak Listele (GET)
@app.route('/admin/feedbacks', methods=['GET'])
def list_feedbacks():
    try:
        # Eğer dosya varsa oku ve içindeki listeyi dön
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                try:
                    feedbacks = json.load(file)
                    return jsonify(feedbacks), 200
                except json.JSONDecodeError:
                    return jsonify([]), 200 # Dosya boş veya bozuksa boş liste dön
                    
        return jsonify([]), 200 # Dosya henüz oluşmadıysa boş liste dön

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Hata: {str(e)}'}), 500

if __name__ == '__main__':
    # Lokal sunucumuzu 5000 portunda çalıştırıyoruz
    app.run(debug=True, port=5000)