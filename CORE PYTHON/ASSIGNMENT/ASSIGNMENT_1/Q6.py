# wap to input two angle from user and find third angle of the triangle

angle1 = float (input ("enter first angle:"))
angle2 = float (input("enter second angle:"))

angle3 = 180 - (angle1+angle2)
print ("third angle of triangle",angle3)