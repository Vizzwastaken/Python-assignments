inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
for i in dragonLoot:
    if i in inv:
        for k,v in inv.items():
            if k==i:
                inv[k]=v+1
    else:
        print(i)
        inv[i]=1
print(inv)