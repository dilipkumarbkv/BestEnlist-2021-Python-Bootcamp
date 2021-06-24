class Brands:
    brand_name1 = "parle"
    brand_name2 = "hl"
    brand_name3 = "dabur"


class Products(Brands):
    prod1 = "parleG"
    prod2 = "colgate"
    prod3 = "honey"


class Popularity(Brands):
    prod1_popularity = 100
    prod2_popularity = 70
    prod3_popularity = 60


class Value(Brands):
    prod1_val = "excellent value"
    prod2_val = "Better value"
    prod3_val = "Good value"


obj1 = Products()
obj2 = Popularity()
obj3 = Value()
print(obj1.brand_name1+" is for " +obj1.prod1)
print(obj2.brand_name2+" is for " +obj1.prod2)
print(obj3.brand_name3+" is for " +obj1.prod3)
