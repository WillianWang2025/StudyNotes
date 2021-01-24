"""
对数组进行排序，使用三个指针 i、j 和 k 分别代表要找的三个数。

通过枚举 i 确定第一个数，另外两个指针 j，k 分别从左边 i + 1 和右边 n - 1 往中间移动，找到满足 nums[i] + nums[j] + nums[k] == 0 的所有组合。

j 和 k 指针的移动逻辑，分情况讨论 sum = nums[i] + nums[j] + nums[k] ：

sum > 0：k 左移，使 sum 变小
sum < 0：j 右移，使 sum 变大
sum = 0：找到符合要求的答案，存起来
由于题目要求答案不能包含重复的三元组，所以在确定第一个数和第二个数的时候，要跳过数值一样的下标（在三数之和确定的情况下，确保第一个数和第二个数不会重复，即可保证三元组不重复）。

"""


class Solution:
    def threeSum(self, nums):
        sortnums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and sortnums[i] == sortnums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if sortnums[j] + sortnums[k] < -sortnums[i]:
                    j += 1
                elif sortnums[j] + sortnums[k] > -sortnums[i]:
                    k -= 1
                else:
                    # 注意此处要先剔除重复项
                    ans.append([sortnums[i], sortnums[j], sortnums[k]])
                    while j < k and sortnums[k] == sortnums[k - 1]:
                        k -= 1
                    while j < k and sortnums[j] == sortnums[j + 1]:
                        j += 1
                    k -= 1
                    j += 1
        return ans
