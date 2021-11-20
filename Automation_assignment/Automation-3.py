import re

file1 = open('auto3.txt','r')
lines = file1.read()
words = list(lines.split())
file1.close()
# print(words)
adjreg=re.compile(r'ADJECTIVE')
verbreg=re.compile(r'VERB')
nounreg=re.compile(r'NOUN')
file1 = open('auto3.txt','w')
for i in words:
    if verbreg.match(i):
        i = verbreg.sub(input("enter the verb"),i)
    if adjreg.match(i):
        i = adjreg.sub(input("enter the adjective"),i)        
    if nounreg.match(i):
        i = nounreg.sub(input("enter the noun"),i)
    file1.write(i+" ")
file1.close()
file1 = open('auto3.txt','r')
lines=file1.read()
print(lines)
file1.close()