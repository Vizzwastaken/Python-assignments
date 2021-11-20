a,b=1,2,
pas = input("Enter the password : ")
flagu=0
flagl=0
flagn=0
if(len(pas) >= 8):
    for i in pas:
        if(i.isupper()):
            flagu=1
        if(i.islower()):
            flagl=1
        if(i.isnumeric()):
            flagn=1

if(flagn == 1 and flagu == 1 and flagl == 1):
    print("strong password")
else:
    print("weak password")