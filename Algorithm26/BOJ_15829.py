M = 1234567891
r = 31

string = "abcde"

total_sum = 0
    

for i in range(len(string)):
    a_i = ord(string[i]) - 96
    total_sum += a_i * (r ** i)

print(total_sum % M)