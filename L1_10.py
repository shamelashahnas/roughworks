a='**#*#**##'
i=0
c=''
d=""
for x in a:
    if x[i]=='*':
        c=c+x
    else:
        d=d+x

if len(c)>len(d):
    print('positive integer')
elif len(d)>len(c):
    print('negative integer')
else:
    print('0')
# print('*= '+str(len(c)))
# print('#= '+str(len(d)))
# print('*-#= '+str(len(c)-len(d)))
print("this is for git")