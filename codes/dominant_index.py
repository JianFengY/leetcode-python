class Solution:
    """
    https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/771/
    在一个给定的数组nums中，总是存在一个最大元素 。
    查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
    如果是，则返回最大元素的索引，否则返回-1。
    """

    def dominant_index(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy = nums[:]
        copy.remove(max(nums))
        if len(nums) == 1 or max(copy) == 0 or max(nums) >= max(copy) * 2:
            return nums.index(max(nums))
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.dominant_index([0, 0, 0, 1]))
