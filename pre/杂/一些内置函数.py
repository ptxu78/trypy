# # 判断浮点数为0
# print(abs(1-1.0 < 1e-6))
#
# # _表可读性
# print(123_456)
#
# # 列表定位
# l = [9,6,4,2,4,5]
# print(l.index(4))
#
# # range倒叙
# lenList = 10
# for i in range(lenList, 0, -1):
#     print(i)

# zip
# print(help(zip))
# 所有的内置函数
# print(dir(__builtins__))
# print(help(reversed))
# print(help(sorted))
# max 与 sort
import random
a = [random.randint(1,100) for i in range(10)]
print(a)
def maxa(a):
    return -1 * a
print(max(a, key = maxa))

print(sorted(a, key = lambda item: (len(str(item)),item) ,reverse=True))
