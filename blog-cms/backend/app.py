from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

from langsmith import expect 

app = Flask(__name__)

#Cors hatasını engelleme
CORS(app)

# SQLite Veritabanı Ayarı
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ADIM 2: Veri Modeli (Database Table)

class BlogPost(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    content=db.Column(db.Text, nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date_created': self.date_created.strftime("%Y-%m-%d %H:%M:%S")
    }

# API ENDPOINT 1: Tüm Yazıları Getir (GET)
@app.route('/api/posts', methods=['GET'])
def get_posts():
    try:
        posts = BlogPost.query.order_by(BlogPost.date_created.desc()).all()
        return jsonify([post.to_dict() for post in posts]),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API ENDPOINT 2: Yeni Yazı Ekle (POST)
@app.route('/api/posts', methods=['POST'])
def create_post():
        data = request.get_json()
        if not data or 'title' not in data or 'content' not in data:
            return jsonify({"message": "Başlık ve içerik alanları boş olamaz!"}), 400
        
        try:
             new_post=BlogPost(title=data['title'], content=data['content'])
             db.session.add(new_post)
             db.session.commit()
             return jsonify({"message": "Yazı başarıyla eklendi!", "post": new_post.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API ENDPOINT 3: Belirli Bir Yazıyı Sil (DELETE)
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        # Veritabanında o ID'ye sahip yazıyı bul, yoksa 404 fırlat
        post = BlogPost.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": f"{post_id} ID'li yazı başarıyla silindi!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
     
#Tabloları otomatik yarat ve ayağa kaldır

if __name__ == '__main__':
     with app.app_context():
          db.create_all() # Veritabanı yoksa otomatik oluşturur
     app.run(debug=True,port=5000)
