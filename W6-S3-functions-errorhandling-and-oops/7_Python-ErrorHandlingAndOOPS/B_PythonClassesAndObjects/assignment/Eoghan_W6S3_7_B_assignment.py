# Class definition
class Car:
    def __init__(self, make, model, year):
        self.make = make    # Defining attribute of make
        self.model = model  # Defining attribute of model
        self.__year = year  # Defining the car year 

    # Function to display car details
    def display_info(self):
        print(f"Car details: {self.make} {self.model}, year: {self.__year}")

    # Function to update the car's year
    def set_year(self, new_year):
        self.__year = new_year  # Updates the car's year to new_year

    # Function to get the year
    def get_year(self):
        return self.__year

    # Function to delete car objects
    def __del__(self):
        print(f"The car {self.make} {self.model} has been deleted.")

# ================   Inheritance with ElectricCar subclass ================================= #
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)  # Initialize the parent class
        self.battery_size = battery_size  # Defining additional attribute for battery size

    # Function to display electric car details, including battery_size
    def display_info(self):
        super().display_info()  # Calls the display_info method from the parent Car class
        print(f"Battery size: {self.battery_size} kWh")

# **📝 Test the Classes**:

if __name__ == "__main__":
    # Create an instance of Car
    my_car = Car("Toyota", "4Runner", 2024)
    my_car.display_info()  # Display the car's make, model, and year

    # Update the year of the car using the setter method
    my_car.set_year(2022)
    print(f"Updated Year: {my_car.get_year()}")  # Access the updated year using the getter

    # Create an instance of ElectricCar
    my_electric_car = ElectricCar("Tesla", "Model S", 2020, 100)
    my_electric_car.display_info()  # Display electric car's details
