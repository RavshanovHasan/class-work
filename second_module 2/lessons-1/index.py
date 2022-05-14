# class Person:
#     species = 'Homo sapiens'

#     def __init__(self, firsname, brith_year):
#         self.name = firsname
#         self.brith_year = brith_year

#     def say_hello(self):
#         from datetime import datetime
#         return f'Hi I am {self.name}, I am {datetime.today().year - self.brith_year} years old '

        
# person1 = Person('isander', 2008)
# person2 = Person('shavkat', 2008)

# # print(person1.species, person1.name, person1. brith_year)
# # print(person2.species, person2.name,person2. brith_year)
# print(person1.say_hello(), 
# person2.say_hello())

# class Square: 
#     square = 'it is square'


#     def __init__(self, first_side):
#         self.side = first_side

#     def area(self):
#         return self.side * self.side 
    
#     def perimetr(self):
#         return self.side *  4

# sqr1 = Square(100)

# print(sqr1.area)
# print(sqr1.perimetr)
        

class Circle:

    def __init__(self, radius1):
        self.radius = radius1

    def area(self):
        return 3.14 * (self.radius ** 2 )
    
    def perimetr(self):
        return (2 * 3.14) * self.radius


sqr = Circle(1)

print(sqr.area())
print(sqr.perimetr())