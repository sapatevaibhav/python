t1=(58,65,99,98,97,58)
for i in t1:
    sum=0
    for j in t1:
        if i==j:
            sum=sum+1
            if sum>=2:
                print(j," is repeated")