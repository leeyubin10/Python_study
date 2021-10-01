a = [2,4,10,20,5,2,20,4]

uniq_items=[]

for x in a:
    if x not in uniq_items:
        uniq_items.append(x)

print('중복제거전',a)
print('중복제거후',uniq_items)
