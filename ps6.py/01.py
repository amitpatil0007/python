# Write a program to find the greatest of four numbers entered by the user
a1 = int(input("enter number a1:"))
a2 = int(input("enter number a2:"))
a3 = int(input("enter number a3:"))
a4 = int(input("enter number a4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1",a1)
    
if(a2>a1 and a2>a3 and a1>a4):
    print("greatest number is a2",a2)
    
if(a3>a2 and a3>a1 and a3>a4):
    print("greatest number is a3",a3)

if(a4>a2 and a4>a3 and a4>a1):
    print("greatest number is a4",a4)
    
#yaha if ke jageh a2 se elif bhi likhe sakte the jaise
# elif(a2>a1 and a2>a3 and a1>a4):
#     print("greatest number is a2",a2)
    
# elif(a3>a2 and a3>a1 and a3>a4):
#     print("greatest number is a3",a3)
# elif(a4>a2 and a4>a3 and a4>a1):
#     print("greatest number is a4",a4)
