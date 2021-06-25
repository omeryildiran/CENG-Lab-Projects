machine=eval(input())
request=eval(input())
payment=int(input())
hesap=0
for item in request:
    if item in machine.keys():
        hesap=hesap+machine[item]
    else:
        continue

if payment>hesap:
    print("Change:"+str(payment-hesap))
elif payment<hesap:
    print("Insert:"+str(hesap-payment))
elif payment==hesap:
    print("Done")