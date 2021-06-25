#This is a password creator tool

u1=input()
p1=input()
u2=input()
p2=input()
u3=input()
p3=input()
 
users=[u1,u2,u3]
paswords=[p1,p2,p3]

selected=input()

for i in range(len(users)):
    if users[i]==selected:
        newpas1=users[i][-4:]
        newpas2=paswords[i][:-6:-1]
        newpas3=(len(paswords[i])**2)%100
    else:
        continue
print(newpas1+newpas2+str(newpas3))