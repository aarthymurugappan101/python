strdict = {}
item = input("plese enter a string")
item = item.lower()#casing
for c in item:#reps the charecter
    count = strdict.get(c)
    if count == None:
        strdict[c]=1
    else:
        strdict[c] = count+1

for (k,v)in sorted(strdict.items()):#k reps the key or charecter, v reps the value or the count
    print(k+" "+ str (v))