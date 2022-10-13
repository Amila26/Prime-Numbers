from socket import MsgFlag


L = int(input("EnterLower Value"))
U = int(input("EnterUpper Value"))
print("all the prime Numbers between" , L ,"and" , U ,"are \n")
for i in range(L,U):
    count=0
    #print(i)
    for j in range(2,i):
        if(i%j==0):
            count=count+1
           # print(j)
    if(count==0):
        print(i,end=" ")
