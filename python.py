import math  

class Circle: 
    def __init__(self,radius):   
        self.radius = radius 
        

    def calc_area(self): 
        return (self.radius*self.radius)*math.pi  
    
    def circumference(self):  
        return(2 * self.radius)*math.pi    
    
    


users_choice = int(input("Enter 1 to calculate AREA\nEnter 2 to calculate CIRCUMFERENCE\nEnter here "))
if users_choice == 1:
    r = int(input("Enter radius in cm: ")) 
    
    area_Obj = Circle(r) 
    print("Area of Circle is: ", area_Obj.calc_area(), " cm squared") 

elif users_choice == 2:
    r = int(input("Enter radius in cm: ")) 
    
    Circumference_Obj = Circle(r) 
    print("Circumference of Circle is: ", Circumference_Obj.circumference(), " cm") #----------2

else:
    print("Option not available")

