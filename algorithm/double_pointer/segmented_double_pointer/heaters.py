"""
   冬季来临，请设计一个有固定加热半径的供暖器向所有房屋供暖
   在加热器的加热半径范围内的每个房屋都可以获得供暖
   现在，给出位于一条水平线上的房屋houses和供暖器heaters 的位置，找出并返回可以覆盖所有房屋的最小加热半径
   example 1:
     输入: houses = [1,2,3], heaters = [2]
     输出: 1
   example 2:
     输入:  houses = [1,2,3,4], heaters = [1,4]
     输出: 1
   example 3:
     输入: houses = [1,5], heaters = [2]
     输出: 3
"""
from typing import List


# 找到每个房屋前一个加热器，和后一个加热器，取距离最近的值
# 使用指针pointer_previous和pointer_next，分别指向前一个加热器，和后一个加热器
# 此时所有房屋的距离最大值就是目标半径
# 当只有一个加热器的时候，直接计算后返回即可
def heaters(houses: List[int], heaters: List[int]) -> int:
    result = []
    if len(heaters) == 1:
        for item in houses:
            result.append(abs(item - heaters[0]))
        return max(result)
    houses.sort()
    heaters.sort()
    pointer_previous, pointer_next = 0, 1
    for house in houses:
        while pointer_next < len(heaters) - 1 and heaters[pointer_next] < house:
            pointer_next += 1
            pointer_previous += 1
        result.append(min(abs(house - heaters[pointer_previous]), abs(heaters[pointer_next] - house)))
    return max(result)


if __name__ == '__main__':
    print(heaters(houses=[1, 2, 3], heaters=[2]))
    print(heaters(houses=[1, 2, 3, 4], heaters=[1, 4]))
    print(heaters(houses=[1, 5], heaters=[2]))
