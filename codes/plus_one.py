class Solution:
    """
    https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/772/
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。
    """

    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(x) for x in digits])) + 1
        return [int(y) for y in list(str(num))]


if __name__ == '__main__':
    solution = Solution()
    print(solution.plus_one([9, 8, 7, 6, 5, 4, 3, 2, 9, 9]))
