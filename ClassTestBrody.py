class Recipe:
    def __init__(self, tsp1, tsp2, tsp3, tsp4, name):
        self.spice1=tsp1
        self.spice2=tsp2
        self.spice3=tsp3
        self.spice4=tsp4
        self.name=name

    def extract(self):
        #servo
        print("extracting")

recipelist = []


recipelist.append(Recipe(1,2,2,2,"Lasagna"))

recipelist.append(Recipe(1,2,3,2,"Beef"))

recipelist.append(Recipe(1,5,2,2,"pORK"))

recipelist.append(Recipe(4,2,2,4,"Chicken"))


for obj in recipelist:
    print(obj.name)


# Lasagna, 0
# Beef, 1
# pORK, 2
# Chicken, 3
# 

ab=recipelist[1] #gets the amount that is set for each spice for Beef Recipe
a=1
# for obj in recipelist:
#     if obj.name == "pORK":
#         print("ooo")
