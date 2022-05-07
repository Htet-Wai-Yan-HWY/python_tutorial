new_s="t.e.s.t"

List=[]
x= len(new_s)
y= len(List)

for i in new_s:
    List.append(i)

for j in range(0,y):
    List.pop(j%2)
    
print()