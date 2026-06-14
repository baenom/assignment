stack = []
capacity = 5

def isFull():
    if len(stack) >= capacity:
        return True
    else:
        return False
    
def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

def push(data):
    if isFull():
        print('스택이 꽉차있습니다')
    else:
        stack.append(data)

def pop():
    if isEmpty():
        print('스택이 비어있습니다')
        return -1
    else:
        return stack.pop()
    
def peek():
    if isEmpty():
        print('스택이 비어있습니다')
        return -1
    else:
        return stack[-1]

print(f'[[정수형 스택 연산 실습 (용량 : {capacity})]]')

while True:
    print('==========================')
    print('1.push 2.pop 3.peek 0.exit')
    print('==========================')
    menu = int(input('> 메뉴 선택: '))
    if menu == 0:
        break
    elif menu == 1:
        data = int(input('데이터 입력'))
        push(data)
    elif menu == 2:
        data = pop()
        print('> 가져온 데이터:', data)
    elif menu == 3:
        data = peek()
        print('> 가져올 데이터:', data)
    print('> 현재 스택 상태:', stack)
    
    
print('[[정수형 연산 실습 종료]]')