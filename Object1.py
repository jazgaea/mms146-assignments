class Cabinet:
    def __init__(self, s, c, ht, m, sh):
        self.size = s
        self.color = c
        self.handleType = ht
        self.material = m
        self.shelves = sh
    
  #Let's Repaint the Cabinet!
    def change_Color(self, c):
        self.color = c
   
  #For Opening and closing the cabinet
    def open_shelf(self, sh):
        self.shelves = "Shelf is opened."
  
    def close_shelf(self, sh):
        self.shelves = "Shelf is closed."
    
  #changing the handles
    def change_handles(self, ht):
        self.handleType = ht
    
 #Let's experiment by opening the shelf, adding an item, then closing it again.
  
    def add_item(self, sh):
        self.shelves = open_shelf + "You added an item" + close_shelf
    
  #Okay, let's start reviewing our code! 
  #Our Cabinet is 5 meters tall, paint is dark brown, handles are gold, made of narra, and all shelves are closed.

cabinet1 = Cabinet("5 meters", "Dark Brown", "Gold", "Narra", "Shelf is closed.")
  
  #Let's repaint it to pink.
print ("I don't like a " + cabinet1.color + " cabinet")
cabinet1.change_Color("pink")
print ("let's paint it to " + cabinet1.color)
