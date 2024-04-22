s=('sam',1,2,3,4,4)
print(s)
print(type(s))
#range of tuple

a=('sam','raja','ganesh','anu','ss')
print(a[0:4])
print(a[:2])
print(a[2:])

a1=10
b=10.5
c='Anu'
print(type(a1))
print(type(b))
print(type(c))



#Tuple method
a=(1,2,3,4,5,6,1,8,3,4,1,510,1)
b=a.count(1)
print(b)
#index
s=(1,2,3,4,5,6,7)
d=s.index(5)
print(d)


#append method
a=('sam','sathish','anu','priya')
b=list(a)
b.append("ganesh")
a=tuple(b)
print(a)
#adding tuple in tuple
a=('sam','sathish','anu','priya')
b=("ganesh",)
a += b
print(a)



a=('sam','raja','anu','pk')
if 'sam' in a:
    print("welcome ")
else:
    print("NOt valid")

#del keyword
# a=("sam","sathish","anu","pk","raja")
# del a
# print(a)

#Join 
a=("sam","sathis","vekat","Karthi")
a=a*3
print(a)
s={1,2,3,4,5,1,3,5,6}
print(s) 


a=("sam","pk","sathish","karthi")
b=(1,2,3)
c=a + b
print(c)



a=('sam','sathish','pk')
for i in a:
    print(i)
#range methods
a=(1,2,3,"sam","pk")
for i in range(len(a)):
    print(a[i])
#while Loop
'''
a=("sam","raja",1,2,3)
i=0
while i<len(a):
    print(a[i])
    i=i+1'''



#remove
a=("sam","sathish","anu","pk","raja")
b=list(a)
b.remove("raja")
a=tuple(b)
print(a)