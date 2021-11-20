dct={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
sum = 0
for k,v in dct.items():
    print(v ,k)
    sum = sum +v
print("total number of items :" + str(sum))
