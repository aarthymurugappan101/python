s=set()#to create an empty set or else a not so empty example: s = {1,2}

s.add('1')
print(s)

s.add('1')
print(s)

s.add(1) #{1,'1'}
print(s)

s2=('2')

s3 = s.union(s2)
print(s3) 

s4 = s.intersection(s2)
print(s4)