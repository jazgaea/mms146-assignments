class Table:
  def __init__(self, s, m, h, w, g):
    self.size = s
    self.material = m
    self.height = h
    self.weight = w
    self.glass = g

  def remove_glass(self):
    self.glass = "glass removed."


#Let's assign the attributes to two objects
table1 = Table("large", "Metal", "1 meter", "20 KG", "No glass")
table2 = Table("small", "Wood", "0.50 meter", "15 KG", "With glass")

print ("table1 is made of " + table1.material)
print ("table2 is " + table2.height + " tall.")

print ("table2 is " + table2.glass)
table2.remove_glass()
print ("table2 has now its " + table2.glass)
