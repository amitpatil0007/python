name = "patil"
print(name[-4:-1]) #yeh negative hai isko positive kiya neeche
print(name[1:4])

print(name[:4])  # print(name[0:4])
print(name[1:])  # print(name[1:5])  -1 hai last mein start mein 0 hai
print(name[1:5])

# #SLICING WITH SKIP VALUE 
# We can provide a skip value as a part of our slice like this: 
# word = "amazing" 
# word[1: 6: 2] # "mzn" 
# Other advanced slicing techniques: 
# Word = "amazing" 
# Word = [:7]  # word [0:7] – 'amazing' 
# Word = [0:]  # word [0:7] – 'amazing' 