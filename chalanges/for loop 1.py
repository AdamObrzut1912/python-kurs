numbers = [-3,-2,-1,0,1,2,3]
set = {-1}

for i in numbers:
    if i%2 != 0:
        set.add(i)

for i in set:
    print(i)