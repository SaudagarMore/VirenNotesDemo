import datetime

class Products:
    myproduct = {}          # {name : price}
    mycartlist = []         # [(name, price, qty)]
    dailysales = "daily_sales.txt"

    def __init__(self, key, value):
        Products.myproduct.update({key: value})

    def getProducts(self):
        print("Product List:")
        for p, pr in Products.myproduct.items():
            print("Product Name:", p, "Product Price:", pr)
        print("------------------------------------------")

    # -------------------- BILL APP --------------------
    def ProductBillApp(self):
        print("----------- Product Bill App --------")
        while True:
            print("\nSelect choice:")
            print("1. Add items to cart")
            print("2. Generate Final Bill")
            print("3. Save Invoice")
            print("4. Daily Sales")
            print("0. Exit")

            choice = int(input("Enter your choice: "))

            # ---------------- ADD TO CART ----------------
            if choice == 1:
                pname = input("Enter Product Name: ")

                if pname in Products.myproduct:
                    price = Products.myproduct[pname]

                    qty = int(input("Enter Quantity: "))
                    Products.mycartlist.append((pname, price, qty))
                    print("Item added to cart!")
                else:
                    print("Product not found!")

            # ---------------- FINAL BILL ----------------
            elif choice == 2:
                self.generateBill()

            # ---------------- SAVE INVOICE ----------------
            elif choice == 3:
                total = self.generateBill(show=False)
                self.saveInvoice(total)

            # ---------------- DAILY SALES ----------------
            elif choice == 4:
                pass
              #self.dailySales()

            elif choice == 0:
                print("Exiting Program...")
                exit(0)

            else:
                print("Invalid choice!")

    # ==========================================================
    #                 FINAL BILL FUNCTION
    # ==========================================================
    def generateBill(self, show=True):
        gst_percent = 12  # fixed GST for all products
        total_amount = 0
        total_gst = 0

        if show:
            print("\n-------------- FINAL BILL --------------")

        for (name, price, qty) in Products.mycartlist:
            gst_amount = (price * gst_percent / 100) * qty
            item_total = (price * qty) + gst_amount

            total_gst += gst_amount
            total_amount += item_total

            if show:
                print(f"{name} x {qty} -> {item_total:.2f}  (GST: {gst_amount:.2f})")

        if show:
            print("-----------------------------------------")
            print(f"Total GST: {total_gst:.2f}")
            print(f"Grand Total: {total_amount:.2f}")
            print("-----------------------------------------")

        return total_amount

    # ==========================================================
    #                 SAVE INVOICE
    # ==========================================================
    def saveInvoice(self, total):
        filename = f"invoice_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write("--------- INVOICE ----------\n")
            for name, price, qty in Products.mycartlist:
                f.write(f"{name} x {qty} -> Rs {price * qty}\n")
            f.write("-----------------------------\n")
            f.write(f"Total Amount: Rs {total}\n")

        # Save to daily sales file
        with open(Products.dailysales, "a") as f:
            f.write(f"{datetime.date.today()} {total}\n")

        print(f"Invoice Saved: {filename}")

# ---------------- MAIN PROGRAM ----------------
for j in range(2):
    pname = input("Enter Product Name: ")
    price = int(input("Enter Product Price: "))
    p1 = Products(pname, price)

p1.getProducts()
p1.ProductBillApp()