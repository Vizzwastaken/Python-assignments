def collatz(num):
    if num%2==0:
        return num//2
    else:
        return (3*num)+1

num =int(input("enter the number"))
while(num!=1):
    num=collatz(num)
    print(num)