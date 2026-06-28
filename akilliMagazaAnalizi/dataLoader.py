import csv
import os
from models import Sale


class DataLoader():
    def __init__(self, filePath):
        self.filePath = filePath

    def loadData(self):
        sales = []

        if not os.path.exists(self.filePath):
            print("Hata: CSV dosyası bulunamadı.")
            print("Beklenen dosya yolu:", self.filePath)
            return sales

        with open(self.filePath, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Hata: CSV dosyası boş veya başlık satırı yok.")
                return sales

            requiredColumns = [
                "Transaction ID",
                "Date",
                "Customer ID",
                "Gender",
                "Age",
                "Product Category",
                "Quantity",
                "Price per Unit",
                "Total Amount"
            ]

            for column in requiredColumns:
                if column not in reader.fieldnames:
                    print("Hata: CSV içinde eksik sütun var:", column)
                    return sales

            for row in reader:
                try:
                    if not any(row.values()):
                        continue

                    if row["Age"].strip() == "":
                        print("Yaş değeri boş olan satır atlandı:", row)
                        continue

                    if row["Total Amount"].strip() == "":
                        print("Toplam tutar değeri boş olan satır atlandı:", row)
                        continue

                    transactionID = row["Transaction ID"]
                    date = row["Date"]
                    customerID = row["Customer ID"]
                    gender = row["Gender"]
                    age = int(row["Age"])
                    category = row["Product Category"]
                    quantity = int(row["Quantity"])
                    price = float(row["Price per Unit"])
                    total = float(row["Total Amount"])

                    sale = Sale(
                        transactionID,
                        date,
                        customerID,
                        gender,
                        age,
                        category,
                        quantity,
                        price,
                        total
                    )

                    sales.append(sale)

                except ValueError:
                    print("Sayısal değeri hatalı olan satır atlandı:", row)

                except KeyError:
                    print("Eksik veri içeren satır atlandı:", row)

        return sales