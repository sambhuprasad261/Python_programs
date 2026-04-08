num_list = [10, 20, 33, 46, 55]
div_lst = []

for i in num_list:
    if i%5 == 0:
        div_lst.append(i)
    else:
        continue
        
print(div_lst)