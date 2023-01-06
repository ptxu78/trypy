# n = a ** m
# m * ln(a) = ln(n)
# ln(a) = ln(n) / m
# a = e ** (ln(n) / m)
import math
# 输入
# n,m = map(int, input().split(' '))
# 19692140453072697253697824 = 114514 ** 5
n, m = 19692140453072697253697824, 5
# 计算
a = math.e ** (math.log(n, math.e) / m)
# 取整
a = round(a)
# 输出
print(a)
