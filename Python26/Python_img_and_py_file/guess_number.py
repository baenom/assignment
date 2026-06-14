import random
cum_num_end = 50
end_num = 7

com_num = random.randint(1,cum_num_end)

count = 1
while True:
    count += 1
    user_num = int(input("숫자를 입력하세요"))
    if user_num > com_num:
        print("down")
    elif user_num < com_num:
        print("up")
    else: 
        print("you win!!!")
        break
    if count == end_num:
        print("you lose~~~")
        break
print(">>컴퓨터의 숫자:",com_num)


