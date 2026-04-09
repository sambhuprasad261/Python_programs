base = int(input("base = "))
exp = int(input("exp = "))

def custom_exp(base, exp):
    temp = base
    for i in range(1, exp):
        base = temp * base
    return base

res = custom_exp(base, exp)

print(f"{base} raises to the power of {exp}: {res}")