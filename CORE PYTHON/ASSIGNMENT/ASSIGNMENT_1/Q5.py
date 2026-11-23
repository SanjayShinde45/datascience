# wap to enter P,T,R and calculate compound interest

p = float (input("enter priciple amount (p):"))
t = float (input("enter time (t):"))
r = float (input("enter rate (R):"))

amount = p*(1+r/100)**t

ci=amount-p
print("compound interest",ci)
print("total amount ",amount)