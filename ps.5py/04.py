s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

a = set()
a.add(20)
a.add(20.0)
a.add("20")
print(a)    # reason 20 == 20.0 cover both at same time