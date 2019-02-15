class Solution:
    """
    https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/770/
    给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
    我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
    如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
    """

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
