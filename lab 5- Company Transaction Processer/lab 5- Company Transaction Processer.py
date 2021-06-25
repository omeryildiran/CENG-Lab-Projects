def process_transactions(transactions, lower_bound, upper_bound):
    alttakiler=[]
    usttekiler=[]
    ortancalar=[]
    for i in range(len(transactions)):
        if transactions[i]<=lower_bound:
            alttakiler.append(transactions[i])
        elif transactions[i]>lower_bound and transactions[i]<upper_bound:
            ortancalar.append(transactions[i])
        elif transactions[i]>=upper_bound:
            usttekiler.append(transactions[i])
    
    sonuclar=list([alttakiler,ortancalar,usttekiler])

    return sonuclar
