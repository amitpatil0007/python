#Write a program which finds out whether a given name is present in a list or not
l = ["amit" , "patil" , "sania" , "more" , "sanjay"]
name = input("enter your name: ")

if(name in l):
    print("your name is in list mein hai")
    
else:
    print("your name is not in list mein nhi hai")