spam = ['apples', 'bananas', 'tofu', 'cats']
str=""
l=len(spam)
j=0
for i in spam:
    str=str+i
    if j<l-2:
        str=str+", "
    if j==(l-2):
        str=str+" and "
    j=j+1
print(str)
