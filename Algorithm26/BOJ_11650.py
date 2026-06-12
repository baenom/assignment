def BOJ11650():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points.sort(key=lambda x: (x[0], x[1]))
    for point in points:
        print(point[0], point[1])

if __name__ == "__main__":
    BOJ11650()