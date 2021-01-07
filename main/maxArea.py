""""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
链接：https://leetcode-cn.com/problems/container-with-most-water
"""

# 算法流程： 设置双指针 ii,jj 分别位于容器壁两端，根据规则移动指针（后续说明），并且更新面积最大值 res，直到 i == j 时返回 res。
#
# 指针移动规则与证明： 每次选定围成水槽两板高度 h[i]h[i],h[j]h[j] 中的短板，向中间收窄 11 格。以下证明：
#
# 设每一状态下水槽面积为 S(i, j)S(i,j),(0 <= i < j < n)(0<=i<j<n)，由于水槽的实际高度由两板中的短板决定，则可得面积公式 S(i, j) = min(h[i], h[j]) × (j - i)S(i,j)=min(h[i],h[j])×(j−i)。
# 在每一个状态下，无论长板或短板收窄 11 格，都会导致水槽 底边宽度 -1−1：
# 若向内移动短板，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 可能变大，因此水槽面积 S(i, j)S(i,j) 可能增大。
# 若向内移动长板，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 不变或变小，下个水槽的面积一定小于当前水槽面积。
# 因此，向内收窄短板可以获取面积最大值。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        re = 0
        while left<right:
            value_left = height[left]
            value_right = height[right]
            temp = min(value_left, value_right)*(right-left)
            if temp>re:
                re = temp
            if value_left <= value_right:
                left += 1
            else:
                right -= 1
        return re
