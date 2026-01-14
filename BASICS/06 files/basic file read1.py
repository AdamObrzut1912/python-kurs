fh = open("C:\\Users\\obrzu\\Desktop\\python kurs\\test.txt", "r")
lines = fh.readlines()
fh.close

for line in lines:
    print(line)