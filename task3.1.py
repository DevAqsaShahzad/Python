import random
myrandom1=[]
for x in range(10):
  myrandom1.append(random.randrange(1,101))
print("my random list 1", myrandom1)
myrandom2=[]
for y in range(10):
  myrandom2.append(random.randrange(1,101))
print("my random list 2", myrandom2)

mylist=[]
for i in range(len(myrandom1)):
    for j in range(len(myrandom2)):
        if(myrandom1[i]==myrandom2[j]):
            mylist.append(myrandom1[i])
newset=set(mylist)
print(newset)
