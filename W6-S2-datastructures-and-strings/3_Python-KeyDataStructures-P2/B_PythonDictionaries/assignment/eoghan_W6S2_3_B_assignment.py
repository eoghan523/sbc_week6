#variable to use in the  conditional logic later
retirement_age = 65

#Defines the dictionary "my_dict" and within my_dict is the nested employees within the dictionary.
my_dict = {
    "Employee" : [
    {"name": "John", "age": 31, "email": "john@bloggs.com", "job": "Security"},
    {"name": "Alice", "age": 65, "email": "alice@blogs.com", "job": "HR"},
    {"name": "Tony", "age": 38, "email": "tony@bloggs.com", "job": "IT"}
    ]    
}

employee_id = 0 #Defines 'employee_id' variable and the value is 0

for employee in my_dict["Employee"]:         #For loop that targets "Employee" values.
    employee['id'] = employee_id                   #adds an id value to employee values.
    employee["retirement_eligible"] = employee["age"] >= retirement_age     #Adds a conditiional check on the age value anginst 'retirement_age' integer if its higher than or equal to '65'.   
    employee_id += 1                                      #The for loop adds 1 to each employee id. 

print(employee_id) #prints the 'employee_id' count.

#The new dictionary with the new data defined under the variable 'new_hires'.
new_hires = {
    "Employee" : [
         {"name": "Elenor", "age": 40, "email": "elenor@bloggs.com", "job": "Marketing"},
         {"name": "Roger", "age": 63, "email": "roger@bloggs.com", "job": "Engineering"},
         {"name": "Steve", "age": 41, "email": "steve@bloggs.com", "job": "Catering"}
    ]
}

#This for loop adds new unique ids to the 'Employees' in the 'new_hire' ddictionary
for new_employee in new_hires["Employee"]:  
        new_employee["id"] = employee_id
        new_employee["retirement_eligible"] = new_employee["age"] >= retirement_age #checks the 'Employee' age integer if its higer than or equal to 65.
        employee_id += 1

#This line of code merges the dictionaries from the 'my_dict' and 'new_hires'
updated_list = {"Employees": my_dict["Employee"] + new_hires["Employee"]}

print(updated_list)


print("Below is the list of employees retirement Eligible:")
for employee in updated_list ["Employees"]:
      if employee["retirement_eligible"]:
            print(f'name: {employee["name"]}, {employee["age"]}, {employee["email"]}, {employee["job"]}, {employee["id"]}')
        elif employee["age"] >= 63:
            print(f'Near Retirement: {employee["name"]}, {employee["age"]}, {employee["email"]}, {employee["job"]}, {employee["id"]}')

      











    




