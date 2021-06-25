def find_extremities(env_list,mode):
    sonuc_ilan=[]
    for x in range(len(env_list)):
        for element in range(len(env_list[x])):
            env_list[x][element]=int(env_list[x][element])
    
    if mode=="max":
        for num_of_lists in range(len(env_list)):
            sonuc_ilan.append(max(env_list[num_of_lists]))
    
    elif mode=="min":
        for num_of_lists in range(len(env_list)):
            sonuc_ilan.append(min(env_list[num_of_lists]))
        
    mean=float(sum(sonuc_ilan)/len(sonuc_ilan))
    
    return [sonuc_ilan,mean]
    