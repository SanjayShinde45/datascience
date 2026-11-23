# wap to check login take userid & password from user check if with handcoded values if matched print "login successful" if not print"invalid cretials

correct_password="123"
correct_id="sanjay"

userid=input("enter id:")
password=input("enter a pass:")

if(correct_id==userid and password==correct_password):
    print("login suceess")
else:
    print("invalid crediants")