def BOJ1181():
    N = int(input())

    string_list = []
    for _ in range(N):
        string = input()
        string_list.append(string)

    string_list.sort(key=lambda x: (len(x), x))
    for i in string_list:
        print(i)

if __name__ == "__main__":
    BOJ1181()