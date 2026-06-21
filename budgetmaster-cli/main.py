## Akıllı Bütce Harcama Sümülatörü(BudgetMaster CLI)
import random


## Global Değişkenlerimiz
gelirListesi=[]
harcamaListesi=[]
kategoriler = ("Yemek", "İçecek", "Ulaşım", "Kıyafet", "Fatura", "Eğitim", "Diğer")
zorunluKategoriler = {"Yemek","Ulaşım", "Fatura", "Eğitim"}



# Gerekli Fonksiyonlar
def genelMenu():
    secim = int(input("""====== BudgetMaster CLI ======
    1. Gelir Ekle
    2. Harcama Ekle
    3. Harcamaları Listele
    4. Kategori Analizi
    5. Aylık Bütçe Özeti
    6. Acil Durum Simülasyonu
    7. Tasarruf Önerisi Al
    8. Finansal Skorumu Gör
    9. Verileri Sıfırla
    0. Çıkış
    > """))
    return secim

def gelirEkle():
    gelirTuru = input("====== Gelir Türü ======\nMaaş, Borç Ödemesi, Prim, Bonus\nLütfen gelir türünüzü giriniz:").strip().lower().capitalize()
    try:
        
        gelirTutari = float(input("Lütfen gelir tutarını giriniz:"))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        gelirTutari = float(input("Lütfen gelir tutarını giriniz:"))
    gelirDekont = input("Lütfen dekont varsa (var), yoksa (yok) yazınız:")
    gelirKayit = {
        "gelirTuru": gelirTuru,
        "gelirTutari": gelirTutari,
        "dekont": gelirDekont
    }

    return gelirKayit
    

def harcamaEkle():     
    print("====== Harcama Bilgileri ======")
    harcamaAdi = input("Lütfen ne aldığınızı giriniz:").strip().lower().capitalize()
    try:
        
        harcamaTutari = float(input("Lütfen aldığnız ürünün tutarını giriniz:"))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        harcamaTutari = float(input("Lütfen aldığnız ürünün tutarını giriniz:"))
   
    print("Kategoriler:")
    for kategori in kategoriler:
        print("-", kategori)

    harcamaKatagori = input("Lütfen ürünün kategorisini giriniz: ").strip().lower().capitalize()

    if harcamaKatagori in zorunluKategoriler:
        harcamaZorunlu = "Evet"
    else:
        harcamaZorunlu = input("Yaptığınız harcama zorunlu mu? Evet/Hayır: ").strip().lower().capitalize()
    
    harcamaKayit = {
    "harcamaAdi":harcamaAdi,
    "harcamaTutari":harcamaTutari,
    "harcamaKatagori":harcamaKatagori,
    "harcamaZorunlu":harcamaZorunlu
    }
    return harcamaKayit


def harcamalariListele():
    if len(harcamaListesi) == 0:
        print("Henüz harcama eklenmedi.")
        return
        
    for harcama in harcamaListesi:
        print("-------------------")
        print("Harcama adı:", harcama["harcamaAdi"])
        print("Harcama tutarı:", harcama["harcamaTutari"])
        print("Harcama adı:", harcama["harcamaKatagori"])
        print("Harcama zorunlu mu:", harcama["harcamaZorunlu"])
        print("-------------------")
    
def katagoriAnalizi():
    if len(harcamaListesi) == 0:
        print("Henüz harcama eklenmedi.")
        return

    kategoriToplamlari = {}

    for harcama in harcamaListesi:
        kategori = harcama["harcamaKatagori"]
        tutar = harcama["harcamaTutari"]

        if kategori not in kategoriToplamlari:
            kategoriToplamlari[kategori] = 0

        kategoriToplamlari[kategori] += tutar

    print("====== Kategori Analizi ======")

    for kategori in kategoriToplamlari:
        print(kategori, ":", kategoriToplamlari[kategori], "TL")


    
def aylikButceOzeti():
    gelSum = 0
    harcamaSum = 0

    for gelir in gelirListesi:
        gelSum += gelir["gelirTutari"]

    for harcama in harcamaListesi:
        harcamaSum += harcama["harcamaTutari"]

    kalanMoney = gelSum - harcamaSum
    tasarruf = kalanMoney / gelSum * 100

    print("====== Aylık Bütçe Özeti ======")
    print(f"Toplam Gelir: {gelSum}")
    print(f"Toplam Harcama: {harcamaSum}")
    print(f"Kalan Para: {kalanMoney}")
    print(f"Tasarruf Oranı: %{tasarruf:.2f}")

    if tasarruf >= 30:
        print("Durum: Çok İyi, gelirinin önemli kısmını koruyorsun.")
    elif 20 <= tasarruf < 30:
        print("Durum: İyi, gelirinin bir kısmını koruyorsun.")
    elif 10 <= tasarruf < 20:
        print("Durum: Orta, harcamalarına dikkat etmelisin.")
    elif 0 <= tasarruf < 10:
        print("Durum: Kötü, gelirinin çoğu harcamalara gidiyor.")
    else:
        print("Durum: Çok Kötü, gelirinden fazla harcama yapmışsın.")
            
            
            
    
def acilDurumSimilasyonu():
    acilDurumlar = [
        {"olay": "Telefon ekranın kırıldı", "masraf": 2500},
        {"olay": "Bilgisayarın bozuldu", "masraf": 4000},
        {"olay": "Beklenmeyen fatura geldi", "masraf": 1200},
        {"olay": "Ani sağlık masrafı çıktı", "masraf": 1800},
        {"olay": "Ulaşım için ekstra para gerekti", "masraf": 600}
    ]

    secilenDurum = random.choice(acilDurumlar)

    gelSum = 0
    harcamaSum = 0

    for gelir in gelirListesi:
        gelSum += gelir["gelirTutari"]

    for harcama in harcamaListesi:
        harcamaSum += harcama["harcamaTutari"]

    kalanPara = gelSum - harcamaSum

    print("====== Acil Durum Simülasyonu ======")
    print("Acil durum:", secilenDurum["olay"])
    print("Gerekli para:", secilenDurum["masraf"], "TL")
    print("Senin kalan paran:", kalanPara, "TL")

    if kalanPara >= secilenDurum["masraf"]:
        print("Bu acil masrafı karşılayabiliyorsun.")
    else:
        eksikPara = secilenDurum["masraf"] - kalanPara
        print("Bu acil masrafı karşılayamıyorsun.")
        print("Eksik paran:", eksikPara, "TL")
        
def tasarrufOnerisi():
    gelSum = 0
    harcamaSum = 0
    gereksizHarcama = 0

    for gelir in gelirListesi:
        gelSum += gelir["gelirTutari"]

    for harcama in harcamaListesi:
        harcamaSum += harcama["harcamaTutari"]

        if harcama["harcamaZorunlu"] == "Hayır":
            gereksizHarcama += harcama["harcamaTutari"]

    kalanPara = gelSum - harcamaSum
    tasarrufOrani = kalanPara / gelSum * 100

    print("====== Tasarruf Önerisi ======")
    print("Toplam Gelir:", gelSum, "TL")
    print("Toplam Harcama:", harcamaSum, "TL")
    print("Kalan Para:", kalanPara, "TL")
    print("Zorunlu Olmayan Harcamalar:", gereksizHarcama, "TL")
    print(f"Tasarruf Oranı: %{tasarrufOrani:.2f}")

    if kalanPara < 0:
        print("Öneri: Gelirinden fazla harcama yapmışsın. İlk olarak zorunlu olmayan harcamaları azaltmalısın.")

    elif gereksizHarcama > gelSum * 0.3:
        print("Öneri: Gereksiz harcamaların çok yüksek. Kıyafet, içecek veya keyfi harcamaları azaltmalısın.")

    elif gereksizHarcama > gelSum * 0.1:
        print("Öneri: Bazı gereksiz harcamaların var. Bunları biraz azaltırsan daha fazla para biriktirebilirsin.")

    elif tasarrufOrani >= 30:
        print("Öneri: Çok iyi gidiyorsun. Kalan parayı birikim veya acil durum fonu için ayırabilirsin.")

    elif tasarrufOrani >= 10:
        print("Öneri: Durumun orta seviyede. Harcamalarını biraz daha kontrollü yapmalısın.")

    else:
        print("Öneri: Tasarruf oranın düşük. Günlük küçük harcamaları azaltmaya çalışmalısın.")
        
def finansalSkor():
    gelSum = 0
    harcamaSum = 0

    for gelir in gelirListesi:
        gelSum += gelir["gelirTutari"]

    for harcama in harcamaListesi:
        harcamaSum += harcama["harcamaTutari"]

    kalanPara = gelSum - harcamaSum
    tasarrufOrani = kalanPara / gelSum * 100

    if tasarrufOrani >= 30:
        skor = 90
        durum = "Çok iyi"
    elif tasarrufOrani >= 20:
        skor = 75
        durum = "İyi"
    elif tasarrufOrani >= 10:
        skor = 60
        durum = "Orta"
    elif tasarrufOrani >= 0:
        skor = 40
        durum = "Kötü"
    else:
        skor = 20
        durum = "Çok kötü"

    print("====== Finansal Skor ======")
    print("Toplam Gelir:", gelSum, "TL")
    print("Toplam Harcama:", harcamaSum, "TL")
    print("Kalan Para:", kalanPara, "TL")
    print(f"Tasarruf Oranı: %{tasarrufOrani:.2f}")
    print("Finansal Skorun:", skor, "/ 100")
    print("Durum:", durum)
    
def verileriSifirla():
    gelirListesi.clear()
    harcamaListesi.clear()
    print("Tüm gelir ve harcama verileri sıfırlandı.")

# Main kısmımız   
secim = -1
while secim != 0:
    secim = genelMenu()

    if secim == 1:
        gelirBilgileri = gelirEkle()
        gelirListesi.append(gelirBilgileri)
        print("Gelir bilgisi başarıyla eklendi. Menüye geçiliyor...")

    elif secim == 2:
        harcamaBilgileri = harcamaEkle()
        harcamaListesi.append(harcamaBilgileri)
        print("Harcamanız başarıyla eklendi. Menüye geçiliyor...")

    elif secim == 3:
        harcamalariListele()

    elif secim == 4:
        katagoriAnalizi()

    elif secim == 5:
        aylikButceOzeti()

    elif secim == 6:
        acilDurumSimilasyonu()

    elif secim == 7:
        tasarrufOnerisi()

    elif secim == 8:
        finansalSkor()

    elif secim == 9:
        verileriSifirla()

    elif secim == 0:
        print("Çıkış yapılıyor...")

    else:
        print("Geçersiz seçim yaptınız.")
    



    
    

