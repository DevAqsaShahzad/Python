Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> for i in range(len(a)):
	if(a[i]<5):
		myList.insert(b,a[i])
		b=b+1

	
Traceback (most recent call last):
  File "<pyshell#5>", line 3, in <module>
    myList.insert(b,a[i])
NameError: name 'myList' is not defined
>>> Mylist
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Mylist
NameError: name 'Mylist' is not defined
>>> MyList()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    MyList()
NameError: name 'MyList' is not defined
>>> myList=[]
>>> b=0
>>> for i in range(len(a)):
	if(a[i]<5):
		myList.insert(b,a[i])
		b=b+1

		
>>> print(myList)
[1, 1, 2, 3]
>>> for i in range(len(a)):
	if(a[i]<5):
		myList.appened(a[i])

		
Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    myList.appened(a[i])
AttributeError: 'list' object has no attribute 'appened'
>>> for i in range(len(a)):
	if(a[i]<5):
		myList.append(a[i])

		
>>> print(myList)
[1, 1, 2, 3, 1, 1, 2, 3]
>>> 
