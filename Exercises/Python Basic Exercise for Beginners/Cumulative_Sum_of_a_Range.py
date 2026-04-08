print("Printing current and previous number sum in a range(10)");

prev_num = 0

for i in range(10):
    
    sum_out = prev_num + i
    
    print(f"Current Number {i} Previous Number {prev_num} Sum: {sum_out}")
    
    prev_num = i