import requests
import json
import pandas as pd
import os

# 1. Gerçek e-ticaret verilerini simüle eden test API'miz
API_URL = "https://fakestoreapi.com/products"

def get_products():
    """
    Bu fonksiyon uzak sunucuya (API) bağlanır ve ürün verilerini çeker.
    """
    try:
     # API'ye GET isteği gönderiyoruz
        response = requests.get(API_URL)
    # Eğer sunucu '200 OK' (Başarılı) kodu döndüyse veriyi JSON olarak alıyoruz
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[-] Sunucu hatası! Durum Kodu: {response.status_code}")
            return None
        # İnternet kopması veya yanlış URL durumunda programın çökmesini engelliyoruz
    except Exception as e:
        print(f"[-] API'ye bağlanırken hata oluştu: {e}")
        return None

def filter_by_category(products, category):
    """
    Kullanıcının seçtiği kategoriye göre ürünleri filtreler.
    Büyük/küçük harf duyarlılığını (.lower()) sıfırlayarak hata önler.
    """
    return [p for p in products if p['category'].lower() == category.lower()]

def filter_by_price_range(products, min_price, max_price):
    """
    Ürün fiyatlarını belirlenen alt ve üst sınıra göre filtreler.
    """
    return [p for p in products if min_price <= p['price'] <= max_price]


def sort_products(products, sort_by='price', reverse=False):
    """
    Ürünleri fiyata veya puana göre küçükten büyüğe (veya tam tersi) sıralar.
    """
    return sorted(products, key=lambda x: x[sort_by], reverse=reverse)


def process_catalog(products):
    """
    Pandas kütüphanesini kullanarak veriyi bir tabloya (DataFrame) dönüştürür
    ve kaç adet benzersiz kategori olduğunu analiz edip ekrana basar.
    """
    if products:
        # Gelen JSON listesini Pandas DataFrame'e çeviriyoruz (Excel tablosu gibi düşün)
        df = pd.DataFrame(products)
        print(f"\n[ANALİZ] Toplam Ürün Sayısı: {len(df)}")
        
        # Benzersiz kategorileri çekiyoruz
        categories = df['category'].unique()
        print(f"[ANALİZ] Mevcut Kategoriler: {list(categories)}\n")
        return products
    else:
        print("[-] İşlenecek veri bulunamadı.")
        return None

# Test Bölümü
def show_menu():
    '''
    Kullanıcıya seçecekleri sunan basit bir menü fonksiyonu.
    '''
    print("\n" + "="*40)
    print("\n=== E-TİCARET KATALOG YÖNETİM SİSTEMİ ===")
    print("="*40)
    print("1. Tüm Ürünleri Listele (İlk 5 Ürün)")
    print("2. Kategoriye Göre Filtrele")
    print("3. Fiyat Aralığına Göre Filtrele")
    print("4. Ürünleri Fiyata Göre Sırala")
    print("5. Sistemden Güvenli Çıkış (LOG_OUT)")
    print("="*40)
def main():
    print("[+] Api'ye bağlanılıyor, veriler çekiliyor...")
    products = get_products()

    if not products:
        print("[-] Veri tabanına bağlanılamadığı için Program sonlandırılıyor.")
        return
    
    #ilk açılışta Pandas analiz raporunu ekrana basıyoruz.
   # process_catalog(products)

    while True:
        show_menu()
        choice=input("Lütfen yapmak istediğiniz işlemi seçin (1-5): ").strip()

        if choice =="1":
            print("\n[+] İlk 5 Ürün geliştiriliyor (JSON Formatında) :")
            # json.dumps kullanarak veriyi daha okunaklı (indent=4) basıyoruz
            print(json.dumps(products[:5], indent=4,ensure_ascii=False))

        elif choice == "2":
            category = input("Filtrelemek istediğiniz kategori adını girin: ")
            filtered = filter_by_category(products, category)
            print(f"\n[+] '{category}' kategorisinde {len(filtered)} ürün bulundu:")
            for p in filtered:
                print(f" - {p['title']} ({p['price']} USD)")

        elif choice == "3":
            try:
                min_price=float(input("Minimum fiyatı girin: "))
                max_price=float(input("Maksimum fiyatı girin: "))
                filtered = filter_by_price_range(products, min_price, max_price)
                print(f"\n[+] {min_price} - {max_price} USD arası fiyatlandırılmış {len(filtered)} ürün bulundu:")
                for price in filtered:
                    print(f" - {price['title']} ({price['price']} USD)")
            except ValueError:
                print("[-] Hata: Lütfen geçerli bir sayısal fiyat girin!")

        elif choice == "4":
            reverse=input ("Pahalıdan ucuza mı sıralamak istersiniz? (E/H): ").lower()
            is_reverse = True if reverse == 'e' else False
            sorted_products = sort_products(products, sort_by='price', reverse=is_reverse)

            print("\n[+] Fiyata göre sırlanmış ürün listesi")
            for product in sorted_products:
                print(f" - {product['title']} ({product['price']} USD)")

        elif choice == "5":
           print("\n[+] E-Ticaret veri bağlantısı kesildi. Güvenli çıkış yapıldı. Görüşmek üzere kanka!")
           break
            
        else:
            print("[-] Geçersiz seçim! Lütfen 1 ile 5 arasında bir değer girin.")
        if choice in ["1", "2", "3", "4"]:
            print("\n" + "-"*40)
            input("Devam etmek ve ekranı temizlemek için ENTER'a basın...")
            os.system('cls')  # Kullanıcı Enter'a bastığı an ekran temizlenir ve taze menü gelir!

# ---- PROGRAMIN ATEŞLENME NOKTASI ----
if __name__ == "__main__":
    main()