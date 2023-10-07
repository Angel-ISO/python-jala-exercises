from datetime import datetime

class IceCreamShop:
    def __init__(self):
        self.vanilla_initial = 0
        self.peach_initial = 0
        self.passion_fruit_initial = 0
        self.vanilla_stock = 0
        self.peach_stock = 0
        self.passion_fruit_stock = 0
        self.vanilla_expiration = datetime(2023, 6, 29)
        self.peach_expiration = datetime(2023, 6, 30)
        self.passion_fruit_expiration = datetime(2023, 6, 30)
    
    def input_initial_stock(self):
        self.vanilla_initial = int(input("Enter the initial quantity of vanilla ice cream: "))
        self.peach_initial = int(input("Enter the initial quantity of peach ice cream: "))
        self.passion_fruit_initial = int(input("Enter the initial quantity of passion fruit ice cream: "))
    
    def input_current_stock(self):
        self.vanilla_stock = int(input("Enter the current quantity of vanilla ice cream: "))
        self.peach_stock = int(input("Enter the current quantity of peach ice cream: "))
        self.passion_fruit_stock = int(input("Enter the current quantity of passion fruit ice cream: "))
    
    def need_to_restock(self, flavor, current_stock, initial_stock, threshold=0.5):
        today = datetime.today()
        expiration_date = getattr(self, f"{flavor}_expiration")
        if current_stock < initial_stock * threshold and today >= expiration_date:
            return True
        else:
            return False
    
    def check_stock_status(self):
        for flavor in ["vanilla", "peach", "passion_fruit"]:
            current_stock = getattr(self, f"{flavor}_stock")
            initial_stock = getattr(self, f"{flavor}_initial")
            if self.need_to_restock(flavor, current_stock, initial_stock):
                print(f"Buy more {flavor} ice cream.")
            else:
                print(f"Don't need to buy more {flavor} ice cream.")

heladeria = IceCreamShop()
heladeria.input_initial_stock()
heladeria.input_current_stock()
heladeria.check_stock_status()
