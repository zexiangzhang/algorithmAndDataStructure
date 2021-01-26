"""
    在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积
    每个矩形由其左下顶点和右上顶点坐标表示
    example:
     输入: -3, 0, 3, 4, 0, -1, 9, 2
     输出: 45
"""


# 把两个矩形叫做A和B
# 不重叠就有四种情况，此时矩形覆盖的面积就是两个矩形的面积和：
#   1、A在B左边
#   2、A在B右边
#   3、A在B上边
#   4、A在B下边
# 有重叠的情况，只要求出重叠形成的矩形的面积，然后用两个矩形的面积减去重叠矩形的面积就是两个矩形覆盖的面积了
# 求重叠矩形的面积，需要确认重叠矩形的四条边：
#   1、左边选择两个矩形的两条左边靠右的那条
#   2、上边选择两个矩形的两条上边靠下的那条
#   3、右边选择两个矩形的两条右边靠左的那条
#   4、下边选择两个矩形的两条下边靠上的那条
def compute_area(a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int) -> int:
    area1 = (c - a) * (d - b)
    area2 = (g - e) * (h - f)
    if e >= c or g <= a or f >= d or h <= b:
        return area1 + area2
    length_x_1 = min(c, g)
    length_x_2 = max(e, a)
    length = length_x_1 - length_x_2
    width_y_1 = min(d, h)
    width_y_2 = max(f, b)
    width = width_y_1 - width_y_2
    area_repeat = length * width
    return area1 + area2 - area_repeat


if __name__ == '__main__':
    print(compute_area(-3, 0, 3, 4, 0, -1, 9, 2))