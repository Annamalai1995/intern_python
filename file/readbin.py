from pickle import *
name=open("data.txt","rb")
# while True:
#     try:
#         office=load(name)
#         print(office)
#     except EOFError as e:
#         break


content=load(name)
print(content)
content1=load(name)
print(content1)
# name.close()
