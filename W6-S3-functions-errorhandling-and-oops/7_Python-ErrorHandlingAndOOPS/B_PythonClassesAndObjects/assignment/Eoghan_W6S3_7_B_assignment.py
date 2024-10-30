
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



