"""
from study_class_person import Person
man = Person("宇佐美")
man.who()
print(man.__name)
"""

from study_class_goods import Goods
shoes = Goods("dream", 6800)
print(shoes.name)
shoes.name = "dream 8"
print(shoes.name)
print(shoes.price)
shoes.price = 7200
