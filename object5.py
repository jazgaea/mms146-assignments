class Book:
    ## attributes
    def __init__(self,n,y,p,w,aN,c):
        self.name = n
        self.year = y
        self.pages = p
        self.authorName = aN
        self.wordCount = w
        self.cover = c

    ## publishing + picking cover attribute
    def publish(self):
        self.year = '2022'
    def hard_Cover(self):
        self.cover = "hard-cover"
    def soft_Cover(self):
        self.cover = "soft-cover"
    
book1 = Book("La Historia fácil por los Tontos",'0000','300', '5000',"Chica Minuto","not selected")

print("-- starting attributes --")
print("name: " + book1.name)
print("year of publication: " + book1.year)
print("no. of pages: " + book1.pages)
print("word count: " + book1.wordCount)
print("author: " + book1.authorName)
print("cover type: " + book1.cover)
print("\n")

print("=== picking a cover type ===")
book1.hard_Cover()
if book1.cover == "hard-cover" or "soft-cover":
   print("!!! cover type has been selected")
print("\n")

print("=== publishing now ===")
book1.publish()
print("published! - " + book1.year)
print("\n")

print("-- updated attributes --")
print("name: " + book1.name)
print("year of publication: " + book1.year)
print("no. of pages: " + book1.pages)
print("word count: " + book1.wordCount)
print("author: " + book1.authorName)
print("cover type: " + book1.cover)
print("\n")