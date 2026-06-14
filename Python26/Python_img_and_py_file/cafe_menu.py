print('어서오세요 카페입니다')

def sum_menu_pric(sum_menu_f,menu_pric_f):
  if sum_menu_f <= menu_pric_f:
    return True
  return False

def order(sum_menu_f,menu_pric_f):
  if sum_menu_f < menu_pric_f:
    return menu_pric_f - sum_menu_f
  return 0

def menu_show(menu_f):
  for key,value in menu_f.items():
    print(key,value)

menu_list = []
menu = {'아메리카노':500,'레몬에이드':600,'복숭아아이스티':800,'빵':900,'샌드위치':700,}
sum_menu = 0
while True:
  menu_show(menu)
  user_menu = input("메뉴를 골라주세요. 주문하시려면 '주문하기' 라고 말씀해주세요")
  if user_menu == '주문하기':
    menu_pric = int(input("주문 금액을 입력해주세요"))
    if sum_menu_pric(sum_menu,menu_pric):
      break
    else:continue
  menu_list.append(user_menu)
  sum_menu += menu[user_menu]

print(f"거스름돈은{order(sum_menu,menu_pric)}원 입니다")
print('주문하신 영수증입니다')
for i in menu_list:
  print(i,menu[i],'원')