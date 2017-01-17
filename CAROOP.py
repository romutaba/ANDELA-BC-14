class Car(object):

    # num_of_wheels = 4
    # num_of_doors = 4
    # speed = 0

    def __init__(self, name, model, type, num_of_wheels=8, num_of_doors=4):

        self.name = name
        self.model = model
        self.type = type
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        #self.wheels = Car.num_of_wheels
    
        if name is not None:
            self.name = name
        else:
            self.name = "General"
        
        if model is not None:
            self.model = model
        else:
            self.model = "GM"  
        

        if self.name == "porsche" or self.name == "Koenigsegg":
                self.num_of_doors = 2
        else: 
            return self.num_of_doors

        if self.type == "saloon":
            self.num_of_wheels = 4
        else:
            return self.num_of_wheels
    
    def is_saloon(self):
        if self.num_of_wheels < 4:
            return False
        elif self.num_of_wheels > 4:
            return False
        return True

    def drive(self, factor):
        if factor == 7:
            self.speed = 77  
        elif factor == 3:
            self.speed = 1000
        return self

porsche = Car('porsche', 'GTO', 'saloon',"10","")
print (porsche.name, porsche.model,porsche.type)
print(porsche.num_of_doors, porsche.num_of_wheels)
print(porsche.is_saloon())

#Truck = Car("","",'trailer', "", "")
# Truck = Car('FIat','99','trailer','','')
# print (Truck.name, Truck.model)
# print(Truck.num_of_wheels)
