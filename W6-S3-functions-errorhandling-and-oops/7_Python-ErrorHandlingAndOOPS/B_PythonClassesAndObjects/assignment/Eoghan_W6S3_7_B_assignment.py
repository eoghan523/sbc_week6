
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

#Function to update the cars year
def update_year(self, new_year):
        # Sets the private attribute __year to new_year
        self.__year = new_year

 # Function to get year
def get_year(self):
    # Returns the current year of the car
    return self.__year

 # Function to set the year attribute.
def set_year(self, new_year):
        # Updates the car's year to new_year
        self.__year = new_year

  #Function to delete car objects
def __del__(self):
        # Prints a message indicating the car object is being deleted
        print(f"The car {self.make} {self.model} has been deleted.")


# ================   Inheritance with ElectricCar subclass ================================= #

# ElectricCar inherits from Car and adds additional functionality
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Initialize the parent class with make, model, and year attributes. It also adds in the additional attribute of battery_size only for the eletric car class.
        super().__init__(make, model, year) #super() is a Python function that allows a class to access methods and properties from its parent class. 
        self.battery_size = battery_size  # Defining additional attribute for battery size

   # Function to display electric car details, including battery_size
def display_info(self):
    # Calls the display_info method from the parent Car class. This also prints the car's make, model, and year of the existing car class whilst also also adding the inheritted attributes of Electric_car. 
    super().display_info()  
    # An f string that prints the battery size of the electric car in kilowatt-hours (kWh). This attribute is specific to electric vehicles.
    print(f"Battery size: {self.battery_size} kWh")