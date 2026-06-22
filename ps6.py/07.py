# Write a program to find out whether a given post is talking about “Harry” or not
post = input("enter the post:")

if("harry" in post.lower()):
    print("this post is talking about harry")
    
else:
    print("not talking about harry")
    
    #.lower kiya post ko kyuki harry upper lower kisme bhi chal jayega abhi