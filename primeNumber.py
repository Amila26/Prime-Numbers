L = int(input("EnterLower Value"))
U = int(input("EnterUpper Value"))
for i in range(L,U):
    count=0
    #print(i)
    for j in range(2,i):
        if(i%j==0):
            count=count+1
           # print(j)
    if(count==0):
        print(i,end=" ")