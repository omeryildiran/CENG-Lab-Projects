name=input()
color=input()
number=int(input())

flowerName=""
flowerColor=""
white=['0','1','2','3']
pink=['4','5','6']
red=['7','8','9']
flowerNum=0
if name[0]=='7':
    flowerName="Rose"
elif name[0]=='8':
    flowerName="Tulip"
else:
    flowerName="Orchid"
    
if color[-1] in white:
    flowerColor="White"
elif color[-1] in pink:
    flowerColor="Pink"
elif color[-1] in red:
    flowerColor="Red"
    
if flowerName=="Rose" and number >100:
    print("Invalid!")
elif flowerName=="Tulip" and number >50:
    print("Invalid!")    
elif flowerName=="Orchid" and number >30:
    print("Invalid!")
else:
    print(flowerName+flowerColor+str(number))
    