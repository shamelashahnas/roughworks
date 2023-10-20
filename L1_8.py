a=[22,22,33,45,65,22,77,33,65,44,33,33,33]
i=1
while i<len(a):
    if a[i] in a[0:i]:
        a.pop(i)
    else:
        i+=1
print(a)

print("   this is for git",a)



# b=[]
# for x in a:
#
#     if x not in b:
#         b.append(x)
#
# print(b)



