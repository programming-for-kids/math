# 2023/07/22

# --- Q1 ---

# y = ax + b
# f(x) = ax + b，是一条直线


# 给定函数 f(x) = 2x + 1
# 也就是说，a = 2, b = 1
from fractions import Fraction  # 分数
import math


def f(x):
    return 2 * x + 1


# 输出整数点
def p(x):
    return (x, f(x))


print(p(1), p(2), p(3), p(4), p(5), sep="\n")

# 问题
# 已知 f(x) = 55，求 x


def solution1(y):
    x = ...
    return x


# --- 一般化 ---


# 函数生成器：返回函数的函数
def f_generator(a, b):
    # 匿名函数
    return lambda x: a * x + b


f2 = f_generator(2, 1)  # f2(x) = 2x + 1
f3 = f_generator(3, 1)  # f3(x) = 3x + 1
f4 = f_generator(4, 1)  # f4(x) = 4x + 1
f5 = f_generator(4, 3)  # f5(x) = 4x + 3

print(f2(2), f3(2), f4(2), f5(2))

# --- Q2 ---


# 给定函数 f(x) = ax + b
# 例如，a = e, b = π
a = math.e
b = math.pi


def g(x):
    return a * x + b


# 输出整数点
def q(x):
    return (x, g(x))


print(
    q(0),
    q(1),
    q(math.e),  # 自然指数 2.718281828
    q(math.pi),  # π 3.141592653589793
    q(4.4),  # 小数
    q(-5),  # 负数
    q(Fraction(2, 3)),  # 分数
    q(complex(1, -1)),  # 复数 1 - i
    sep="\n")

print(1 - 2j)

# 问题
# 已知 g(x) = 55，求 x


def solution2(y):
    x = ...
    return x
