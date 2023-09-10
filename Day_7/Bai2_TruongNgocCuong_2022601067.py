class Book:
    def __init__(self, title="", author="", price=""):
        self.__title = title
        self.__author = author
        self.__price = price

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        self.__author = author

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price


class SoftCoverBook(Book):
    def __init__(self, title, author, price, discount=0.0):
        super().__init__(title, author, price)
        self.__discount = discount

    def getDiscount(self):
        return self.__discount

    def setDiscount(self, discount):
        self.__discount = discount

    def calculate_discounted_price(self):
        price = super().getPrice()
        if isinstance(price, (int, float)):
            return price * (1 - self.getDiscount() / 100)
        else:
            return None


class HardCoverBook(Book):
    def __init__(self, title, author, price, weight=0.0):
        super().__init__(title, author, price)
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        self.__weight = weight

    def calculate_shipping_cost(self):
        return self.getWeight() * 15000


class BookStore:
    def __init__(self):
        self.__books = []

    def getBooks(self):
        return self.__books

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def total_revenue(self):
        total = 0
        for book in self.__books:
            total += book.getPrice()
        return total


if __name__ == "__main__":
    bookstore = BookStore()
    softcoverbook = SoftCoverBook("Sách mềm", "Tác giả A", 10000, 10)
    hardcover_book = HardCoverBook("Sách cứng", "Tác giả B", 200000, 1.5)
    bookstore.add_book(softcoverbook)
    bookstore.add_book(hardcover_book)

    discounted_price = softcoverbook.calculate_discounted_price()
    print("Giá sách mềm sau khi giảm giá:", discounted_price)

    shipping_cost = hardcover_book.calculate_shipping_cost()
    print("Phí ship đối với sách cứng:", shipping_cost)

    total_revenue = bookstore.total_revenue()
    print("Tổng doanh thu của cửa hàng:", total_revenue)