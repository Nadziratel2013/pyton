f = open('mat_dv.txt')
lst=[]
max8=int()
max9=int()
max10=int()
max11=int()

for line in f.readlines():
    lst=line.split()
    cl=int(lst[2])
    alg=int(lst[3])
    geo=int(lst[4])
    max=int(alg+geo)
    if(lst[2]=='8'):
        if(max8<max):
            max8=max
            name8=str(lst[0]+' '+lst[1]+' '+lst[2])
    if(lst[2]=='9'):
        if(max9<max):
            max9=max
            name9=str(lst[0]+' '+lst[1]+' '+lst[2])
    if(lst[2]=='10'):
        if(max10<max):
            max10=max
            name10=str(lst[0]+' '+lst[1]+' '+lst[2])
    if(lst[2]=='11'):
        if(max11<max):
            max11=max
            name11=str(lst[0]+' '+lst[1]+' '+lst[2])



print(name8)
print(name9)
print(name10)
print(name11)

