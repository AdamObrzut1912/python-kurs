def emailParts(email):
    monkeyInd = email.find("@")
    dotInd = email.find(".")
    user = email[0:monkeyInd]
    domainName = email[monkeyInd+1: dotInd]
    domainExt = email[dotInd+1:]

    slownik = {
        "user":user,
        "domainName":domainName,
        "domainExt":domainExt

    }
    return slownik

print(emailParts("ola@domena.com"))

