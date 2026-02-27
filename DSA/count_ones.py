n = 5000000

count  = 0
for i in range(1, n+1):
    k = str(i)
    #print(k, type(k))
    for j in k:
        #print("loop k = ", j)
        if int(j) == 1:
            count += 1
            #print("loop count = ", count)
        else:
            continue
print(count)   