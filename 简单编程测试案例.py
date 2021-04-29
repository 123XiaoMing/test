# 需求：小明现在体重75kg，跑步体重减少1kg，吃饭体重增加2kg，将其封装成对象

class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 1

    def eat(self):
        self.weight += 0.5

    def __str__(self):
        return "%s现在的体重为%.1f" % (self.name,self.weight)

person_1 = Person("小明",75)
for i in range(7):
    person_1.run()
for j in range(5):
    person_1.eat()
print(person_1)

# ----
