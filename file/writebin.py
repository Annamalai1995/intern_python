from pickle import *
name=open("data.txt","wb")
office=[2190,"Saran","MEC","Salem"]

college={"Name":"karthi","College":"MEC","Rollno":2879}

Frnds=("saran","priya")

dump(office,name)
dump(college,name)
dump(Frnds,name)
name.close()
