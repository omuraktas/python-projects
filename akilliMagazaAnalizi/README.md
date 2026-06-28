# Kaggle Verisiyle Akıllı Mağaza Analiz Sistemi

## Projenin Amacı

Bu projenin amacı Kaggle’dan alınan gerçek bir satış veri setini kullanarak Python ile terminalde çalışan bir mağaza analiz sistemi geliştirmektir.

Projede OOP, CSV dosyası okuma, liste kullanımı, dictionary kullanımı ve NumPy ile temel istatistik hesaplama işlemleri yapılmıştır.

## Kullanılan Dataset

Projede Kaggle üzerinde bulunan Retail Sales Dataset kullanılmıştır.

Dataset içinde şu sütunlar yer almaktadır:

* Transaction ID
* Date
* Customer ID
* Gender
* Age
* Product Category
* Quantity
* Price per Unit
* Total Amount

Bu sütunlar satış işlemlerini, müşteri bilgilerini, ürün kategorilerini ve toplam satış tutarlarını analiz etmek için kullanılmıştır.

## Kullanılan Python Konuları

Bu projede kullanılan temel Python konuları şunlardır:

* Class yapısı
* Object Oriented Programming
* CSV dosyası okuma
* Liste kullanımı
* Dictionary kullanımı
* NumPy ile temel istatistik hesaplama
* Terminal menüsü oluşturma
* Hata kontrolü

## OOP Sınıf Yapısı

Projede 3 ana sınıf kullanılmıştır.

### Sale

Sale sınıfı bir satış işlemini temsil eder. CSV dosyasındaki her satır program içinde bir Sale nesnesine dönüştürülür.

Sale sınıfı şu bilgileri tutar:

* transaction_id
* date
* customer_id
* gender
* age
* category
* quantity
* price
* total

Ayrıca satış tutarına göre düşük, orta veya yüksek değerli satış segmenti belirleyebilir.

### DataLoader

DataLoader sınıfı CSV dosyasını okur. Her satırı Sale nesnesine çevirir ve tüm satışları liste halinde döndürür.

Bu sayede analiz sınıfı doğrudan CSV dosyasıyla uğraşmaz.

### RetailAnalyzer

RetailAnalyzer sınıfı satış listesi üzerinden analiz yapar.

Bu sınıf toplam gelir, ortalama satış, kategori analizi, yaş grubu analizi, cinsiyet analizi, müşteri harcaması ve kampanya önerisi gibi işlemleri gerçekleştirir.

## Yapılan Analizler

Projede yapılan analizler şunlardır:

1. Dataset özeti
2. En çok gelir getiren kategori analizi
3. Yaş grubu analizi
4. Cinsiyete göre harcama analizi
5. En çok harcama yapan müşteriler
6. Kategori bazlı rapor
7. Kampanya önerisi

## Elde Edilen Sonuçlar

Program, satış verilerini okuyarak toplam işlem sayısını, toplam geliri, ortalama işlem tutarını, en düşük ve en yüksek satış tutarını hesaplamaktadır.

Ayrıca ürün kategorilerine göre gelirleri karşılaştırmakta, yaş gruplarına göre ortalama harcamaları göstermekte ve kadın-erkek müşterilerin ortalama harcamalarını analiz etmektedir.

Müşteri bazlı analizde en çok harcama yapan ilk 5 müşteri listelenmektedir.

Kategori raporunda her kategori için toplam gelir, ortalama satış, en yüksek satış, en düşük satış ve satış adedi gösterilmektedir.

Kampanya önerisi bölümünde ise en düşük gelir getiren kategori için indirim önerisi, en yüksek gelir getiren kategori için stok artırımı önerisi yapılmaktadır.

## Geliştirme Önerileri

Proje ileride şu şekilde geliştirilebilir:

* Pandas kütüphanesi eklenebilir.
* Grafiklerle görselleştirme yapılabilir.
* Aylık satış analizi eklenebilir.
* Tarihe göre gelir değişimi incelenebilir.
* Makine öğrenmesi ile satış tahmini yapılabilir.
* Kullanıcı arayüzü geliştirilebilir.

## Sonuç

Bu proje sayesinde gerçek bir Kaggle datası Python ile okunmuş, OOP mantığıyla sınıflara ayrılmış ve NumPy kullanılarak temel satış analizleri yapılmıştır.

Proje, terminal üzerinden çalışan basit ama kullanışlı bir mağaza analiz sistemi olarak hazırlanmıştır.
