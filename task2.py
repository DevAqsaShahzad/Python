mylist=[]
num = int(input())
for i in range(1,num):
    if((num%i)==0):
        mylist.append(i)
print(mylist)
