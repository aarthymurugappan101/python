from circle import circle
circle1 = circle(2)

print("circle1 area = ",circle1.getarea())

circle1.enlargecircle()
print("circle1 enlarged = ",circle1.getarea())

circle1.shrinkcircle()
print("circle1 shrunk = ",round (circle1.getarea(),2))