def createUser(name,contact):
    user = {
        "userName" : name
    }

    if isinstance(contact, str):
        user["email"] = contact
        for key, value in user.items():
            print(f"imię: {user["userName"]}, contact (string): {user["email"]}")
            break
   
    if isinstance(contact, int):
        user["telephone"] = contact
        for key, value in user.items():
            print(f"imię: {user["userName"]}, contact (int): {user["telephone"]}")
            break


print(createUser("Ola", "ola@example.com"))
print(createUser("Kasia", 546546456))