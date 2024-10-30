
#class definition
class car:
    def __init__(self, make, model, year): #This line of code initialises the Car Object, make, model and year.
        self.make = make    #Defining attribute of make
        self.model = model  #Defining attribute of model
        self.__year = year  #Defining the car year 
    

#Function to display car details
def display_info(self):
    #prints f string function calling the obects under the car class 
    print(f"Car details: {self.make} {self.model}, year: {self.__year}")

    
