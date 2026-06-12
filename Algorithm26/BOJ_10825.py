def BOJ10825():
    N = int(input())
    students = []
    for _ in range(N):
        name, kor, eng, math = input().split()
        students.append((name, int(kor), int(eng), int(math)))
        
    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    
    for student in students:
        print(student[0])

if __name__ == "__main__":
    BOJ10825()