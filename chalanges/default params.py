def f(email, country = "Poland", company = "Example Ltd"):
    slownik = {
        "userEmail":email,
        "userCountry":country,
        "userCompany":company
    }
    print(slownik)


f("ola@example.com")
f("kasia@example.com", "UK")