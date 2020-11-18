num = int(input())
points = []

def polygon_area(point_list):
    plus_part = point_list[len(point_list)-1][0] * point_list[0][1]
    for i in range(1, len(point_list)):
        plus_part += (point_list[i-1][0] * point_list[i][1])
    minus_part = point_list[0][0] * point_list[len(point_list)-1][1]
    for i in range(1, len(point_list)):
        minus_part += (point_list[i][0] * point_list[i-1][1])
    area = plus_part - minus_part
    if plus_part <= minus_part:
        area *= (-1)
    return area * 0.5


for i in range(num):
    point = list(map(int, input().split()))
    points.append(point)

print("{:.1f}".format(polygon_area(points)))