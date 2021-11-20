import os
import re
path = r'C:\\Users\\VK30\\Downloads\\Automation Assignment\\'
dirlist = os.listdir(path)
pat_regex = re.compile(str(input("enter the pattern")))
file_regex = re.compile(r'Assignment-01.txt')
# if pat_regex.match("Strong"):
#     print("ok")
#print(pat_regex)
for i in range(len(dirlist)):
    #print(dirlist[i])
    if dirlist[i].endswith(".txt"):
        print(dirlist[i])
        file1 = open(path+ dirlist[i],'r',encoding='utf-8')
        content = file1.read()
        content_list = list(content.split(" "))
        #print(content_list)
        for line in content_list:
           # print(content[line])
            if pat_regex.search(line):
                print(line)
        file1.close()
