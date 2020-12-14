"""
求数组中连续子数组的和的最大值
"""


# 方法一 穷举法---时间复杂度约n^2
def maxOfSum(ls):
    maxsofar = 0
    n = len(ls)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += ls[j]
            maxsofar = max(maxsofar,sum)
    return maxsofar


# 方法二  动态规划法---时间复杂度约O(n)
"""
Kadane算法又被称为扫描法，为动态规划（dynamic programming）的一个典型应用。我们用DP来解决最大子数组和问题：对于数组a，用ci标记
子数组a[0..i]的最大和，那么则有 ci=max{ai,ci−1+ai}
子数组最大和即为maxci。
Kadane算法比上面DP更进一步，不需要用一个数组来记录中间子数组和。通过观察容易得到：若ci−1≤0，则ci=ai。用e表示以当前为结束的子数组的最大和，
以替代数组c；那么 e=max{ai,e+ai}
"""
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    ls = [1,2,3,4,-10,5,7]
    ls2 = [4]
    # maxSum = maxOfSum(ls)
    maxSum = max_subarray(ls)
    print(maxSum)

