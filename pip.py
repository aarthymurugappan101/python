from os import system
system ("say Test 123")
file = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/class work/speach.txt")

data = file.readlines()

for line in data:
    system("say "+ line)