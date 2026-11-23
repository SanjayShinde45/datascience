# wap to convert days into years , weeks and days

days = int (input("enter total days"))
year = days // 365 
remaing_day = days % 365
weeks = remaing_day //7
remaing_day = remaing_day % 7 

print ("years",year)
print("weeks",weeks)
print ("days",remaing_day)