a = (1,2,3,4,5,6,3)
print(a)
no = a.count(3) #.count method
print(no)

i = a.index(2)
print(i)




# tuple methods

# In Python, tuples are immutable (you can’t change them after creation), so they have very few built-in methods compared to lists.

# 🔹 Tuple Methods (Only 2)
# 1. count()
# Returns how many times a value appears in the tuple.

# t = (1, 2, 3, 2, 2, 4)

# print(t.count(2))   # Output: 3
# 2. index()
# Returns the index of the first occurrence of a value.

# t = (10, 20, 30, 20)

# print(t.index(20))   # Output: 1
# 👉 You can also specify start and end range:

# t = (10, 20, 30, 20, 50)

# print(t.index(20, 2, 5))   # Output: 3
# 🔹 Important Notes
# Tuples are immutable, so no methods like append(), remove(), etc.

# But you can still use built-in functions:

# t = (5, 2, 9, 1)

# print(len(t))   # 4
# print(max(t))   # 9
# print(min(t))   # 1
# print(sum(t))   # 17
# 🔥 Quick Summary
# Method	Use
# count(x)	Counts occurrences of x
# index(x)	Finds first index of x
# If you want, I can also give you tuple interview questions or tricks (very useful for exams & coding rounds).


# most used tuple mehods

# Since tuples are immutable, Python only gives 2 built-in methods, but in real coding people use some common operations + functions with tuples a lot.

# 🔥 Most Used Tuple Methods
# 1. count()
# 👉 Used to count occurrences

# t = (1, 2, 2, 3, 2)
# print(t.count(2))   # 3
# 2. index()
# 👉 Used to find position

# t = (10, 20, 30, 20)
# print(t.index(20))   # 1
# 💡 Most Used Tuple Operations (Very Important)
# Even more than methods, these are used daily:

# 🔹 3. Accessing Elements
# t = (10, 20, 30)
# print(t[1])   # 20
# 🔹 4. Slicing
# t = (1, 2, 3, 4, 5)
# print(t[1:4])   # (2, 3, 4)
# 🔹 5. Tuple Unpacking ⭐ (VERY IMPORTANT)
# t = (1, 2, 3)
# a, b, c = t
# print(a, b, c)
# 🔹 6. Membership Check
# t = (1, 2, 3)
# print(2 in t)   # True
# 🔹 7. Looping
# for i in (1, 2, 3):
#     print(i)
# 🔧 Common Built-in Functions Used with Tuples
# t = (4, 2, 9, 1)

# print(len(t))   # 4
# print(max(t))   # 9
# print(min(t))   # 1
# print(sum(t))   # 16