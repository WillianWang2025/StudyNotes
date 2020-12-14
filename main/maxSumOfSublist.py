"""
求数组中连续子数组的和的最大值
"""


# 方法一 穷举法
def maxOfSum(ls):
    maxsofar = 0
    n = len(ls)
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += ls[k]
            maxsofar = max(maxsofar,sum)
    return maxsofar


if __name__ == '__main__':
    ls = [1,2,3,4,-10,5,7]
    ls2 = [4]
    maxSum = maxOfSum(ls2)
    print(maxSum)

