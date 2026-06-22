s = {1,5,32,54,3,3,"patil"}
print(s,type(s))
s.add(44)
print(s,type(s))
s.remove(5)
print(s,type(s))


# set methods in python

# Here are the most commonly used set methods in Python (clean + practical):

# 🔹 1. Adding Elements
# add(x) → Adds a single element

# s = {1, 2}
# s.add(3)   # {1, 2, 3}
# update(iterable) → Adds multiple elements

# s.update([4, 5])   # {1, 2, 3, 4, 5}
# 🔹 2. Removing Elements
# remove(x) → Removes element (error if not found)

# s.remove(2)
# discard(x) → Removes element (no error if not found)

# s.discard(10)
# pop() → Removes random element

# s.pop()
# clear() → Removes all elements

# s.clear()
# 🔹 3. Set Operations
# union() → Combines sets

# a = {1, 2}
# b = {2, 3}
# a.union(b)   # {1, 2, 3}
# intersection() → Common elements

# a.intersection(b)   # {2}
# difference() → Elements in first not in second

# a.difference(b)   # {1}
# symmetric_difference() → Non-common elements

# a.symmetric_difference(b)   # {1, 3}
# 🔹 4. In-place Update Methods
# intersection_update()

# difference_update()

# symmetric_difference_update()

# 👉 These modify the original set instead of returning a new one.

# 🔹 5. Comparison Methods
# issubset()

# {1,2}.issubset({1,2,3})   # True
# issuperset()

# {1,2,3}.issuperset({1,2})   # True
# isdisjoint() → No common elements

# {1,2}.isdisjoint({3,4})   # True
# 🔹 6. Copy
# copy() → Creates a shallow copy

# new_set = s.copy()