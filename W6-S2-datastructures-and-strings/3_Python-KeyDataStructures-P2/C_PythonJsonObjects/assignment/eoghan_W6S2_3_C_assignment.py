import json   #This line off code imports json from the inbuilt json libray

json_data = ''' {
    "company": {
        "name": "Tech Corp",
        "location": "New York",
        "departments": [
            {
                "name": "Engineering",
                "employees": [
                    {"name": "Alice", "age": 30, "role": "Software Engineer"},
                    {"name": "Bob", "age": 35, "role": "DevOps Engineer"}
                ]
            },
            {
                "name": "Sales",
                "employees": [
                    {"name": "Charlie", "age": 28, "role": "Sales Manager"},
                    {"name": "Dana", "age": 32, "role": "Account Executive"}
                ]
            }
        ]
    }
} '''

parsed_json = json.loads(json_data)

engineering_employees = parsed_json["company"]["departments"][0]["employees"]

print(engineering_employees)