numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def lst_comp(num):
    #if num[0] == num[len(num) - 1]:
    if num[0] == num[-1]:
        return True
    else:
        return False
        
print(f"Given list: {numbers_x}| result is {lst_comp(numbers_x)}")
print(f"Given list: {numbers_y}| result is {lst_comp(numbers_y)}")