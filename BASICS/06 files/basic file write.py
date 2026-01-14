fh = open("test.txt", "w")
fh .write("contetn1\n")
fh .write("contetn2\n")
fh.close()



fh2 = open("test.txt", "a")
fh2.write("contetent3\n")
fh2.close