from math import sqrt

def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points.sort()
    hull = []
    for p in points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

def calculate_perimeter(points):
    hull = convex_hull(points)
    return round(sum(distance(hull[i], hull[i + 1]) for i in range(len(hull) - 1)))

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(calculate_perimeter(points))

if __name__ == "__main__":
    main()


