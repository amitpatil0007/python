#arithmetic operators
a = 3
b = 4
c = a+b
print(c)

#assignment operators
a = 4-2  #a ko usne apne aap leliya 2 karke
print(a)
b = 6
b += 2 #b pehle ka plus 2 same for -/% 
print(b)
c= 7
# c-=3 decrement
# c*=3 ans 21
# c/=3 divide
c += 2 #increment the value of c by 2 and then assign it to c
print(c)


#comparison operator  hamesha boolean return karega true or false
d = 5<4
print(d)

e = 5>5
print(e)

f = 5>=5
print(f)

g = 6==6
print(g)

h = 4!=5
print(h)


#logical operators
#or table
m = True or False
print("true or false is", True or False)
print("true or true is", True or True)
print("false or true is", False or True)
print("false or false is", False or False)

#aand table
n = True and False
print("true and false is", True and False)
print("false and true is", False and True)
print("false and false is", False and False)
print("true and true is", True and True)

#not table ulta
print(not(False))