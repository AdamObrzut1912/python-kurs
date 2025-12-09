employee = {
    "name": "Adam",
    "email": "Obrzut",
    "rank": "menager",
    "salary": 8000
}

def promoteToManager(user):
   
    if user["rank"] == "menager":
        print("jest już menagerem")
        return 
    user["salary"] *= 1.5
    user["rank"] = "menager"

promoteToManager(employee)

for key, value in employee.items():
    print(key, value)