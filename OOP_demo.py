class Animal:
    #encapulation 
    __name =""
    __height= 0
    __weight = 0
    __sound = 0
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    def set_name(self,name):
        self.__name =name
    def set_height(self,height):
        self.__height =height
    def set_weight(self,weight):
        self.__weight =weight
    def set_sound(self,sound):
        self.__sound =sound
    def get_name(self):
        return self.__name
    def get_height(self):
        return str(self.__height)
    def get_sound(self):
        return self.__sound
    def get_weight(self):
        return self.__weight
    #to demonstrate polymorphism
    def get_type(self):
        print("Animal")
    def toString(self):
        return "{} is  {} cm tall and {} kilograms and says {} ".format(self.__name,self.__height,self.__weight,self.__sound)
 

cat = Animal("Black Kitty",33,10,"Purrs")
print(cat.toString())
print(cat.get_type())

"""inheritance"""
class Dog(Animal):
    __onwer = ""
    def __init__(self, name,height,weight,sound,owner):
        self.__owner =owner
        super(Dog,self).__init__(name,height,weight,sound)
    def set_owner(self,owner):
        self.__owner = owner
    def get_owner(self):
        return self.__owner
    def get_type(self):
        print("Dog")
    # def toString(self):
    #     return "{} is  {} cm tall and weighs {} kilograms and says {} and the owner is {} ".format(self.get_name(),self.get_height(),self.get_weight(),self.get_sound(),self.__owner)
    def print_name(self):
        return self.get_name()
spot = Dog("German Shephard",33,10,"woof! woof!","Ray")
print(spot.get_type())
print(spot.toString())