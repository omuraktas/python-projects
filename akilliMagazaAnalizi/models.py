class Sale():
    def __init__(self, transactionID, date, customerID, gender, age, category, quantity, price, total):
        self.transactionID = transactionID
        self.date = date
        self.customerID = customerID
        self.gender = gender
        self.age = age
        self.category = category
        self.quantity = quantity
        self.price = price
        self.total = total

    def getSegment(self):
        if self.total < 500:
            return "Düşük değerli satış"
        elif self.total < 1000:
            return "Orta değerli satış"
        else:
            return "Yüksek değerli satış"

    def showInfo(self):
        print("--------------------------------")
        print("İşlem ID:", self.transactionID)
        print("Tarih:", self.date)
        print("Müşteri ID:", self.customerID)
        print("Cinsiyet:", self.gender)
        print("Yaş:", self.age)
        print("Kategori:", self.category)
        print("Adet:", self.quantity)
        print("Birim Fiyat:", self.price)
        print("Toplam Tutar:", self.total)
        print("Satış Segmenti:", self.getSegment())