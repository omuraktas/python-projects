from dataLoader import DataLoader
from analyzer import RetailAnalyzer


def showMenu():
    print("\n========== AKILLI MAĞAZA ANALİZ SİSTEMİ ==========")
    print("1 - Dataset özetini göster")
    print("2 - En çok gelir getiren kategoriyi göster")
    print("3 - Yaş grubu analizi yap")
    print("4 - Cinsiyete göre harcama analizi yap")
    print("5 - En çok harcama yapan müşterileri göster")
    print("6 - Kategori bazlı rapor oluştur")
    print("7 - Kampanya önerisi üret")
    print("0 - Çıkış")


def main():
    filePath = "data/retail_sales_dataset.csv"

    loader = DataLoader(filePath)
    sales = loader.loadData()

    if len(sales) == 0:
        print("Veri yüklenemedi. Program kapatılıyor.")
        return

    analyzer = RetailAnalyzer(sales)

    while True:
        showMenu()

        secim = input("Seçiminizi girin: ")

        if secim == "1":
            analyzer.datasetSummary()

        elif secim == "2":
            analyzer.bestCategory()

        elif secim == "3":
            analyzer.ageGroup()

        elif secim == "4":
            analyzer.genderAnalysis()

        elif secim == "5":
            analyzer.enCokHarcamaYapanMusteriler()

        elif secim == "6":
            analyzer.KatagoriRaporu()

        elif secim == "7":
            analyzer.kampanyaOneri()

        elif secim == "0":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Hatalı seçim yaptınız. Lütfen tekrar deneyin.")


main()