class Restaurant:
    def __init__(self):
        self.menu={
            "Pizza":200,
            "Burger":120,
            "Pasta":150,
            "Sandwich":100,
            "Coffee":80
        }
        self.order={}
    def show_menu(self):
        print("\nMenu")
        for item in self.menu:
            print(item,"- Rs",self.menu[item])
    def take_order(self):
        while True:
            item=input("\nEnter item name(or type done):")
            if item=="done":
                break
            if item in self.menu:
                qty=int(input("Enter quantity:"))
                if item in self.order:
                    self.order[item]=self.order[item]+qty
                else:
                    self.order[item]=qty
            else:
                print("Item not in menu")
    def show_bill(self):
        if len(self.order)==0:
            print("\nNo items ordered")
            return
        print("\nYour Bill")
        total=0
        for item in self.order:
            price=self.menu[item]
            qty=self.order[item]
            cost=price*qty
            print(item,"|qty:",qty,"|price:",price,"|cost:",cost)
            total=total+cost
        print("Total Bill:",total)

r=Restaurant()

r.show_menu()
r.take_order()
r.show_bill()
