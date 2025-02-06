class BookStore:
    def __init__(self):
        self.books={"Python Basics":500,"AI Fundamentals":800,"Data Science Guide":1000,"Machine learning book":1200}

    def get_discount(self,customer_id):
        if 1 <= customer_id <= 100:
            return 50
        elif 101 <= customer_id <= 300:
            return 30
        elif 301 <= customer_id <= 400:
            return 20
        elif 401 <= customer_id <= 500:
            return 10
        else:
            return 0

    def cal_price(self,book_name,customer_id):
        if book_name not in self.books:
            print("Invalid book name.Please try again!.")
            return

        price=self.books[book_name]
        discount=self.get_discount(customer_id)
        discounted_price=price - (price*discount / 100)

        print(f"Price of the Book is {price} MRP")
        print(f"You are eligible for a Discount of {discount}%")
        print(f"Your discounted Price for the Book is {discounted_price:.2f} MRP")

    def  start(self):
        while True:
            print("\n --------Welcome to Zampa's Bookstore--------")
            book_name=input("Enter your Book Name:").strip()
            if not book_name:
                print("Book name cannot be empty. Try again")
                continue

            try:
                customer_id=int(input("Enter your Customer ID:").strip())
                if customer_id < 1:
                    print("Invalid Customer ID. Try again!.")
                    continue
            except ValueError:
                print("Customer ID should be a valid number.Try again!.")
                continue

            self.cal_price(book_name,customer_id)

            cont=input("Do you want to continue? (yes/no): ")
            if cont!= "yes":
                print("Thank you for visiting Zampa 's Bookstore!")
                break

store = BookStore()
store.start()
                       
