#!/usr/bin/python3

# num = 12345
for num in range(00, 100):
    a = str(num)
    b = len(a)
    if num == 99:
        
        print(num)
        continue
    elif b == 2:
        print(num, end=", ")
        continue
    elif b == 1:
        print("0"+str(num), end=", ")
        
# print(b)