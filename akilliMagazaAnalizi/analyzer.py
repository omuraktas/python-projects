import numpy as np # pyright: ignore[reportMissingImports]


class RetailAnalyzer():
    def __init__(self, sales):
        self.sales = sales

    def datasetSummary(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        totals = np.array([sale.total for sale in self.sales])

        print("\n--- DATASET ÖZETİ ---")
        print("Toplam işlem sayısı:", len(self.sales))
        print("Toplam gelir:", np.sum(totals))
        print("Ortalama işlem tutarı:", np.mean(totals))
        print("En düşük işlem tutarı:", np.min(totals))
        print("En yüksek işlem tutarı:", np.max(totals))

    def bestCategory(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        kategoriGeliri = {}

        kategoriCevirisi = {
            "Beauty": "Güzellik",
            "Clothing": "Giyim",
            "Electronics": "Elektronik"
        }

        for sale in self.sales:
            if sale.category not in kategoriGeliri:
                kategoriGeliri[sale.category] = 0

            kategoriGeliri[sale.category] += sale.total

        bestKategori = max(kategoriGeliri, key=kategoriGeliri.get)
        kategoriAdi = kategoriCevirisi.get(bestKategori, bestKategori)

        print("\n--- EN ÇOK GELİR GETİREN KATEGORİ ---")
        print("Kategori:", kategoriAdi)
        print("Toplam gelir:", kategoriGeliri[bestKategori])

    def ageGroup(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        yasGrup = {
            "18-25": [],
            "26-35": [],
            "36-45": [],
            "46-60": [],
            "60+": []
        }

        for sale in self.sales:
            if 18 <= sale.age <= 25:
                yasGrup["18-25"].append(sale.total)
            elif 26 <= sale.age <= 35:
                yasGrup["26-35"].append(sale.total)
            elif 36 <= sale.age <= 45:
                yasGrup["36-45"].append(sale.total)
            elif 46 <= sale.age <= 60:
                yasGrup["46-60"].append(sale.total)
            else:
                yasGrup["60+"].append(sale.total)

        print("\n--- YAŞ GRUBU ANALİZİ ---")

        for grup, harcamalar in yasGrup.items():
            if len(harcamalar) > 0:
                ortalama = np.mean(np.array(harcamalar))
                print(grup, "yaş grubu ortalama harcama:", ortalama)
            else:
                print(grup, "yaş grubunda veri yok.")

    def genderAnalysis(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        kadinHarcamalari = []
        erkekHarcamalari = []

        for sale in self.sales:
            gender = sale.gender.lower()

            if gender == "female":
                kadinHarcamalari.append(sale.total)
            elif gender == "male":
                erkekHarcamalari.append(sale.total)

        print("\n--- CİNSİYETE GÖRE HARCAMA ANALİZİ ---")

        if len(kadinHarcamalari) > 0:
            kadinOrtalama = np.mean(np.array(kadinHarcamalari))
            print("Kadın müşteri ortalama harcama:", kadinOrtalama)
        else:
            kadinOrtalama = 0
            print("Kadın müşteri verisi yok.")

        if len(erkekHarcamalari) > 0:
            erkekOrtalama = np.mean(np.array(erkekHarcamalari))
            print("Erkek müşteri ortalama harcama:", erkekOrtalama)
        else:
            erkekOrtalama = 0
            print("Erkek müşteri verisi yok.")

        if kadinOrtalama > erkekOrtalama:
            print("Kadın müşteriler bu datasette ortalama daha fazla harcama yapmış.")
        elif erkekOrtalama > kadinOrtalama:
            print("Erkek müşteriler bu datasette ortalama daha fazla harcama yapmış.")
        else:
            print("İki grubun ortalama harcaması eşit veya karşılaştırma için yeterli veri yok.")
    def enCokHarcamaYapanMusteriler(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        musteriHarcama = {}

        for sale in self.sales:
            if sale.customerID not in musteriHarcama:
                musteriHarcama[sale.customerID] = 0

            musteriHarcama[sale.customerID] += sale.total

        musteriSira = sorted(
            musteriHarcama.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n--- EN ÇOK HARCAMA YAPAN 5 MÜŞTERİ ---")

        for musteriID, toplamHarcama in musteriSira[:5]:
            print(musteriID, "→", toplamHarcama)
    
    def KatagoriRaporu(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        kategoriVeri = {}

        kategoriCeviri = {
            "Beauty": "Güzellik",
            "Clothing": "Giyim",
            "Electronics": "Elektronik"
        }

        for sale in self.sales:
            if sale.category not in kategoriVeri:
                kategoriVeri[sale.category] = []

            kategoriVeri[sale.category].append(sale.total)

        print("\n--- KATEGORİ BAZLI RAPOR ---")

        for kategori, harcamalar in kategoriVeri.items():
            harcamaVeri = np.array(harcamalar)
            kategoriAdi = kategoriCeviri.get(kategori, kategori)

            print("\nKategori:", kategoriAdi)
            print("Toplam gelir:", np.sum(harcamaVeri))
            print("Ortalama satış:", np.mean(harcamaVeri))
            print("En yüksek satış:", np.max(harcamaVeri))
            print("En düşük satış:", np.min(harcamaVeri))
            print("Satış adedi:", len(harcamaVeri))
    def kampanyaOneri(self):
        if len(self.sales) == 0:
            print("Analiz yapılacak veri yok.")
            return

        kategoriGelir = {}

        kategoriCeviri = {
            "Beauty": "Güzellik",
            "Clothing": "Giyim",
            "Electronics": "Elektronik"
        }

        for sale in self.sales:
            if sale.category not in kategoriGelir:
                kategoriGelir[sale.category] = 0

            kategoriGelir[sale.category] += sale.total

        enDusukKategori = min(kategoriGelir, key=kategoriGelir.get)
        enYuksekKategori = max(kategoriGelir, key=kategoriGelir.get)

        enDusukKategoriAdi = kategoriCeviri.get(enDusukKategori, enDusukKategori)
        enYuksekKategoriAdi = kategoriCeviri.get(enYuksekKategori, enYuksekKategori)

        print("\n--- KAMPANYA ÖNERİSİ ---")

        print(enDusukKategoriAdi, "kategorisinin toplam geliri düşük.")
        print("Bu kategori için %15 indirim kampanyası önerilir.")

        print()

        print(enYuksekKategoriAdi, "kategorisi güçlü performans gösteriyor.")
        print("Bu kategori için stok artırımı önerilir.")