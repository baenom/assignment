
def getIndex(number, target):
    for i in number:
        if i == target:
            return i
        
def getMax(number):
    max = number[0]
    for i in number:
        if max <= i:
            max = i
    return max

def getMin(number):
    min = number[0]
    for i in number:
        if min >= i:
            min = i
    return min

def countGT(number, target):
    max = number[0]
    for i in number:
        if max >= target:
            max = i
    return max

def sumList(number):
    sumadd = 0
    for i in number:
        sumadd += i
    return sumadd

def swapList(number):
    return number.reverse()


number_list = [23, 45, 27, 11, 25, 65, 78]
print (getIndex (number_list, 25))
print (getMax (number_list))
print (getMin(number_list))
print (countGT(number_list, 42))
print (sumList (number_list))
swapList(number_list)
print (number_list)