# a=10
# b=20
# a+=15
# b-=10
# print(a)
# print(b)

account={
    "number":123456789,
    "holder":"karthik",
    "balance":35000.06,
}

userIn=int(input("tell us amount to deposite "))

account['balance']+=userIn

print(userIn,"has deposited,so available is",account['balance'])

#ticket

count=int(input("Tell us no of tickets you required "))

payable=count*120;

print(payable,"amount to be payable for",count,"tickets")
