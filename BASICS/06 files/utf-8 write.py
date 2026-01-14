import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)

fh = open(scriptDir + "/ogonki.txt","w", encoding="utf-8")
fh.write("text z ogonkami: żźąśąś\n")
fh.write("text z ogonkami: źąęń \n")
fh.close()